# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Database_Manager.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DatabaseAccess(object):
    def setupUi(self, DatabaseAccess):
        DatabaseAccess.setObjectName("DatabaseAccess")
        DatabaseAccess.resize(479, 404)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        DatabaseAccess.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/mainIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DatabaseAccess.setWindowIcon(icon)
        self.tabWidget = QtWidgets.QTabWidget(DatabaseAccess)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 481, 461))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_base_info = QtWidgets.QWidget()
        self.tab_base_info.setObjectName("tab_base_info")
        self.line = QtWidgets.QFrame(self.tab_base_info)
        self.line.setGeometry(QtCore.QRect(0, 190, 471, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget = QtWidgets.QWidget(self.tab_base_info)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 401, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.listWidgetDB = QtWidgets.QListWidget(self.layoutWidget)
        self.listWidgetDB.setObjectName("listWidgetDB")
        self.gridLayout.addWidget(self.listWidgetDB, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonBoxBD = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBoxBD.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBoxBD.setObjectName("buttonBoxBD")
        self.horizontalLayout.addWidget(self.buttonBoxBD)
        self.pushButton_refreshlist = QtWidgets.QPushButton(self.layoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/Reload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_refreshlist.setIcon(icon1)
        self.pushButton_refreshlist.setObjectName("pushButton_refreshlist")
        self.horizontalLayout.addWidget(self.pushButton_refreshlist)
        self.pushButton_deleteFile = QtWidgets.QPushButton(self.layoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_deleteFile.setIcon(icon2)
        self.pushButton_deleteFile.setObjectName("pushButton_deleteFile")
        self.horizontalLayout.addWidget(self.pushButton_deleteFile)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_base_info)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 230, 291, 113))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.formLayout_2 = QtWidgets.QFormLayout(self.layoutWidget1)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_DBNameNew = QtWidgets.QLabel(self.layoutWidget1)
        self.label_DBNameNew.setObjectName("label_DBNameNew")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_DBNameNew)
        self.lineEditBaseName_create = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEditBaseName_create.setObjectName("lineEditBaseName_create")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditBaseName_create)
        self.label_USRNameNew = QtWidgets.QLabel(self.layoutWidget1)
        self.label_USRNameNew.setObjectName("label_USRNameNew")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_USRNameNew)
        self.lineEditUrName_new = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEditUrName_new.setObjectName("lineEditUrName_new")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditUrName_new)
        self.label_PWDNew = QtWidgets.QLabel(self.layoutWidget1)
        self.label_PWDNew.setObjectName("label_PWDNew")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_PWDNew)
        self.lineEdit_PasswordNew = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_PasswordNew.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_PasswordNew.setObjectName("lineEdit_PasswordNew")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_PasswordNew)
        self.label_RetypeNew = QtWidgets.QLabel(self.layoutWidget1)
        self.label_RetypeNew.setObjectName("label_RetypeNew")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_RetypeNew)
        self.lineEdit_RetypeNew = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_RetypeNew.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_RetypeNew.setObjectName("lineEdit_RetypeNew")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_RetypeNew)
        self.spinBox_MaxSeqDb = QtWidgets.QSpinBox(self.layoutWidget1)
        self.spinBox_MaxSeqDb.setMinimum(1)
        self.spinBox_MaxSeqDb.setObjectName("spinBox_MaxSeqDb")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spinBox_MaxSeqDb)
        self.label_maxSeqDb = QtWidgets.QLabel(self.layoutWidget1)
        self.label_maxSeqDb.setObjectName("label_maxSeqDb")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_maxSeqDb)
        self.layoutWidget2 = QtWidgets.QWidget(self.tab_base_info)
        self.layoutWidget2.setGeometry(QtCore.QRect(320, 230, 141, 91))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelWarning_DBNew = QtWidgets.QLabel(self.layoutWidget2)
        self.labelWarning_DBNew.setText("")
        self.labelWarning_DBNew.setObjectName("labelWarning_DBNew")
        self.verticalLayout.addWidget(self.labelWarning_DBNew)
        self.labelWarning_UrsNew = QtWidgets.QLabel(self.layoutWidget2)
        self.labelWarning_UrsNew.setText("")
        self.labelWarning_UrsNew.setObjectName("labelWarning_UrsNew")
        self.verticalLayout.addWidget(self.labelWarning_UrsNew)
        self.labelWarning_PWDNew = QtWidgets.QLabel(self.layoutWidget2)
        self.labelWarning_PWDNew.setText("")
        self.labelWarning_PWDNew.setObjectName("labelWarning_PWDNew")
        self.verticalLayout.addWidget(self.labelWarning_PWDNew)
        self.labelWarning_PWDRettypeNEw = QtWidgets.QLabel(self.layoutWidget2)
        self.labelWarning_PWDRettypeNEw.setText("")
        self.labelWarning_PWDRettypeNEw.setObjectName("labelWarning_PWDRettypeNEw")
        self.verticalLayout.addWidget(self.labelWarning_PWDRettypeNEw)
        self.label_success_create = QtWidgets.QLabel(self.tab_base_info)
        self.label_success_create.setGeometry(QtCore.QRect(290, 350, 171, 20))
        self.label_success_create.setText("")
        self.label_success_create.setObjectName("label_success_create")
        self.checkBox_secureLock = QtWidgets.QCheckBox(self.tab_base_info)
        self.checkBox_secureLock.setGeometry(QtCore.QRect(320, 200, 141, 20))
        self.checkBox_secureLock.setObjectName("checkBox_secureLock")
        self.label_6 = QtWidgets.QLabel(self.tab_base_info)
        self.label_6.setGeometry(QtCore.QRect(30, 150, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.layoutWidget3 = QtWidgets.QWidget(self.tab_base_info)
        self.layoutWidget3.setGeometry(QtCore.QRect(110, 170, 231, 20))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_openDB = QtWidgets.QPushButton(self.layoutWidget3)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/Dbase.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_openDB.setIcon(icon3)
        self.pushButton_openDB.setObjectName("pushButton_openDB")
        self.horizontalLayout_3.addWidget(self.pushButton_openDB)
        self.pushButtonNewDBS = QtWidgets.QPushButton(self.layoutWidget3)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/DbaseAdd.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonNewDBS.setIcon(icon4)
        self.pushButtonNewDBS.setObjectName("pushButtonNewDBS")
        self.horizontalLayout_3.addWidget(self.pushButtonNewDBS)
        self.pushButton_CreateDB = QtWidgets.QPushButton(self.tab_base_info)
        self.pushButton_CreateDB.setGeometry(QtCore.QRect(130, 350, 131, 21))
        self.pushButton_CreateDB.setObjectName("pushButton_CreateDB")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/question.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_base_info, icon5, "")
        self.baseSign = QtWidgets.QWidget()
        self.baseSign.setObjectName("baseSign")
        self.label_successSign_In = QtWidgets.QLabel(self.baseSign)
        self.label_successSign_In.setGeometry(QtCore.QRect(120, 210, 241, 20))
        self.label_successSign_In.setText("")
        self.label_successSign_In.setObjectName("label_successSign_In")
        self.layoutWidget4 = QtWidgets.QWidget(self.baseSign)
        self.layoutWidget4.setGeometry(QtCore.QRect(50, 70, 341, 51))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget4)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_userName = QtWidgets.QLabel(self.layoutWidget4)
        self.label_userName.setObjectName("label_userName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_userName)
        self.lineEditUrName = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEditUrName.setObjectName("lineEditUrName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditUrName)
        self.label_password = QtWidgets.QLabel(self.layoutWidget4)
        self.label_password.setObjectName("label_password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_password)
        self.lineEdit_Passw = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEdit_Passw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_Passw.setObjectName("lineEdit_Passw")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Passw)
        self.pushButton_SignIN = QtWidgets.QPushButton(self.baseSign)
        self.pushButton_SignIN.setGeometry(QtCore.QRect(170, 130, 111, 21))
        self.pushButton_SignIN.setObjectName("pushButton_SignIN")
        self.commandLinkButton_Prev = QtWidgets.QCommandLinkButton(self.baseSign)
        self.commandLinkButton_Prev.setGeometry(QtCore.QRect(30, 330, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.commandLinkButton_Prev.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/leftArr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_Prev.setIcon(icon6)
        self.commandLinkButton_Prev.setObjectName("commandLinkButton_Prev")
        self.label_7 = QtWidgets.QLabel(self.baseSign)
        self.label_7.setGeometry(QtCore.QRect(20, 20, 411, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_authorizedmessage = QtWidgets.QLabel(self.baseSign)
        self.label_authorizedmessage.setGeometry(QtCore.QRect(40, 180, 391, 21))
        self.label_authorizedmessage.setText("")
        self.label_authorizedmessage.setObjectName("label_authorizedmessage")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/key.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.baseSign, icon7, "")
        self.EditDB_view = QtWidgets.QWidget()
        self.EditDB_view.setObjectName("EditDB_view")
        self.label_curr_DB_name = QtWidgets.QLabel(self.EditDB_view)
        self.label_curr_DB_name.setGeometry(QtCore.QRect(20, 230, 421, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_curr_DB_name.setFont(font)
        self.label_curr_DB_name.setObjectName("label_curr_DB_name")
        self.line_2 = QtWidgets.QFrame(self.EditDB_view)
        self.line_2.setGeometry(QtCore.QRect(10, 240, 451, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButtonAddtoDB = QtWidgets.QPushButton(self.EditDB_view)
        self.pushButtonAddtoDB.setGeometry(QtCore.QRect(160, 320, 101, 21))
        self.pushButtonAddtoDB.setObjectName("pushButtonAddtoDB")
        self.layoutWidget5 = QtWidgets.QWidget(self.EditDB_view)
        self.layoutWidget5.setGeometry(QtCore.QRect(10, 260, 251, 61))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.formLayout_3 = QtWidgets.QFormLayout(self.layoutWidget5)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget5)
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit_Instructor = QtWidgets.QLineEdit(self.layoutWidget5)
        self.lineEdit_Instructor.setMaxLength(15)
        self.lineEdit_Instructor.setObjectName("lineEdit_Instructor")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Instructor)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget5)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_class_spc = QtWidgets.QLineEdit(self.layoutWidget5)
        self.lineEdit_class_spc.setObjectName("lineEdit_class_spc")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_class_spc)
        self.layoutWidget6 = QtWidgets.QWidget(self.EditDB_view)
        self.layoutWidget6.setGeometry(QtCore.QRect(290, 250, 171, 71))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_classInfo = QtWidgets.QCheckBox(self.layoutWidget6)
        self.checkBox_classInfo.setObjectName("checkBox_classInfo")
        self.verticalLayout_2.addWidget(self.checkBox_classInfo)
        self.checkBox_Include_scores = QtWidgets.QCheckBox(self.layoutWidget6)
        self.checkBox_Include_scores.setObjectName("checkBox_Include_scores")
        self.verticalLayout_2.addWidget(self.checkBox_Include_scores)
        self.checkBox_IncludePed = QtWidgets.QCheckBox(self.layoutWidget6)
        self.checkBox_IncludePed.setObjectName("checkBox_IncludePed")
        self.verticalLayout_2.addWidget(self.checkBox_IncludePed)
        self.commandLinkButtonHome = QtWidgets.QCommandLinkButton(self.EditDB_view)
        self.commandLinkButtonHome.setGeometry(QtCore.QRect(10, 350, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButtonHome.setFont(font)
        self.commandLinkButtonHome.setIcon(icon6)
        self.commandLinkButtonHome.setObjectName("commandLinkButtonHome")
        self.tableWidgetDB = QtWidgets.QTableWidget(self.EditDB_view)
        self.tableWidgetDB.setGeometry(QtCore.QRect(10, 0, 451, 161))
        self.tableWidgetDB.setObjectName("tableWidgetDB")
        self.tableWidgetDB.setColumnCount(0)
        self.tableWidgetDB.setRowCount(0)
        self.layoutWidget7 = QtWidgets.QWidget(self.EditDB_view)
        self.layoutWidget7.setGeometry(QtCore.QRect(10, 170, 111, 21))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget7)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget7)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.spinBox_DbSeq = QtWidgets.QSpinBox(self.layoutWidget7)
        self.spinBox_DbSeq.setMinimum(1)
        self.spinBox_DbSeq.setObjectName("spinBox_DbSeq")
        self.horizontalLayout_2.addWidget(self.spinBox_DbSeq)
        self.label_star1 = QtWidgets.QLabel(self.EditDB_view)
        self.label_star1.setGeometry(QtCore.QRect(130, 360, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_star1.setFont(font)
        self.label_star1.setText("")
        self.label_star1.setObjectName("label_star1")
        self.layoutWidget8 = QtWidgets.QWidget(self.EditDB_view)
        self.layoutWidget8.setGeometry(QtCore.QRect(208, 170, 251, 21))
        self.layoutWidget8.setObjectName("layoutWidget8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget8)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButtonCopySel = QtWidgets.QPushButton(self.layoutWidget8)
        self.pushButtonCopySel.setObjectName("pushButtonCopySel")
        self.horizontalLayout_4.addWidget(self.pushButtonCopySel)
        self.pushButtonDRDB = QtWidgets.QPushButton(self.layoutWidget8)
        self.pushButtonDRDB.setObjectName("pushButtonDRDB")
        self.horizontalLayout_4.addWidget(self.pushButtonDRDB)
        self.pushButtonInsrtTotals = QtWidgets.QPushButton(self.layoutWidget8)
        self.pushButtonInsrtTotals.setObjectName("pushButtonInsrtTotals")
        self.horizontalLayout_4.addWidget(self.pushButtonInsrtTotals)
        self.label_DB_Selected = QtWidgets.QLabel(self.EditDB_view)
        self.label_DB_Selected.setGeometry(QtCore.QRect(10, 200, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setItalic(True)
        self.label_DB_Selected.setFont(font)
        self.label_DB_Selected.setText("")
        self.label_DB_Selected.setObjectName("label_DB_Selected")
        self.commandLinkButtonToPrint = QtWidgets.QCommandLinkButton(self.EditDB_view)
        self.commandLinkButtonToPrint.setGeometry(QtCore.QRect(380, 350, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButtonToPrint.setFont(font)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/rightArr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButtonToPrint.setIcon(icon8)
        self.commandLinkButtonToPrint.setObjectName("commandLinkButtonToPrint")
        self.line_8 = QtWidgets.QFrame(self.EditDB_view)
        self.line_8.setGeometry(QtCore.QRect(10, 340, 451, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/tableAdd.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.EditDB_view, icon9, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.listWidget_print_fields = QtWidgets.QListWidget(self.tab)
        self.listWidget_print_fields.setGeometry(QtCore.QRect(20, 51, 121, 181))
        self.listWidget_print_fields.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget_print_fields.setObjectName("listWidget_print_fields")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 171, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.line_3 = QtWidgets.QFrame(self.tab)
        self.line_3.setGeometry(QtCore.QRect(200, 20, 261, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(230, 10, 211, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.line_4 = QtWidgets.QFrame(self.tab)
        self.line_4.setGeometry(QtCore.QRect(190, 30, 20, 131))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.tab)
        self.line_5.setGeometry(QtCore.QRect(450, 30, 20, 131))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.tab)
        self.line_6.setGeometry(QtCore.QRect(200, 150, 261, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.pushButton_sel_logo = QtWidgets.QPushButton(self.tab)
        self.pushButton_sel_logo.setGeometry(QtCore.QRect(340, 130, 111, 21))
        self.pushButton_sel_logo.setObjectName("pushButton_sel_logo")
        self.line_7 = QtWidgets.QFrame(self.tab)
        self.line_7.setGeometry(QtCore.QRect(0, 340, 481, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.pushButton_Generate = QtWidgets.QPushButton(self.tab)
        self.pushButton_Generate.setGeometry(QtCore.QRect(140, 350, 121, 21))
        self.pushButton_Generate.setObjectName("pushButton_Generate")
        self.textEdit_to_print = QtWidgets.QTextEdit(self.tab)
        self.textEdit_to_print.setGeometry(QtCore.QRect(190, 180, 271, 131))
        self.textEdit_to_print.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.textEdit_to_print.setLineWrapColumnOrWidth(0)
        self.textEdit_to_print.setObjectName("textEdit_to_print")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(260, 160, 121, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.commandLinkButtonTo_Edit = QtWidgets.QCommandLinkButton(self.tab)
        self.commandLinkButtonTo_Edit.setGeometry(QtCore.QRect(20, 350, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.commandLinkButtonTo_Edit.setFont(font)
        self.commandLinkButtonTo_Edit.setIcon(icon6)
        self.commandLinkButtonTo_Edit.setObjectName("commandLinkButtonTo_Edit")
        self.pushButtonFileLoc = QtWidgets.QPushButton(self.tab)
        self.pushButtonFileLoc.setGeometry(QtCore.QRect(270, 350, 111, 21))
        self.pushButtonFileLoc.setObjectName("pushButtonFileLoc")
        self.label_Pdf_print_err = QtWidgets.QLabel(self.tab)
        self.label_Pdf_print_err.setGeometry(QtCore.QRect(120, 320, 251, 21))
        self.label_Pdf_print_err.setText("")
        self.label_Pdf_print_err.setObjectName("label_Pdf_print_err")
        self.checkBoxSelectAll = QtWidgets.QCheckBox(self.tab)
        self.checkBoxSelectAll.setGeometry(QtCore.QRect(20, 30, 31, 16))
        self.checkBoxSelectAll.setObjectName("checkBoxSelectAll")
        self.layoutWidget9 = QtWidgets.QWidget(self.tab)
        self.layoutWidget9.setGeometry(QtCore.QRect(210, 39, 241, 91))
        self.layoutWidget9.setObjectName("layoutWidget9")
        self.formLayout_4 = QtWidgets.QFormLayout(self.layoutWidget9)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget9)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_Schl_name_print = QtWidgets.QLineEdit(self.layoutWidget9)
        self.lineEdit_Schl_name_print.setObjectName("lineEdit_Schl_name_print")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Schl_name_print)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget9)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_Author_name_print = QtWidgets.QLineEdit(self.layoutWidget9)
        self.lineEdit_Author_name_print.setObjectName("lineEdit_Author_name_print")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Author_name_print)
        self.lineEditdepartment = QtWidgets.QLineEdit(self.layoutWidget9)
        self.lineEditdepartment.setObjectName("lineEditdepartment")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditdepartment)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget9)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.lineEditTitle = QtWidgets.QLineEdit(self.layoutWidget9)
        self.lineEditTitle.setObjectName("lineEditTitle")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditTitle)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget9)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(210, 130, 101, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.layoutWidget10 = QtWidgets.QWidget(self.tab)
        self.layoutWidget10.setGeometry(QtCore.QRect(20, 250, 151, 61))
        self.layoutWidget10.setObjectName("layoutWidget10")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget10)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget10)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_3.addWidget(self.label_14)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_Seq_sel = QtWidgets.QLineEdit(self.layoutWidget10)
        self.lineEdit_Seq_sel.setObjectName("lineEdit_Seq_sel")
        self.gridLayout_2.addWidget(self.lineEdit_Seq_sel, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon10, "")

        self.retranslateUi(DatabaseAccess)
        self.tabWidget.setCurrentIndex(2)
        self.checkBoxSelectAll.clicked.connect(self.listWidget_print_fields.selectAll) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DatabaseAccess)

    def retranslateUi(self, DatabaseAccess):
        _translate = QtCore.QCoreApplication.translate
        DatabaseAccess.setWindowTitle(_translate("DatabaseAccess", "Database Manager"))
        self.label_2.setText(_translate("DatabaseAccess", "Select Database"))
        self.pushButton_refreshlist.setText(_translate("DatabaseAccess", "Reload List"))
        self.pushButton_deleteFile.setText(_translate("DatabaseAccess", "Delete"))
        self.label_DBNameNew.setText(_translate("DatabaseAccess", "Database Name"))
        self.label_USRNameNew.setText(_translate("DatabaseAccess", "User name"))
        self.label_PWDNew.setText(_translate("DatabaseAccess", "Password"))
        self.label_RetypeNew.setText(_translate("DatabaseAccess", "Retype password"))
        self.label_maxSeqDb.setText(_translate("DatabaseAccess", "Max sequence"))
        self.checkBox_secureLock.setText(_translate("DatabaseAccess", "    lock database"))
        self.label_6.setText(_translate("DatabaseAccess", "OR"))
        self.pushButton_openDB.setText(_translate("DatabaseAccess", "Open database"))
        self.pushButtonNewDBS.setText(_translate("DatabaseAccess", "New Database"))
        self.pushButton_CreateDB.setText(_translate("DatabaseAccess", "Create"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_base_info), _translate("DatabaseAccess", "Database Info"))
        self.label_userName.setText(_translate("DatabaseAccess", "User Name"))
        self.label_password.setText(_translate("DatabaseAccess", "Password"))
        self.pushButton_SignIN.setText(_translate("DatabaseAccess", "Sign-In"))
        self.commandLinkButton_Prev.setText(_translate("DatabaseAccess", "Previous"))
        self.label_7.setText(_translate("DatabaseAccess", "This database is password-locked. Please provide sign-in details."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.baseSign), _translate("DatabaseAccess", "Sign-In "))
        self.label_curr_DB_name.setText(_translate("DatabaseAccess", "      Add current scores and lessons statistics to current database"))
        self.pushButtonAddtoDB.setText(_translate("DatabaseAccess", "Add to database"))
        self.label.setText(_translate("DatabaseAccess", "Instructor Name"))
        self.label_3.setText(_translate("DatabaseAccess", "Class"))
        self.checkBox_classInfo.setText(_translate("DatabaseAccess", "Include Roll Info"))
        self.checkBox_Include_scores.setText(_translate("DatabaseAccess", "Include  scores statistics"))
        self.checkBox_IncludePed.setText(_translate("DatabaseAccess", "Include pedagogy statistics"))
        self.commandLinkButtonHome.setText(_translate("DatabaseAccess", "Home"))
        self.label_8.setText(_translate("DatabaseAccess", "Viewing Seq."))
        self.pushButtonCopySel.setText(_translate("DatabaseAccess", "Copy selection"))
        self.pushButtonDRDB.setText(_translate("DatabaseAccess", "Delete Row"))
        self.pushButtonInsrtTotals.setText(_translate("DatabaseAccess", "Insert Totals"))
        self.commandLinkButtonToPrint.setText(_translate("DatabaseAccess", "Next"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.EditDB_view), _translate("DatabaseAccess", "Edit/view Database"))
        self.label_5.setText(_translate("DatabaseAccess", "Select which fields to print"))
        self.label_12.setText(_translate("DatabaseAccess", "                                  Pdf info"))
        self.pushButton_sel_logo.setText(_translate("DatabaseAccess", "Choose logo"))
        self.pushButton_Generate.setText(_translate("DatabaseAccess", "Generate pdf"))
        self.label_15.setText(_translate("DatabaseAccess", "               Comments"))
        self.commandLinkButtonTo_Edit.setText(_translate("DatabaseAccess", "Previous"))
        self.pushButtonFileLoc.setText(_translate("DatabaseAccess", "Open file location"))
        self.checkBoxSelectAll.setText(_translate("DatabaseAccess", "All"))
        self.label_10.setText(_translate("DatabaseAccess", "School name"))
        self.label_9.setText(_translate("DatabaseAccess", "Author name"))
        self.label_16.setText(_translate("DatabaseAccess", "Department"))
        self.label_13.setText(_translate("DatabaseAccess", "Title"))
        self.label_11.setText(_translate("DatabaseAccess", "Logo (Optional)"))
        self.label_14.setText(_translate("DatabaseAccess", "     Include sequences \n"
" (commas separated )"))
        self.lineEdit_Seq_sel.setPlaceholderText(_translate("DatabaseAccess", "1,2,3..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("DatabaseAccess", "Print Database"))
import resources_rc