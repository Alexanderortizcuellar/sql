from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import typing
import pymysql
import sqlite3
import psycopg2
from psycopg2 import extensions
import pymongo
import duckdb
from pathlib import Path
from sql import Ui_MainWindow
from dialogs import sqlitecon
from dialogs import connections
from dialogs import mysql
from dialogs import about
from dialogs import export
import rc_resources
import numpy as np







 
class Export(QDialog, export.Ui_Dialog):
    def __init__(self, parent: typing.Optional[QWidget]=None) -> None:
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.formats_list.itemClicked.connect(self.change)
    def change(self, widget:QListWidgetItem):
        index = self.formats_list.indexFromItem(widget).row()
        self.formst_uis.setCurrentIndex(index)
    



class SavedConnectionsDlg(QDialog, ):
    pass

class DataModel(QAbstractTableModel):
    def __init__(self, data, headers):
        super().__init__()
        self._data = data
        self.headers = headers
    def rowCount(self, parent: QModelIndex = ...) -> int: 
        return len(self._data)
    def columnCount(self, parent: QModelIndex = ...) -> int:
        return len(self._data[0])

    def data(self, index: QModelIndex, role: int = ...) -> typing.Any:
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> typing.Any:
        if role==Qt.DisplayRole:
            if orientation==Qt.Horizontal:
                return self.headers[section]


class DatabaseDlg(QDialog, connections.Ui_Dialog):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        sqlite_icon = QIcon(":/sqlite.png")
        mysql_icon = QIcon(":/mysql.png")
        postg_icon = QIcon(":/postgress.png")
        maria_db_icon = QIcon(":/sqlite.png")
        mongodb_icon = QIcon(":/mongodb.png")
        duckdb_icon = QIcon(":/duckdb.png")
        csv_icon = QIcon(":/csv.png")
        self.connection_type.setItemIcon(0,sqlite_icon)
        self.connection_type.setItemIcon(1,mysql_icon)
        self.connection_type.setItemIcon(2,postg_icon)
        self.connection_type.setItemIcon(3,maria_db_icon)
        self.connection_type.setItemIcon(4,mongodb_icon)
        self.connection_type.setItemIcon(5,duckdb_icon)
        self.connection_type.setItemIcon(6,csv_icon)
        self.btn_accept.pressed.connect(self.database_type)
        
    def database_type(self):
        self.database = self.connection_type.currentText()
        if self.database == "SQLite":
            self.close()
            SQliteDlg(self.parent).exec_()
        else:
            self.close()
            ConnectionsDlg(self.database, self.parent).exec_()
            
        


class SQliteDlg(QDialog, sqlitecon.Ui_Dialog):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.btn_filechooser.pressed.connect(self.choose_file)
        self.btn_connect.clicked.connect(self.connect)
        self.btn_test_con.clicked.connect(self.test_connections)
        

    def choose_file(self):
        file = QFileDialog.getOpenFileName(self,"Select Database",None,"SQLite Files(*.db *.sqlite *.SQLITE3)")
        if file:
            self.sqlitefilename.setText(file[0])

    def test_connections(self):
        database = Path(self.sqlitefilename.text())
        if database.is_file():
            try:
                name = Path(database).name.split(".")[0]
                con = sqlite3.connect(database)
            except Exception as e:
                msg = QMessageBox.critical(self, "SQL Error",str(e))
        else:
           msg = QMessageBox.critical(self, "SQL Error","File doesn't exist")

    def schema_to_json(self,db)->dict :
        name = Path(db).name.split(".")[0]
        con = sqlite3.connect(db)
        cursor = con.cursor()
        cursor2 = con.cursor()
        
        tables = cursor.execute("SELECT name FROM SQLITE_SCHEMA")
        schema = {name:{}}
        for table in tables.fetchall():
            schema[name][table[0]] = [col[1] for col in cursor2.execute(f"PRAGMA TABLE_INFO('{table[0]}')").fetchall()]
        self.parent.con = con
        return schema

    def tree_structure(self):
        self.parent.tree.setModel(None)
        model = self.parent.treemodel
        model.removeRows(0,model.rowCount())
        data = self.schema_to_json(self.sqlitefilename.text())
        for db in data.keys():
            db_item = QStandardItem(db)
            for table in data[db].keys():
                table_item = QStandardItem(table)
                for column in data[db][table]:
                   col_item = QStandardItem(column)
                   table_item.appendRow(col_item)
                db_item.appendRow(table_item)
            model.appendRow(db_item)
        self.parent.connection_history.addItem(self.sqlitefilename.text())
        self.parent.connection_history.setCurrentText(self.sqlitefilename.text())
        self.parent.tree.setModel(model) 
        self.close()
    def connect(self):
        if Path(self.sqlitefilename.text()).is_file():
            try:
                self.tree_structure()
                msg = QMessageBox.information(self, "SQL",f"Successfully connected to {self.sqlitefilename.text()}")
            except Exception as e:
                msg = QMessageBox.critical(self, "SQL Error",str(e))
        else:
            msg = QMessageBox.critical(self, "SQL Error","File doesn't exist")
            



