# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connections.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(417, 293)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_4)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setStyleSheet("QLabel {\n"
"    color: rgb(106, 106, 106);\n"
"}")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frame_3)
        self.connection_type = QtWidgets.QComboBox(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connection_type.sizePolicy().hasHeightForWidth())
        self.connection_type.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.connection_type.setFont(font)
        self.connection_type.setStyleSheet("QComboBox {\n"
"    border-radius:5px;\n"
"    background-color: rgb(232, 232, 232);\n"
"    border:1px solid rgb(159, 159, 159);\n"
"    color:rgb(99, 99, 99);\n"
"    padding:6px;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 12px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 5px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 5px;\n"
"    background-color: rgb(122, 122, 122);\n"
"    \n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    padding:6px;\n"
"    color: rgb(95, 95, 95);\n"
"    border:1px solid  rgb(159, 159, 159);\n"
"}")
        self.connection_type.setObjectName("connection_type")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/sqlite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.connection_type.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/mysql.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.connection_type.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/postgresql.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.connection_type.addItem(icon2, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/mariadb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.connection_type.addItem(icon3, "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/mongodb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.connection_type.addItem(icon4, "")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/duckdb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.connection_type.addItem(icon5, "")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/csv.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.connection_type.addItem(icon6, "")
        self.verticalLayout.addWidget(self.connection_type)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 4)
        self.horizontalLayout_4.setSpacing(16)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.btn_cancel = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy)
        self.btn_cancel.setStyleSheet("QPushButton {\n"
"    border-radius:5px;\n"
"    background-color:rgb(200, 200, 200);\n"
"    font: 75 9pt \"MS Shell Dlg 2\";\n"
"    padding:5px 15px 5px 15px;\n"
"    height:24px;\n"
"    width:54;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border-radius:5px;\n"
"    background-color:rgb(219, 219, 219) ;\n"
"    font: 75 9pt \"MS Shell Dlg 2\";\n"
"    padding:5px 15px 5px 15px;\n"
"    height:24px;\n"
"    width:54;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    font: 75 8pt \"MS Shell Dlg 2\";\n"
"    background-color:rgb(229, 229, 229) ;\n"
"    padding:5px 15px 5px 15px;\n"
"    border:1px solid rgb(200, 200, 200);\n"
"    height:24px;\n"
"    width:54;\n"
"}\n"
"\n"
"")
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_4.addWidget(self.btn_cancel)
        self.btn_accept = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_accept.sizePolicy().hasHeightForWidth())
        self.btn_accept.setSizePolicy(sizePolicy)
        self.btn_accept.setStyleSheet("QPushButton {\n"
"    border-radius:5px;\n"
"    background-color:rgb(200, 200, 200);\n"
"    font: 75 9pt \"MS Shell Dlg 2\";\n"
"    padding:5px 15px 5px 15px;\n"
"    height:24px;\n"
"    width:54;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border-radius:5px;\n"
"    background-color:rgb(219, 219, 219) ;\n"
"    font: 75 9pt \"MS Shell Dlg 2\";\n"
"    padding:5px 15px 5px 15px;\n"
"    height:24px;\n"
"    width:54;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    font: 75 8pt \"MS Shell Dlg 2\";\n"
"    background-color:rgb(229, 229, 229) ;\n"
"    padding:5px 15px 5px 15px;\n"
"    border:1px solid rgb(200, 200, 200);\n"
"    height:24px;\n"
"    width:54;\n"
"}")
        self.btn_accept.setObjectName("btn_accept")
        self.horizontalLayout_4.addWidget(self.btn_accept)
        self.verticalLayout.addWidget(self.frame_5)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.horizontalLayout_3.addWidget(self.frame_2)

        self.retranslateUi(Dialog)
        self.btn_cancel.clicked.connect(Dialog.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Connections"))
        self.label.setText(_translate("Dialog", "New Connection"))
        self.pushButton.setText(_translate("Dialog", "Import From Url"))
        self.label_3.setText(_translate("Dialog", "Connection Type"))
        self.connection_type.setItemText(0, _translate("Dialog", "SQLite"))
        self.connection_type.setItemText(1, _translate("Dialog", "MySQL"))
        self.connection_type.setItemText(2, _translate("Dialog", "PostgreSQL"))
        self.connection_type.setItemText(3, _translate("Dialog", "MariaDB"))
        self.connection_type.setItemText(4, _translate("Dialog", "MongoDB"))
        self.connection_type.setItemText(5, _translate("Dialog", "DuckDB"))
        self.connection_type.setItemText(6, _translate("Dialog", "CSV"))
        self.btn_cancel.setText(_translate("Dialog", "Cancel"))
        self.btn_accept.setText(_translate("Dialog", "Accept"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())