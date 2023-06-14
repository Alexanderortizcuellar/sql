# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sql.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(778, 653)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/database-icon-window.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color:rgb(232, 232, 232);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.main_splitter = QtWidgets.QSplitter(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_splitter.sizePolicy().hasHeightForWidth())
        self.main_splitter.setSizePolicy(sizePolicy)
        self.main_splitter.setStyleSheet("QSplitter:handle {\n"
"    background-color:rgb(0,0,0);\n"
"    width:1px;\n"
"}")
        self.main_splitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.main_splitter.setHandleWidth(0)
        self.main_splitter.setChildrenCollapsible(False)
        self.main_splitter.setObjectName("main_splitter")
        self.left = QtWidgets.QFrame(self.main_splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left.sizePolicy().hasHeightForWidth())
        self.left.setSizePolicy(sizePolicy)
        self.left.setMinimumSize(QtCore.QSize(80, 0))
        self.left.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.left.setSizeIncrement(QtCore.QSize(0, 0))
        self.left.setBaseSize(QtCore.QSize(140, 0))
        self.left.setStyleSheet("QFrame {\n"
"    background-color:rgb(232, 232, 232);\n"
"}")
        self.left.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left.setObjectName("left")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.left)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.left)
        self.frame_6.setStyleSheet("QFrame {\n"
"    background-color:rgb(232, 232, 232);\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setSpacing(22)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.database_btn = QtWidgets.QToolButton(self.frame_6)
        self.database_btn.setStyleSheet("QToolButton {\n"
"    background-color:rgb(232, 232, 232);\n"
"    border:none;\n"
"}\n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/database.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.database_btn.setIcon(icon1)
        self.database_btn.setIconSize(QtCore.QSize(30, 30))
        self.database_btn.setObjectName("database_btn")
        self.verticalLayout_8.addWidget(self.database_btn)
        self.query_history_btn = QtWidgets.QToolButton(self.frame_6)
        self.query_history_btn.setStyleSheet("QToolButton {\n"
"    background-color:rgb(232, 232, 232);\n"
"    border:none;\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/queries.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.query_history_btn.setIcon(icon2)
        self.query_history_btn.setIconSize(QtCore.QSize(30, 30))
        self.query_history_btn.setObjectName("query_history_btn")
        self.verticalLayout_8.addWidget(self.query_history_btn)
        self.refresh_btn = QtWidgets.QToolButton(self.frame_6)
        self.refresh_btn.setStyleSheet("QToolButton {\n"
"    background-color:rgb(232, 232, 232);\n"
"    border:none;\n"
"}\n"
"\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refresh_btn.setIcon(icon3)
        self.refresh_btn.setIconSize(QtCore.QSize(30, 30))
        self.refresh_btn.setObjectName("refresh_btn")
        self.verticalLayout_8.addWidget(self.refresh_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem)
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.tree_search_frame = QtWidgets.QFrame(self.left)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_search_frame.sizePolicy().hasHeightForWidth())
        self.tree_search_frame.setSizePolicy(sizePolicy)
        self.tree_search_frame.setMinimumSize(QtCore.QSize(100, 0))
        self.tree_search_frame.setStyleSheet("QFrame {\n"
"    background-color:rgb(232, 232, 232);\n"
"}")
        self.tree_search_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tree_search_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tree_search_frame.setObjectName("tree_search_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tree_search_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.tree_search_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(2, 0, 4, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.connection_history = QtWidgets.QComboBox(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connection_history.sizePolicy().hasHeightForWidth())
        self.connection_history.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.connection_history.setFont(font)
        self.connection_history.setStyleSheet("\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color:red;\n"
"}\n"
"\n"
"QComboBox:!editable {\n"
"     border:none;\n"
"     border-radius:4px;\n"
"     background-color: rgb(210,210,210);\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: rgb(210,210,210);\n"
"    border-radius:4px;\n"
"    padding:5px;\n"
"    color: rgb(56, 56, 56);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 12px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 4px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"")
        self.connection_history.setEditable(False)
        self.connection_history.setFrame(False)
        self.connection_history.setObjectName("connection_history")
        self.verticalLayout_2.addWidget(self.connection_history)
        self.tree_filter = QtWidgets.QLineEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_filter.sizePolicy().hasHeightForWidth())
        self.tree_filter.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tree_filter.setFont(font)
        self.tree_filter.setStyleSheet("QLineEdit {\n"
"    border-radius:4px;\n"
"    border:1px solid rgb(136, 136, 136);\n"
"    background-color: rgb(232, 232, 232);\n"
"    padding:5px;\n"
"}")
        self.tree_filter.setClearButtonEnabled(True)
        self.tree_filter.setObjectName("tree_filter")
        self.verticalLayout_2.addWidget(self.tree_filter)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.tree_search_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tree = QtWidgets.QTreeView(self.frame_4)
        self.tree.setFrameShape(QtWidgets.QFrame.Box)
        self.tree.setLineWidth(0)
        self.tree.setObjectName("tree")
        self.verticalLayout_3.addWidget(self.tree)
        self.verticalLayout.addWidget(self.frame_4)
        self.horizontalLayout_2.addWidget(self.tree_search_frame)
        self.right = QtWidgets.QFrame(self.main_splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.right.sizePolicy().hasHeightForWidth())
        self.right.setSizePolicy(sizePolicy)
        self.right.setMinimumSize(QtCore.QSize(150, 300))
        self.right.setStyleSheet("QFrame {\n"
"    background-color:rgb(232, 232, 232);\n"
"}")
        self.right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right.setObjectName("right")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.right)
        self.verticalLayout_9.setContentsMargins(10, 0, 0, 0)
        self.verticalLayout_9.setSpacing(1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.right_splitter = QtWidgets.QSplitter(self.right)
        self.right_splitter.setStyleSheet("QSplitter:handle {\n"
"    background-color:rgb(200,200,200);\n"
"    width:1px;\n"
"}")
        self.right_splitter.setOrientation(QtCore.Qt.Vertical)
        self.right_splitter.setHandleWidth(1)
        self.right_splitter.setChildrenCollapsible(True)
        self.right_splitter.setObjectName("right_splitter")
        self.frame_9 = QtWidgets.QFrame(self.right_splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setLineWidth(0)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_5 = QtWidgets.QFrame(self.frame_9)
        self.frame_5.setStyleSheet("QFrame {\n"
"    background-color:rgb(232, 232, 232);\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tab_manager = QtWidgets.QTabWidget(self.frame_5)
        self.tab_manager.setStyleSheet("QTabWidget {\n"
"    background-color:rgb(232, 232, 232);\n"
"    border-bottom:none;\n"
"}\n"
"\n"
"QTabWidget:pane{\n"
"    border: 0px\n"
"}")
        self.tab_manager.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab_manager.setElideMode(QtCore.Qt.ElideLeft)
        self.tab_manager.setTabsClosable(True)
        self.tab_manager.setTabBarAutoHide(False)
        self.tab_manager.setObjectName("tab_manager")
        self.main_tab = QtWidgets.QWidget()
        self.main_tab.setObjectName("main_tab")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.main_tab)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.query_editor = QtWidgets.QTextEdit(self.main_tab)
        self.query_editor.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.query_editor.setFrameShadow(QtWidgets.QFrame.Plain)
        self.query_editor.setLineWidth(0)
        self.query_editor.setObjectName("query_editor")
        self.horizontalLayout_5.addWidget(self.query_editor)
        self.tab_manager.addTab(self.main_tab, "")
        self.verticalLayout_5.addWidget(self.tab_manager)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.frame_7 = QtWidgets.QFrame(self.frame_9)
        self.frame_7.setStyleSheet("QFrame {\n"
"    background-color:rgb(232, 232, 232);\n"
"    border:none;\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setLineWidth(0)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setContentsMargins(0, 6, 9, 5)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.save_query_btn = QtWidgets.QPushButton(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_query_btn.sizePolicy().hasHeightForWidth())
        self.save_query_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save_query_btn.setFont(font)
        self.save_query_btn.setStyleSheet("QPushButton {\n"
"    background-color:rgb(222, 222, 222);\n"
"    border-radius:4px;\n"
"    border: 1px solid rgb(199, 199, 199);\n"
"    padding:5px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color:rgb(200, 200, 200);\n"
"    border-radius:4px;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color:rgb(150, 150, 150);\n"
"    border-radius:4px;\n"
"}")
        self.save_query_btn.setObjectName("save_query_btn")
        self.horizontalLayout_3.addWidget(self.save_query_btn)
        self.run_query_btn = QtWidgets.QPushButton(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.run_query_btn.sizePolicy().hasHeightForWidth())
        self.run_query_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.run_query_btn.setFont(font)
        self.run_query_btn.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(11, 11, 11);\n"
"    border-radius:4px;\n"
"    padding:5px 18px 5px 18px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(70, 70, 70);\n"
"    border-radius:4px;\n"
"    padding:5px 18px 5px 18px;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(100, 100, 100);\n"
"    border-radius:4px;\n"
"    padding:5px 18px 5px 18px;\n"
"}")
        self.run_query_btn.setObjectName("run_query_btn")
        self.horizontalLayout_3.addWidget(self.run_query_btn)
        self.verticalLayout_4.addWidget(self.frame_7)
        self.frame_11 = QtWidgets.QFrame(self.right_splitter)
        self.frame_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_7.setContentsMargins(0, -1, -1, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.table = QtWidgets.QTableView(self.frame_11)
        self.table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.table.setFrameShadow(QtWidgets.QFrame.Plain)
        self.table.setLineWidth(0)
        self.table.setSortingEnabled(True)
        self.table.setObjectName("table")
        self.verticalLayout_7.addWidget(self.table)
        self.frame = QtWidgets.QFrame(self.frame_11)
        self.frame.setStyleSheet("QFrame {\n"
"    background-color:rgb(232, 232, 232);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.refresh_btn_table = QtWidgets.QPushButton(self.frame)
        self.refresh_btn_table.setFlat(True)
        self.refresh_btn_table.setObjectName("refresh_btn_table")
        self.horizontalLayout_4.addWidget(self.refresh_btn_table)
        self.details_btn = QtWidgets.QPushButton(self.frame)
        self.details_btn.setFlat(True)
        self.details_btn.setObjectName("details_btn")
        self.horizontalLayout_4.addWidget(self.details_btn)
        self.export_btn = QtWidgets.QPushButton(self.frame)
        self.export_btn.setFlat(True)
        self.export_btn.setObjectName("export_btn")
        self.horizontalLayout_4.addWidget(self.export_btn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.query_info = QtWidgets.QLabel(self.frame)
        self.query_info.setMinimumSize(QtCore.QSize(200, 0))
        self.query_info.setText("")
        self.query_info.setObjectName("query_info")
        self.horizontalLayout_4.addWidget(self.query_info)
        self.verticalLayout_7.addWidget(self.frame)
        self.verticalLayout_9.addWidget(self.right_splitter)
        self.horizontalLayout.addWidget(self.main_splitter)
        self.verticalLayout_6.addWidget(self.main_frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 778, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menu_Edit = QtWidgets.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")
        self.menu_About = QtWidgets.QMenu(self.menubar)
        self.menu_About.setObjectName("menu_About")
        self.menu_Query = QtWidgets.QMenu(self.menubar)
        self.menu_Query.setObjectName("menu_Query")
        self.menu_Database = QtWidgets.QMenu(self.menubar)
        self.menu_Database.setObjectName("menu_Database")
        self.menu_Table = QtWidgets.QMenu(self.menubar)
        self.menu_Table.setObjectName("menu_Table")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.action_Close_Connection = QtWidgets.QAction(MainWindow)
        self.action_Close_Connection.setObjectName("action_Close_Connection")
        self.action_Quit = QtWidgets.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")
        self.action_Recent_Connections = QtWidgets.QAction(MainWindow)
        self.action_Recent_Connections.setObjectName("action_Recent_Connections")
        self.action_Save = QtWidgets.QAction(MainWindow)
        self.action_Save.setObjectName("action_Save")
        self.action_Open = QtWidgets.QAction(MainWindow)
        self.action_Open.setObjectName("action_Open")
        self.action_Run = QtWidgets.QAction(MainWindow)
        self.action_Run.setObjectName("action_Run")
        self.action_About = QtWidgets.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.action_New_Database = QtWidgets.QAction(MainWindow)
        self.action_New_Database.setObjectName("action_New_Database")
        self.action_Delete_Database = QtWidgets.QAction(MainWindow)
        self.action_Delete_Database.setObjectName("action_Delete_Database")
        self.action_Export = QtWidgets.QAction(MainWindow)
        self.action_Export.setObjectName("action_Export")
        self.action_Create_table = QtWidgets.QAction(MainWindow)
        self.action_Create_table.setObjectName("action_Create_table")
        self.action_Delete_Table = QtWidgets.QAction(MainWindow)
        self.action_Delete_Table.setObjectName("action_Delete_Table")
        self.action_Table_Information = QtWidgets.QAction(MainWindow)
        self.action_Table_Information.setObjectName("action_Table_Information")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.action_Close_Connection)
        self.menuFile.addAction(self.action_Recent_Connections)
        self.menuFile.addAction(self.action_Quit)
        self.menu_About.addAction(self.action_About)
        self.menu_Query.addAction(self.action_Save)
        self.menu_Query.addAction(self.action_Open)
        self.menu_Query.addAction(self.action_Run)
        self.menu_Database.addAction(self.action_New_Database)
        self.menu_Database.addAction(self.action_Delete_Database)
        self.menu_Table.addAction(self.action_Create_table)
        self.menu_Table.addAction(self.action_Delete_Table)
        self.menu_Table.addAction(self.action_Table_Information)
        self.menu_Table.addAction(self.action_Export)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_Database.menuAction())
        self.menubar.addAction(self.menu_Table.menuAction())
        self.menubar.addAction(self.menu_Query.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())

        self.retranslateUi(MainWindow)
        self.tab_manager.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SQl Connector"))
        self.database_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Create new connection</span></p></body></html>"))
        self.database_btn.setText(_translate("MainWindow", "..."))
        self.query_history_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Query history</p></body></html>"))
        self.query_history_btn.setText(_translate("MainWindow", "..."))
        self.refresh_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Refresh the current connection</span></p></body></html>"))
        self.refresh_btn.setText(_translate("MainWindow", "..."))
        self.tree_filter.setPlaceholderText(_translate("MainWindow", "Filter"))
        self.tab_manager.setTabText(self.tab_manager.indexOf(self.main_tab), _translate("MainWindow", "Tab 2"))
        self.save_query_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Save the specified query</span></p></body></html>"))
        self.save_query_btn.setText(_translate("MainWindow", "Save"))
        self.run_query_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Run the query</span></p></body></html>"))
        self.run_query_btn.setText(_translate("MainWindow", "Run"))
        self.refresh_btn_table.setText(_translate("MainWindow", "Refresh"))
        self.details_btn.setText(_translate("MainWindow", "Details"))
        self.export_btn.setText(_translate("MainWindow", "Export"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menu_Edit.setTitle(_translate("MainWindow", "&Edit"))
        self.menu_About.setTitle(_translate("MainWindow", "&Help"))
        self.menu_Query.setTitle(_translate("MainWindow", "&Query"))
        self.menu_Database.setTitle(_translate("MainWindow", "&Database"))
        self.menu_Table.setTitle(_translate("MainWindow", "&Table"))
        self.actionNew.setText(_translate("MainWindow", "&New Connection"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.action_Close_Connection.setText(_translate("MainWindow", "&Close Connection"))
        self.action_Quit.setText(_translate("MainWindow", "&Quit"))
        self.action_Quit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.action_Recent_Connections.setText(_translate("MainWindow", "&Recent Connections"))
        self.action_Save.setText(_translate("MainWindow", "&Save"))
        self.action_Open.setText(_translate("MainWindow", "&Open"))
        self.action_Run.setText(_translate("MainWindow", "&Run"))
        self.action_Run.setShortcut(_translate("MainWindow", "Ctrl+Return"))
        self.action_About.setText(_translate("MainWindow", "&About"))
        self.action_New_Database.setText(_translate("MainWindow", "&New Database"))
        self.action_Delete_Database.setText(_translate("MainWindow", "&Delete Database"))
        self.action_Export.setText(_translate("MainWindow", "&Export"))
        self.action_Create_table.setText(_translate("MainWindow", "&Create table"))
        self.action_Delete_Table.setText(_translate("MainWindow", "&Delete Table"))
        self.action_Table_Information.setText(_translate("MainWindow", "&Table Information"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