class ConnectionsDlg(QDialog, mysql.Ui_Dialog):
    def __init__(self, kind, parent=None, *args, **kwargs):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.kind = kind
        self.ssh_frame.setVisible(False)
        self.btn_connect.pressed.connect(self.rdbms)
        self.showpassword.pressed.connect(self.show_password)
        if self.kind == "MySQL":
            self.setWindowTitle("MySQL")
            self.setWindowIcon(QIcon(":/mysql.png"))
            self.port.setValue(3306)
            self.connection_name.setText("MySQL")
            self.host.setText("localhost")
        elif self.kind == "PostgreSQL":
            self.setWindowTitle("PostgreSQL")
            self.setWindowIcon(QIcon(":/postgresql.png"))
            self.port.setValue(5432)
            self.connection_name.setText("PostgreSQL")
            self.host.setText("localhost")
        elif self.kind == "MongoDB":
            self.setWindowTitle("MongoDB")
            self.setWindowIcon(QIcon(":/mongodb.png"))
            self.port.setValue(27017)
            self.connection_name.setText("MongoDB")
            self.host.setText("localhost")
        if self.kind == "MariaDB":
            self.setWindowTitle("MariaDB")
            self.setWindowIcon(QIcon(":/Mariadb.png"))
            self.port.setValue(3306)
            self.connection_name.setText("MariaDB")
            self.host.setText("localhost")

    def rdbms(self):
        if self.kind=="MySQL":
            MySQL(self.parent, self)
        elif self.kind == "PostgreSQL":
            PosgreSQL(self.parent, self)

    def show_password(self):
        echomode = self.password.echoMode()
        if echomode == 2:
            self.password.setEchoMode(0)
            self.showpassword.setIcon(QIcon("images/hidepassword.png"))
        else:
            self.password.setEchoMode(2)
            self.showpassword.setIcon(QIcon("images/showpassword.png"))


class MySQL():
    def __init__(self,parent,dlg:mysql.Ui_Dialog) -> None:
        self.parent = parent
        self.dlg = dlg
        self.connect()

    def tree_structure(self):
        model = self.parent.treemodel
        self.parent.tree.setModel(None)
        model.removeRows(0, model.rowCount())
        con = pymysql.connect(host=self.dlg.host.text(), user=self.dlg.username.text(), passwd=self.dlg.password.text())
        cursor = con.cursor()
        cursor.execute("SHOW DATABASES;")
        databases = cursor.fetchall()

        def parse(q):
            cursor.execute(q)
            data = cursor.fetchall()
            return data
            
        tree_structure = {}
        for db in databases:
            cursor.execute(f"USE {db[0]}")
            tree_structure[db[0]] = {table[0]:[col[0] for col in parse(f"DESCRIBE {table[0]}")] for table in parse("SHOW TABLES")}
        self.parent.con = con
        default_db = self.dlg.default_database.text()
        if default_db!="":
            cursor.execute(F"USE {default_db}")
        
        for db in tree_structure.keys():
            dbs = QStandardItem(db)
            for table in tree_structure[db].keys():
                tables = QStandardItem(table)
                for col in tree_structure[db][table]:
                    cols = QStandardItem(col)
                    tables.appendRow(cols)
                dbs.appendRow(tables)
            model.appendRow(dbs)
        self.parent.tree.setModel(self.parent.treemodel)
    
    def connect(self):
        try:
            self.tree_structure()
        except Exception as e:
            msg = QMessageBox.critical(self.dlg, "SQL Error",str(e))


