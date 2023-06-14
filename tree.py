from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.con = QWidget()
        self.setCentralWidget(self.con)
        self.con.setLayout(self.layout)
        self.tree = QTreeView()
        self.layout.addWidget(self.tree)
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Databases"])
        
        data = {
            "atento": {
                "incidencias":["1","2","3"],
                "birth":[],
            },
            "finances":{
                "transactions":["1","2","3"],
                "merchants":["1","2","3"]
            }
        }


        #data = (["Atento"], ["Incidencias","birth"], ["Empleado", "DNI", "Incidencia", "Mes"])
        self.tree_structure(data, self.model)
        self.tree.setModel(self.model)
        
    def tree_structure(self, data:dict, model:QStandardItemModel):
        #dbs, tables, columns = data

        for db in data.keys():
            db_item = QStandardItem(db)
            for table in data[db].keys():
                table_item = QStandardItem(table)
                for column in data[db][table]:
                   col_item = QStandardItem(column)
                   table_item.appendRow(col_item)
                db_item.appendRow(table_item)
            model.appendRow(db_item)
            


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec_()