class PosgreSQL():
    def __init__(self, parent:Ui_MainWindow, dlg:mysql.Ui_Dialog) -> None:
        self.dlg = dlg
        self.parent = parent
        self.connect()
    def tree_structure(self):
        model:QStandardItemModel = self.parent.treemodel
        self.parent.tree.setModel(None)
        model.removeRows(0, model.rowCount())
        db = self.dlg.default_database.text()
        autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
        con = psycopg2.connect(host=self.dlg.host.text(), 
        user=self.dlg.username.text(), 
        password=self.dlg.password.text(), 
        database=db)
        con.set_isolation_level(autocommit)
        cursor = con.cursor()
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
        tables = cursor.fetchall()
        schema = {}
        for table in tables:
            cursor.execute(f"SELECT column_name, data_type FROM information_schema.columns  WHERE table_name = '{table[0]}'")
            cols = cursor.fetchall()
            schema[table[0]] =  cols

        dbs = QStandardItem(db)
        for table in tables:
            table_item = QStandardItem(table[0])
            for column in schema[table[0]]:
                col = QStandardItem(f"{column[0]} ({column[1]})")
                table_item.appendRow(col)
            dbs.appendRow(table_item)
        model.appendRow(dbs)
        self.parent.tree.setModel(model)
        self.parent.con = con
    def connect(self):
        try:
            self.tree_structure()
        except psycopg2.Error as e:
            msg = QMessageBox.critical(self.dlg, "SQL Error",str(e))
        
        except Exception as e:
            msg = QMessageBox.critical(self.dlg, "SQL Error",str(e))









    


class AboutDlg(QDialog, about.Ui_Dialog):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__()
        self.setupUi(self)
        self.label.setPixmap(QPixmap(":/window-icon.png"))




class Queries():
    def __init__(self, parent:Ui_MainWindow,con) -> None:
        self.parent = parent
        self.con = con
        try:
            self.format_table()
        except Exception as e:
            msg = QMessageBox.critical(self.parent, "SQL Error",str(e))

    def query(self):
        data = [[]]
        headers = []
        try:
            cursor = self.con.cursor()
            cursor.execute(self.parent.query_editor.toPlainText())
            data = cursor.fetchall()
            headers = [column[0] for column in cursor.description] 
        except Exception as e:
                msg = QMessageBox.critical(self.parent, "SQL Error",str(e))
        return data, headers

    def format_table(self):
        self.parent.table.setModel(None)
        data,headers = self.query()
        if len(data)>0:
            self.parent.model = DataModel(data, headers)
            self.parent.table.setModel(self.parent.model)
            self.parent.query_info.setText(f"{self.parent.model.rowCount():,} rows fetched")
            print(data)
            

    def close_connection(self):
        try:
            self.con.close()
            self.treemodel.removeRows(0,self.treemodel.rowCount())
            msg = QMessageBox.information(self, "SQL Connection","Connection Succesfully closed.")
            
        except Exception as e:
            msg = QMessageBox.critical(self, "SQL Error",str(e))

    

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(":/window-icon.png"))
        self.refresh_btn.setIcon(QIcon(":/refresh.png"))
        self.database_btn.setIcon(QIcon(":/database.png"))
        self.query_history_btn.setIcon(QIcon(":/queries.png"))
        self.main_splitter.setStretchFactor(0,0)
        self.main_splitter.setStretchFactor(1,1)
        self.treemodel = QStandardItemModel()
        self.treemodel.setHorizontalHeaderLabels(["Database"])
        self.run_query_btn.clicked.connect(self.set_up_table)
        self.save_query_btn.clicked.connect(self.save_query)
        self.database_btn.clicked.connect(self.connect)
        self.actionNew.triggered.connect(self.connect)
        self.action_Close_Connection.triggered.connect(self.close_con)
        self.action_Run.triggered.connect(self.set_up_table)
        self.action_Quit.triggered.connect(self.close)
        self.action_About.triggered.connect(self.about)
        self.export_btn.pressed.connect(self.export)
        self.tree.setModel(self.treemodel)
        self.showMaximized() 
 
    def connect(self):
        DatabaseDlg(self).exec_()

    def save_query(self):
        query = self.query_editor.toPlainText()
        file,types = QFileDialog.getSaveFileName(self, "Save", None, "SQL (*.sql)")
        if file:
            with open(file, "w") as f:
                f.write(query)

    def set_up_table(self):
        try:
            Queries(self, self.con)
        except Exception as e:
            msg = QMessageBox.critical(self, "SQL Error",str(e))
    def close_con(self):
        try:
            self.con.close()
            self.treemodel.removeRows(0,self.treemodel.rowCount())
            msg = QMessageBox.information(self, "SQL Connection","Connection Succesfully closed.")
            
        except Exception as e:
            msg = QMessageBox.critical(self, "SQL Error",str(e))
    

        
    def about(self):
        dlg = AboutDlg(self)
        dlg.exec_()

    def export(self):
        dlg = Export(self)
        dlg.exec_()

    def closeEvent(self, a0: QCloseEvent) -> None:
        msg = QMessageBox.question(self,"SQLConnector", "You are About to Quit.")
        if msg == QMessageBox.Yes:
            a0.accept()
        else:
            a0.ignore()

    
app = QApplication(sys.argv)
window = Window()
window.show()
app.exec_()
