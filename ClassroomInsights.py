import sys
import os
sys.path.append(sys.path.append(os.path.join(os.path.dirname(__file__), 'CI_lib')))# include path to imports
from PyQt5.QtWidgets import QMainWindow,QDialog,QWidget,QApplication, QAction, QFileDialog,QTableWidgetItem, QInputDialog,QMenu,QSystemTrayIcon
from PyQt5 import QtWidgets, QtCore, QtGui 
from PyQt5.QtCore import Qt
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons
from PyQt5.QtGui import QIcon
#import resources
from Class_Insights_scores import*
from about import*
from Glossary import*
from Advanced_stats import*
from Pedagogy import*
from Database_Manager import*
import statsfuncs as stf
import csv
import matplotlib.pyplot as graph
import json
import sqlite3
from sqlite3 import Error
import hashlib
from appdirs import *
###############
# Set the list of student names and records.It is meant to be a mirror of the actual file
class_list=[]
#Set the list of strings from the header of the .csv file
HeadR=[]
# Stores the maximum sequence number as identified in csv file
max_seq=0
#Holds the current student Id in string
curr_sdt_ID=None
# Determine if previous displayed statistics is cleared
cleared_stats=True
# Determines if all checkbuttons are checked/unchecked
uncheck_state=True
#Holds the maximum column count of the table
col_size_max=''
# Set the maximum number of rows on the table
row_size_max=''
# Will store the path name (string) of the current file or classlist
f_name_dir=''
#Set the maximum allowed number of recent files
max_rec_files=3
#list of path+files located in DBS folder
DbFiles=[]
# current database folder
curr_DB_fold=''
# holds the path to the current selected Database file
DbFile_selected=''
# Defines variables which store the the most recent collective descriptive statistics for exporting to database window is required
stats_eval_left_export_coll={}
stats_eval_right_export_coll={}
# Define a variable to store gender counts to be exported to database if needed
sex_count_export={}
# Define variable for storing lesson and hour stats
lessonsHours_export={}
## define path variables to user data
UserData_dir=''
User_rec_dir=''
################
class Main_ui_class_Ins (QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui=Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.actionRec1.setVisible(False)
		self.ui.actionRec2.setVisible(False)
		self.ui.actionRec3.setVisible(False)
		self.ui.actionopen.triggered.connect(lambda : self.open_any_file(0))
		self.ui.actionRec1.triggered.connect(lambda : self.open_any_file(1))
		self.ui.actionRec2.triggered.connect(lambda : self.open_any_file(2))
		self.ui.actionRec3.triggered.connect(lambda : self.open_any_file(3))
		self.ui.actionSave.triggered.connect(self.saveFileDialog)
		self.ui.actionSaveAs.triggered.connect(self.saveASFileDialog)
		self.ui.actionClose_Application.triggered.connect(self.closeAllW)
		self.ui.actionAdd_record.triggered.connect(self.add_row)
		self.ui.actionInsert_Row.triggered.connect(self.insertrow)
		self.ui.actionDelete_Row.triggered.connect(self.delete_row)
		self.ui.actionFind_record.triggered.connect(self.search_table2)  
		self.ui.actionCopy.triggered.connect(self.copy_item) 
		self.ui.actionPaste.triggered.connect(self.paste_item)  
		self.ui.actionCut.triggered.connect(self.cut_item)
		self.ui.actionDelete.triggered.connect(self.del_item)
		self.ui.tableWidgetMain.itemClicked.connect(self.enable_edit_bar_top)
		self.ui.actionBar_chart.triggered.connect(lambda : self.view_sdt_as(1))
		self.ui.actionGraph.triggered.connect(lambda : self.view_sdt_as(2))
		self.ui.actionHistogram.triggered.connect(self.view_seq_Hist)
		self.ui.actionView_all_sequences.triggered.connect(self.view_seq_All)
		self.ui.actionAbout.triggered.connect(self.show_about) 
		self.ui.actionGloss.triggered.connect(self.show_glossary)  
		self.ui.actionStatistics.triggered.connect(self.show_Pedagogy) 
		self.ui.actionManage_Edit_Databases.triggered.connect(self.show_DBManager)
		self.disable_edit_bar_plus()
		self.disable_TR_menu()
		self.disable_BR_stats()
		self.disable_BL_stats()
		self.ui.pushButtonAdvStat.clicked.connect(self.show_advanced) 
		self.ui.radioButtonColl.clicked.connect(self.enable_seq_choice_coll)
		self.ui.radioButtonIndv.clicked.connect(self.enable_seq_choice_indv)
		self.ui.pushButtonComp.clicked.connect(self.compute_stats)
		self.ui.pushButtoncheck_uncheck.clicked.connect(self.check_uncheck_stats)
		self.ui.pushButtonFind_Rec.clicked.connect(self.search_table2) 
		self.ui.pushButtonInsert.clicked.connect(self.insertrow)
		self.ui.pushButton_Add_Rec.clicked.connect(self.add_row)
		self.ui.pushButtonDel.clicked.connect(self.delete_row)
		self.set_Rec_files()
		#self.setupSystemTrayIcon()
		self.show()
		
	def open_any_file(self,*args):
		global class_list
		global HeadR
		global max_seq
		global f_name_dir
		# mode args[0]=0 corresponds to opening of file from disk
		if args[0]==0:
			f_name=QFileDialog.getOpenFileName(self,'Open File','/home','Csv Files(*.csv)')
			#f_name[0] is the actual path name in string format which is stored in f_name_dir
			f_name_dir=f_name[0]
		# open file from recent 1,2 and 3
		if args[0]==1:
			if recent_Files:
				f_name_dir=recent_Files[-1]
		if args[0]==2:
			f_name_dir=recent_Files[-2]
		if args[0]==3:
			f_name_dir=recent_Files[-3]
		if f_name_dir :
			class_list=[]
			HeadR=[]
			max_seq=0
			try:
				with open(f_name_dir,'r') as f:
					reader=csv.DictReader(f)
					#Extract header info from -csv file and move interator(reader) on the file one step ahead
					HeadR=reader.fieldnames
					for std in reader:
						class_list.append(std)
					self.ui.tableWidgetMain.clear()
					self.write_table()
					self.enable_edit_bar_bottom()
			except OSError:
				print('Cannot open file!')
			else:
			#Continue execution if no exception is raised
				if HeadR:
				# Find the maximum sequence number
					max_seq=max([ eval(item[1]) for item in HeadR if len(item)==2 and item[0]=='S' and item[1].isdigit()])
					self.ui.spinBoxFrom.setMaximum(max_seq)
					self.ui.spinBoxTo.setMaximum(max_seq)
				self.clear_stats()
				# Add file path to recent files
				recent_Files.append(f_name_dir)
				# Save recent file path to JSON file and create the file if it doesn't exist
				with open(User_rec_dir, 'w+') as f:
					json.dump(recent_Files, f)
				self.set_Rec_files()
				
	def write_table(self):
		'''Writes class_list elements into the main table'''
		global HeadR
		global class_list
		global col_size_max, row_size_max
		col_size_max=len(HeadR)
		row_size_max=len(class_list)
		self.ui.tableWidgetMain.setRowCount(row_size_max)
		self.ui.tableWidgetMain.setColumnCount(col_size_max)
		# set table labels setHorizontalHeaderLabels
		self.ui.tableWidgetMain.setHorizontalHeaderLabels(HeadR)
		tab_row=0
		#take one student at a time in class_list
		for row in class_list:
			tab_col=0
			# iterate over dictionary keys
			for key in row:
			#Fetch item correspondind to key
				item=QTableWidgetItem(row[key])
				#add item at (tab_row,tab_col) to table
				self.ui.tableWidgetMain.setItem(tab_row,tab_col,item)
				tab_col+=1
			tab_row+=1
		self.update_sex_count()
	def update_sex_count(self):
		'''Implements an update of the sex count whenever the table is modified or class_list is changed'''
		global class_list
		global f_name_dir
		global sex_count_export
		sex_count=stf.count_sexes(class_list)
		if sex_count:
			self.ui.label_curr_file.setText(f_name_dir.split('/')[-1]+': M={}, F={}'.format(sex_count[0], sex_count[2]))
			sex_count_export={'M':sex_count[0],'F':sex_count[2],'T':sex_count[0]+sex_count[2]}
	def saveASFileDialog(self):
		''' Implements a regular saveAS'''
		global HeadR
		global class_list
		self.update_list()
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getSaveFileName(self,"Save As...","","All Files (*);;Csv Files (*.csv)",options=options)
		if fileName and class_list:
			try:
				with open(fileName,'w',encoding='UTF8', newline='') as f:
					writer = csv.DictWriter(f,fieldnames=HeadR)
					writer.writeheader()
					writer.writerows(class_list)
			except OSError:
				print('Problem saving file!')
		else:
			print('No file loaded!')
	def saveFileDialog(self):
		'''Implements a regular save'''
		global HeadR
		global class_list
		global f_name_dir
		self.update_list()
		if class_list:
			try:
				with open(f_name_dir,'w',encoding='UTF8', newline='') as f:
					writer = csv.DictWriter(f,fieldnames=HeadR)
					writer.writeheader()
					writer.writerows(class_list)
			except OSError:
				print('Problem saving file!')
		else:
			print('No file selected!')
		
	def enable_seq_choice_indv(self): 
		'''Enables certain functionalities if individual statistics is selected'''
		self.ui.labelFrom.setText('From')
		self.ui.labelFrom.setVisible(True)
		self.ui.labelTo.setVisible(True)   
		self.ui.spinBoxFrom.setVisible(True) 
		self.ui.spinBoxTo.setVisible(True)  
		self.ui.label_Select_Range.setText('Select sequence Range')
		self.ui.label_Select_Range.setVisible(True)
		self.enable_BL_stats()
		self.disable_BR_stats()
		self.clear_stats()
		self.ui.label_misc.setText('')
	def enable_seq_choice_coll(self):
		'''Enables certain functionalities if collective statistics is selected'''
		self.ui.labelFrom.setText('Seq. Num.')
		self.ui.labelFrom.setVisible(True)
		self.ui.spinBoxFrom.setVisible(True)
		self.ui.spinBoxTo.setVisible(False) 
		self.ui.labelTo.setVisible(False)
		self.ui.label_Select_Range.setText('Select sequence Number')
		self.ui.label_Select_Range.setVisible(True)
		self.enable_BL_stats()
		self.enable_BR_stats()
		self.clear_stats()
		self.ui.label_misc.setText('')
	def compute_stats(self):
		'''Implements the compute function of the scores statistic window'''
		global max_seq
		global class_list
		global stats_eval_left_export_coll
		global stats_eval_right_export_coll
		self.clear_stats()
		if class_list and HeadR:
			if self.ui.radioButtonIndv.isChecked() or self.ui.radioButtonColl.isChecked():
			#check is user requested a statistical measure
				if self.measure_state():
					if self.ui.radioButtonIndv.isChecked():
					#Fetch student's id
						std_id=self.get_std_id()
						# check is id is not empty and is in table
						if std_id and self.search_table(std_id):
							if self.ui.spinBoxFrom.value()<= self.ui.spinBoxTo.value():
							#search and create sequence range as list of strings 
								seq_range=list(range(self.ui.spinBoxFrom.value(), self.ui.spinBoxTo.value()+1))
								seq_range_str=[str(i) for i in seq_range]
								seq_range_concat=[x+y for x,y in zip(['S']*max_seq,seq_range_str)]
								# read the statistical options to the left and call appropriate function
								stats_op_left=self.read_stats_ops_left()
								stats_eval_left=stf.student_stats(std_id,seq_range_concat,stats_op_left,class_list)
								if stats_eval_left:
									self.set_stats_label_left(stats_eval_left)
							else:
								print('Check sequence range')
								return
						else:
							print('No input or record not found!')
							return 
					if self.ui.radioButtonColl.isChecked():
					# get sequence number and read staistical options to the left
						seq_num=self.ui.spinBoxFrom.value()
						stats_op_left=self.read_stats_ops_left()
						stats_eval_left=stf.sequence_stats(seq_num,stats_op_left,class_list)
						if stats_eval_left:
							#export collective stats to global variable
							stats_eval_left_export_coll=stats_eval_left
							#call fucntion to display stats
							self.set_stats_label_left(stats_eval_left)
							#search for the threshold which defines pass(fail)
						pass_thres=self.get_pass_thresh()
						if pass_thres:
						#read right statistical options
							stats_op_right=self.read_stats_ops_right()
							stats_eval_right=stf.find_sdt_passed(class_list,seq_num,pass_thres,stats_op_right)
							if stats_eval_right:
								# export stats to global variable but filter list of boys and girls prior
								stats_eval_right_export_coll={k:v for k,v in stats_eval_right.items() if k!='boys_pass' and k!='girls_pass'}
								self.set_stats_label_right(stats_eval_right)
				else:
					print('Please select at least one type of measure')
					return
			else:
				print('Please select at least one type of statistics!')
				return 
		else:
			print('No file selected!')
			return
					
	def read_stats_ops_left(self):
		stats_op_left=[]
		if self.ui.checkBoxMean.isChecked():
			stats_op_left.append(1)
		if self.ui.checkBoxMedian.isChecked():
			stats_op_left.append(2)
		if self.ui.checkBoxMode.isChecked():
			stats_op_left.append(3)
		if self.ui.checkBoxStddev.isChecked():
			stats_op_left.append(4)
		if self.ui.checkBoxRange.isChecked():
			stats_op_left.append(5)
		return stats_op_left
	def read_stats_ops_right(self):
		stats_op_right=[]
		if self.ui.checkBoxNboys.isChecked():
			stats_op_right.append(1)
		if self.ui.checkBoxNboysP.isChecked():
			stats_op_right.append(2)
		if self.ui.checkBoxNgirls.isChecked():
			stats_op_right.append(3)
		if self.ui.checkBoxNgirlsP.isChecked():
			stats_op_right.append(4)
		if self.ui.checkBoxTotal.isChecked():
			stats_op_right.append(5)
		if self.ui.checkBoxTotalP.isChecked():
			stats_op_right.append(6)
		return stats_op_right
		
	def get_std_id(self):
		sdt_id,ok=QInputDialog.getText(self, 'Student Info.','Enter the student\'s name or registration number:')
		if sdt_id and ok:
			self.ui.label_misc.setText('Searching :{}'.format(sdt_id))
			return sdt_id
	def get_pass_thresh(self):
		thresh,ok=QInputDialog.getInt(self, 'Pass threshold','Enter the pass threshold')
		if thresh and ok:
			return thresh
	def set_stats_label_left(self,stats_left):
		global cleared_stats
		if 'mean' in stats_left:
			self.ui.label_Mean.setText('{}'.format(stats_left['mean']))
		if 'median' in stats_left:
			self.ui.label_Median.setText('{}'.format(stats_left['median']))
		if 'mode' in stats_left:
			self.ui.label_Mode.setText('{}'.format(stats_left['mode']))
		if 'stdv' in stats_left:
			self.ui.label_Stdv.setText('{}'.format(stats_left['stdv']))
		if ('min_scr' in stats_left) and ('max_scr' in stats_left):
			self.ui.labelRange.setText('{:.2f}--{:.2f}'.format(stats_left['min_scr'],stats_left['max_scr']))
		cleared_stats=False
	def set_stats_label_right(self,stats_right):
		global cleared_stats
		if 'n_boys_pass' in stats_right:
			self.ui.label_Nboys.setText('{}'.format(stats_right['n_boys_pass']))
		if 'n_boysP' in stats_right:
			self.ui.label_NboysP.setText('{}'.format(stats_right['n_boysP']))
		if 'n_girls_pass' in stats_right:
			self.ui.label_NG.setText('{}'.format(stats_right['n_girls_pass']))
		if 'n_girlsP' in stats_right:
			self.ui.label_NGP.setText('{}'.format(stats_right['n_girlsP']))
		if 'n_total_pass' in stats_right:
			self.ui.label_T.setText('{}'.format(stats_right['n_total_pass']))
		if 'n_total_passP' in stats_right:
			self.ui.label_TP.setText('{}'.format(stats_right['n_total_passP']))
		cleared_stats=False
	def clear_stats(self):
		global cleared_stats
		if not cleared_stats:
			self.ui.label_Mean.setText('')
			self.ui.label_Median.setText('')
			self.ui.label_Mode.setText('')
			self.ui.label_Stdv.setText('')
			self.ui.labelRange.setText('')
			self.ui.label_Nboys.setText('')
			self.ui.label_NboysP.setText('')
			self.ui.label_NG.setText('')
			self.ui.label_NGP.setText('')
			self.ui.label_T.setText('')
			self.ui.label_TP.setText('')
			cleared_stats=True
	def disable_BR_stats(self):
		self.ui.checkBoxNboys.setVisible(False)
		self.ui.checkBoxNboysP.setVisible(False)
		self.ui.checkBoxNgirls.setVisible(False)
		self.ui.checkBoxNgirlsP.setVisible(False)
		self.ui.checkBoxTotal.setVisible(False)
		self.ui.checkBoxTotalP.setVisible(False)
		self.ui.label_Nboys.setVisible(False)
		self.ui.label_NboysP.setVisible(False)
		self.ui.label_NG.setVisible(False)
		self.ui.label_NGP.setVisible(False)
		self.ui.label_T.setVisible(False)
		self.ui.label_TP.setVisible(False)
		self.ui.label_Select_Gend.setVisible(False)
	def enable_BR_stats(self):
		self.ui.checkBoxNboys.setVisible(True)
		self.ui.checkBoxNboysP.setVisible(True)
		self.ui.checkBoxNgirls.setVisible(True)
		self.ui.checkBoxNgirlsP.setVisible(True)
		self.ui.checkBoxTotal.setVisible(True)
		self.ui.checkBoxTotalP.setVisible(True)
		self.ui.label_Nboys.setVisible(True)
		self.ui.label_NboysP.setVisible(True)
		self.ui.label_NG.setVisible(True)
		self.ui.label_NGP.setVisible(True)
		self.ui.label_T.setVisible(True)
		self.ui.label_TP.setVisible(True)
		self.ui.label_Select_Gend.setVisible(True)
	def disable_BL_stats(self):
		self.ui.checkBoxMean.setVisible(False)
		self.ui.checkBoxMedian.setVisible(False)
		self.ui.checkBoxMode.setVisible(False)
		self.ui.checkBoxStddev.setVisible(False)
		self.ui.label_Mean.setVisible(False)
		self.ui.label_Median.setVisible(False)
		self.ui.label_Mode.setVisible(False)
		self.ui.label_Stdv.setVisible(False) 
		self.ui.checkBoxRange.setVisible(False) 
		self.ui.label_Select_meas.setVisible(False)
	def enable_BL_stats(self):
		self.ui.checkBoxMean.setVisible(True)
		self.ui.checkBoxMedian.setVisible(True)
		self.ui.checkBoxMode.setVisible(True)
		self.ui.checkBoxStddev.setVisible(True)
		self.ui.checkBoxRange.setVisible(True)
		self.ui.label_Mean.setVisible(True)
		self.ui.label_Median.setVisible(True)
		self.ui.label_Mode.setVisible(True)
		self.ui.label_Stdv.setVisible(True) 
		self.ui.labelRange.setVisible(True)
		self.ui.label_Select_meas.setVisible(True)
	def disable_TR_menu(self):
		self.ui.labelFrom.setVisible(False)
		self.ui.labelTo.setVisible(False)   
		self.ui.spinBoxFrom.setVisible(False) 
		self.ui.spinBoxTo.setVisible(False)  
		self.ui.label_Select_Range.setVisible(False)
	def uncheck_type(self):
		self.ui.radioButtonColl.setChecked(False)
		self.ui.radioButtonIndv.setChecked(False)
		
	def check_uncheck_stats(self):
		global uncheck_state
		if uncheck_state: 
			self.ui.checkBoxMean.setChecked(True)
			self.ui.checkBoxMedian.setChecked(True)
			self.ui.checkBoxMode.setChecked(True)
			self.ui.checkBoxStddev.setChecked(True)
			self.ui.checkBoxRange.setChecked(True)
			self.ui.checkBoxNboys.setChecked(True)
			self.ui.checkBoxNboysP.setChecked(True)
			self.ui.checkBoxNgirls.setChecked(True)
			self.ui.checkBoxNgirlsP.setChecked(True)
			self.ui.checkBoxTotal.setChecked(True)
			self.ui.checkBoxTotalP.setChecked(True)
			uncheck_state=False
		else:
			self.ui.checkBoxMean.setChecked(False)
			self.ui.checkBoxMedian.setChecked(False)
			self.ui.checkBoxMode.setChecked(False)
			self.ui.checkBoxStddev.setChecked(False)
			self.ui.checkBoxRange.setChecked(False)
			self.ui.checkBoxNboys.setChecked(False)
			self.ui.checkBoxNboysP.setChecked(False)
			self.ui.checkBoxNgirls.setChecked(False)
			self.ui.checkBoxNgirlsP.setChecked(False)
			self.ui.checkBoxTotal.setChecked(False)
			self.ui.checkBoxTotalP.setChecked(False)
			uncheck_state=True
	def search_table(self,std_id):
		'''searches for instances of std_id in the main table'''
		found=False
		self.ui.tableWidgetMain.setCurrentItem(None)
		if not std_id:
			return 
			#searches for strings containing sdt_id in the entire table.
		matching_items=self.ui.tableWidgetMain.findItems(std_id,Qt.MatchContains)
		if matching_items:
			found=True
			item=matching_items[0]
			self.ui.tableWidgetMain.setCurrentItem(item)
			self.ui.label_misc.setText('Found match:{}'.format(std_id))
		else:
			self.ui.label_misc.setText('{} not found!'.format(std_id))
		return found
	def search_table2(self):
		'''Search on student id in table when the search action is clicked'''
		if class_list:
			std_id=self.get_std_id()
			self.search_table(std_id)
		else:
			print('No file selected')
			return
	def measure_state(self):
		'''check whether a statistical measure is requensted'''
		measure_bol=False
		if self.ui.checkBoxMean.isChecked() or self.ui.checkBoxMedian.isChecked() or self.ui.checkBoxMode.isChecked() or self.ui.checkBoxStddev.isChecked() or self.ui.checkBoxRange.isChecked():
			measure_bol=True
		if self.ui.checkBoxNboys.isChecked() or self.ui.checkBoxNboysP.isChecked() or self.ui.checkBoxNgirls.isChecked() or self.ui.checkBoxNgirlsP.isChecked() or self.ui.checkBoxTotal.isChecked() or self.ui.checkBoxTotalP.isChecked():
			measure_bol=True
		return measure_bol	
	def update_list(self):
		'''Updates the classlist variable when table is modified or when save or saveAS is initiated'''
		global class_list
		global HeadR
		if class_list and HeadR:
			for row in range(row_size_max):
				for col in range(col_size_max):
					item=self.ui.tableWidgetMain.item(row,col)
					key=HeadR[col]
					if item:
						class_list[row][str(key)]=item.text()
					else:
						class_list[row][str(key)]=''
			self.update_sex_count()
		else:
			print('No file selected')
	def add_row(self):
		global class_list
		global row_size_max
		if class_list:
			row_size_max+=1
			newrow={}
			class_list.append(newrow)
			self.ui.tableWidgetMain.setRowCount(row_size_max)
		else:
			print('No file selected')
		
	def delete_row(self):
		global row_size_max
		if class_list:
			row=self.ui.tableWidgetMain.currentRow()
			self.ui.tableWidgetMain.removeRow(row)
			row_size_max-=1
			self.ui.tableWidgetMain.setRowCount(row_size_max)
			deleted_row=class_list.pop(row)
			self.update_sex_count()
			if deleted_row:
				print('Deleted {}'.format(deleted_row['FULL_NAME']))
		else:
			print('No file selected')
	def insertrow(self):
		global class_list
		global row_size_max
		if class_list:
			row=self.ui.tableWidgetMain.currentRow()
			self.ui.tableWidgetMain.insertRow(row)
			class_list.insert(row,{})
			row_size_max+=1
			#self.ui.tableWidgetMain.setRowCount(row_size_max)
		else:
			print('No file selected')
	def copy_item(self):
		row=self.ui.tableWidgetMain.currentRow()
		col=self.ui.tableWidgetMain.currentColumn()
		item=self.ui.tableWidgetMain.item(row,col)
		clipboard.setText(item.text())
	def paste_item(self):
		row=self.ui.tableWidgetMain.currentRow()
		col=self.ui.tableWidgetMain.currentColumn()
		item=QTableWidgetItem(clipboard.text())
		self.ui.tableWidgetMain.setItem(row,col,item)
	def cut_item(self):
		self.copy_item()
		row=self.ui.tableWidgetMain.currentRow()
		col=self.ui.tableWidgetMain.currentColumn()
		item=QTableWidgetItem(None)
		self.ui.tableWidgetMain.setItem(row,col,item)
	def del_item(self):
		row=self.ui.tableWidgetMain.currentRow()
		col=self.ui.tableWidgetMain.currentColumn()
		item=QTableWidgetItem(None)
		self.ui.tableWidgetMain.setItem(row,col,item)
	def enable_edit_bar_bottom(self):
		'''Allow user to activate certain elements from menu after file is opened '''
		self.ui.actionAdd_record.setEnabled(True)
		self.ui.actionInsert_Row.setEnabled(True)
		self.ui.actionDelete_Row.setEnabled(True)
		self.ui.actionFind_record.setEnabled(True)
		self.ui.menuView_Scores_As.setEnabled(True)
		self.ui.actionView_all_sequences.setEnabled(True)
		self.ui.menuView_Sequence_As.setEnabled(True)
	def enable_edit_bar_top(self):
		self.ui.actionCopy.setEnabled(True)
		self.ui.actionPaste.setEnabled(True) 
		self.ui.actionCut.setEnabled(True)
		self.ui.actionDelete.setEnabled(True)
	def disable_edit_bar_plus(self):
		self.ui.actionCopy.setDisabled(True)
		self.ui.actionPaste.setDisabled(True) 
		self.ui.actionCut.setDisabled(True)
		self.ui.actionDelete.setDisabled(True)
		self.ui.actionAdd_record.setDisabled(True)
		self.ui.actionInsert_Row.setDisabled(True)
		self.ui.actionDelete_Row.setDisabled(True)
		self.ui.actionFind_record.setDisabled(True)
		self.ui.menuView_Scores_As.setDisabled(True)
		self.ui.actionView_all_sequences.setDisabled(True)
		self.ui.menuView_Sequence_As.setDisabled(True)
	def view_sdt_as(self,*args):
		''' View scores as bar chart or line graph'''
		mode=args[0]
		self.update_list()
		row=self.ui.tableWidgetMain.currentRow()
		if row!=None:
			if max_seq:
				score_str=['S'+str(i) for i in range(1,max_seq+1)]
			sdt_name=class_list[row]['FULL_NAME']
			scores_int=stf.fetch_scores_sdt(sdt_name,score_str,class_list)
			f=graph.figure()
			f.set_figwidth(6)
			f.set_figheight(4)
			if mode==1:
				graph.bar(score_str,scores_int)
			if mode==2:
				graph.plot(score_str,scores_int)
			graph.ylabel("Scores")
			graph.title('Showing scores for {}'.format(sdt_name))
			graph.show()
			print(scores_int)
	def view_seq_Hist(self):
		'''View sequence or column as histogram'''
		self.update_list()
		col=self.ui.tableWidgetMain.currentColumn()
		if HeadR[col][0]=='S' and HeadR[col][1].isdigit() and len(HeadR[col])==2:
			seq_num=int(HeadR[col][1])
			scores_int=stf.fetch_scores_seq(seq_num,class_list)
			f=graph.figure()
			f.set_figwidth(6)
			f.set_figheight(4)
			graph.hist(scores_int)
			graph.xlabel("Scores")
			graph.ylabel("Number of records")
			graph.title('Distribution of scores for S{}'.format(seq_num))
			graph.show()
		else:
			print('Not a valid column')
	def view_seq_All(self):
		'''View all sequences as Histograms in subplots'''
		self.update_list()
		#filer sequences from the header
		HeadR_seq=[label for label in HeadR if label[0]=='S' and label[1].isdigit() and len(label)==2]
		if HeadR_seq:
			#define number of subplots
			num_subplots=len(HeadR_seq)
			#set default number of columns
			if num_subplots<3:
				columns=num_subplots
			else:
				columns=3
			# set number of rows, add 1 if there's a remainder
			rows, rem=divmod(num_subplots,3)
			if rem==0:
				figure, axis= graph.subplots(rows,columns)
			else:
				figure,axis= graph.subplots(rows+1,columns)
			axis_row=0
			axis_col=0
			for i in range(num_subplots):
				seq_num=int(HeadR_seq[i][1])
				axis[axis_row,axis_col].hist(stf.fetch_scores_seq(seq_num,class_list))
				axis[axis_row,axis_col].set_title("S{}".format(seq_num))
				axis_col+=1
				if axis_col==columns:
					axis_row+=1
					axis_col=0
			#delete excess subplots 
			if rem!=0:
				while axis_col<columns:
					graph.delaxes(axis[axis_row,axis_col])
					axis_col+=1
			graph.tight_layout()
			graph.show()
			
	def set_Rec_files(self): 
		''' trucncates the recent files to ensure it satisfies the constrain of max_rec_files '''
		if recent_Files:
			size_rec=len(recent_Files)
			if size_rec>max_rec_files:
				curr_rec=max_rec_files
			else:
				curr_rec=size_rec
			path_count=0
			# search for recent files starting from the last to -max_rec_files-1
			for i in recent_Files[-1:-1*curr_rec-1:-1]:
			# split the path of recent file into base path and filename which are contained in path_rec
				path_rec=os.path.split(i)
				if path_count==0:
				#take the strings C:\ from the base path and combine with file name
					self.ui.actionRec1.setText(path_rec[0][0:3:1]+'...'+path_rec[1])
					self.ui.actionRec1.setVisible(True)
				if path_count==1:
					self.ui.actionRec2.setText(path_rec[0][0:3:1]+'...'+path_rec[1])
					self.ui.actionRec2.setVisible(True)
				if path_count==2:
					self.ui.actionRec3.setText(path_rec[0][0:3:1]+'...'+path_rec[1])
					self.ui.actionRec3.setVisible(True)
				path_count+=1
##################Show subwindows and close functions###############################
	def show_about(self):
		if hasattr(self,'abt'):
			self.abt.show()
			self.abt.activateWindow()
		else:
			self.abt=about()
			self.abt.show()
	def show_glossary(self):
		if hasattr(self,'gloss'):
			self.gloss.show()
			self.gloss.activateWindow()
		else:
			self.gloss=glossary()
			self.gloss.show()
	def show_advanced(self):
		if hasattr(self,'adv'):
			self.adv.show()
			self.adv.activateWindow()
		else:
			if class_list and f_name_dir:
				self.adv=advanced_w()
				self.adv.show()
			else:
				print('No file selected!')
	def show_Pedagogy(self):
		if hasattr(self,'pdgy'):
			self.pdgy.show()
			self.pdgy.activateWindow()
		else:
			self.pdgy=pedagogical()
			self.pdgy.show()
	def show_DBManager(self):
		if hasattr(self,'DBMWindow'):
			self.DBMWindow.show()
			self.DBMWindow.activateWindow()
		else:
			self.DBMWindow=DBMain_W()
			self.DBMWindow.show()
	def closeAllW(self):
		if hasattr(self,'abt'):
			self.abt.close()
		if hasattr(self,'gloss'):
			self.gloss.close()
		if hasattr(self,'adv'):
			self.adv.close()
		if hasattr(self,'pdgy'):
			self.pdgy.close()
		if hasattr(self,'DBMWindow'):
			self.DBMWindow.close()
		self.close()
'''	def setupSystemTrayIcon(self):
		self.tray_icon = QSystemTrayIcon(QIcon(":/mainIcon.png"))
		tray_menu = QMenu()
		open_act = tray_menu.addAction("Open")
		open_act.triggered.connect(self.show)
		tray_menu.addSeparator()
		quit_act = tray_menu.addAction("Quit")
		quit_act.triggered.connect(QApplication.quit)
		self.tray_icon.setContextMenu(tray_menu)
		self.tray_icon.show()'''
			
class about(QDialog):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Dialog_abt()
		self.ui.setupUi(self)
		self.show()
class glossary(QWidget):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Form_gloss()
		self.ui.setupUi(self)
		self.show()
		
class pedagogical(QDialog):
	def __init__(self):
		super().__init__()
		self.ui =Ui_pedagogy_stats()
		self.ui.setupUi(self)
		self.ui.calendarWidgetFROM.setSelectionMode(0)
		self.ui.calendarWidgetTO.setSelectionMode(0) 
		self.ui.pushButtonDates.setEnabled(False)
		self.ui.pushButton_comp.clicked.connect(self.compute_stats_ped)
		self.ui.pushButtonDates.clicked.connect(self.get_dates)
		self.ui.comboBox_weeks.currentIndexChanged.connect(self.enable_date_sel)
		self.show()
	def compute_stats_ped(self):
		'''Computes the main statistical metric for lessons and hours coverage from the pedagogy window'''
		global lessonsHours_export
		HDW=self.ui.spinBox_HDW.value()
		WS=self.ui.spinBox_WS.value()  
		HTS=self.ui.spinBox_HTS.value() 
		HTY=self.ui.spinBox_HTY.value() 
		HDS=HDW*WS
		Nholdays=self.ui.spinBox_days.value()
		weeks_In_yr=self.ui.spinBoxWeeks.value()+round(Nholdays/7)
		HDY=HDW*weeks_In_yr
		self.ui.label_HDS.setText(str(HDS))
		self.ui.label_HDY.setText(str(HDY))
		HTSHDS=self.compute_percentage2(HTS,HDS)
		if HTSHDS!=None:
			self.ui.label_HTSper.setText('{}'.format(HTSHDS))
		else:
			self.ui.label_HTSper.setText('Undefined')
		HTYHDY=self.compute_percentage2(HTY,HDY)
		if HTYHDY!=None:
			self.ui.label_HTYper.setText('{}'.format(HTYHDY))
		else:
			self.ui.label_HTYper.setText('Undefined')
		LDS=self.ui.spinBox_LDS.value()    
		LTS=self.ui.spinBox_LTS.value() 
		LDY=self.ui.spinBox_LDY.value()
		LTY=self.ui.spinBox_LTY.value()
		LTSLDS=self.compute_percentage2(LTS,LDS)
		if LTSLDS!=None:
			self.ui.label_LTSper.setText('{}'.format(LTSLDS))
		else:
			self.ui.label_LTSper.setText('Undefined')
		LTYLDY=self.compute_percentage2(LTY,LDY)
		if LTYLDY!=None:
			self.ui.label_LTYper.setText('{}'.format(LTYLDY))
		else:
			self.ui.label_LTYper.setText('Undefined')
		lessonsHours_export={'HDS':HDS, 'HTS':HTS ,'HTSHDS':HTSHDS ,'HDY':HDY ,'HTY':HTY ,'HTYHDY':HTYHDY ,'LDS':LDS ,'LTS':LTS ,\
		'LTSLDS':LTSLDS ,'LDY':LDY ,'LTY':LTY ,'LTYLDY':LTYLDY }
	def get_dates(self):
		startD=self.ui.calendarWidgetFROM.selectedDate()
		ENDD=self.ui.calendarWidgetTO.selectedDate()
		if startD and ENDD:
			days_In_yr=abs(startD.daysTo(ENDD))
			weeks_In_yr=round(days_In_yr/7)
			self.ui.spinBoxWeeks.setValue(weeks_In_yr)
		else:
			print('Select start and End date')
			return
	def enable_date_sel(self):
		week_sel=self.ui.comboBox_weeks.currentText()
		if week_sel=='Manual entry':
			self.ui.calendarWidgetFROM.setSelectionMode(0)
			self.ui.calendarWidgetTO.setSelectionMode(0)
			self.ui.pushButtonDates.setEnabled(False)
		if week_sel=='From Calrendar':
			self.ui.calendarWidgetFROM.setSelectionMode(1)
			self.ui.calendarWidgetTO.setSelectionMode(1)
			self.ui.pushButtonDates.setEnabled(True)
	def compute_percentage2(self,metric_1,metric_2):
		try:
			return round((metric_1/metric_2)*100,2)
		except ZeroDivisionError:
			print('Cannot divide by zero!')
class advanced_w(QDialog):
	def __init__(self):
		super().__init__()
		self.ui =Ui_Dialog_Adv_Stats()
		self.ui.setupUi(self)
		self.ui.spinBoxSeqN.setMaximum(max_seq)
		self.ui.spinBoxN.setMaximum(len(class_list))
		self.ui.pushButtonshow.clicked.connect(self.decide_show)
		self.ui.label_NDec.setText(str(self.ui.spinBoxN.value()))
		self.ui.label_NImp.setText(str(self.ui.spinBoxN.value()))
		self.ui.label_Ntop.setText(str(self.ui.spinBoxN.value()))
		self.ui.label_NBot.setText(str(self.ui.spinBoxN.value()))
		self.ui.spinBoxN.valueChanged.connect(self.set_labels_N)
		self.show()
	def decide_show(self):
		if class_list and f_name_dir!='':
			if self.ui.radioButtonTop.isChecked() or self.ui.radioButton_Bottom.isChecked():
				self.set_sup_sub_seq()
			if self.ui.radioButton_Imp.isChecked() or self.ui.radioButton_Dec.isChecked():
				self.set_sup_sub_std()
	def set_labels_N(self):
		self.ui.label_NDec.setText(str(self.ui.spinBoxN.value()))
		self.ui.label_NImp.setText(str(self.ui.spinBoxN.value()))
		self.ui.label_Ntop.setText(str(self.ui.spinBoxN.value()))
		self.ui.label_NBot.setText(str(self.ui.spinBoxN.value()))
	def set_sup_sub_seq(self):
		cutoff=self.ui.spinBoxN.value()
		seq_numstr=str(self.ui.spinBoxSeqN.value())
		sup_sdts,sub_sdts=stf.find_greatest_smallest_score_sq(class_list,seq_numstr,cutoff)
		if self.ui.radioButtonTop.isChecked():
			sup_names=[sdt['FULL_NAME'] for sdt in sup_sdts]
			self.ui.tableWidget_reg_pred.clear()
			self.Write_Advanced_Table(sup_names,1)
			self.ui.label_count.setText(str(len(sup_names))+''+' record(s)')
			
		if self.ui.radioButton_Bottom.isChecked():
			sub_names=[sdt['FULL_NAME'] for sdt in sub_sdts]
			self.ui.tableWidget_reg_pred.clear()
			self.Write_Advanced_Table(sub_names,1)
			self.ui.label_count.setText(str(len(sub_names))+''+' record(s)')
	def fetch_reg_scores(self,seq_range):
		scores=[]
		class_list_reg=[]
		for student in class_list:
			for i in seq_range:
				if student[i].isnumeric():
					if int(student[i])>=0: 
						scores.append(student[i])
			if scores:
				scores_int=[eval(i) for i in scores]
				x_scores=list(range(1,len(scores_int)+1))
				if len(scores_int)<2:
					pass
				else:	
					slope,intercept =stf.compute_reg(x_scores,scores_int)
					d={'FULL_NAME':student['FULL_NAME'],'Reg_score':slope,'Next prediction':round(slope*(max_seq+1)+intercept,1)}
					class_list_reg.append(d)
			scores.clear()
		return class_list_reg
	def set_sup_sub_std(self):
		cutoff=self.ui.spinBoxN.value()
		seq_range=list(range(1,max_seq+1))
		seq_range_str=[str(i) for i in seq_range]
		seq_range_concat=[x+y for x,y in zip(['S']*max_seq,seq_range_str)]
		class_list_reg=self.fetch_reg_scores(seq_range_concat)
		sup_sdts,sub_sdts=stf.find_greatest_smallest_score(class_list_reg,cutoff)
		if self.ui.radioButton_Imp.isChecked():
			self.ui.tableWidget_reg_pred.clear()
			self.Write_Advanced_Table(sup_sdts,2)
			self.ui.label_count.setText(str(len(sup_sdts))+''+' record(s)')
		if self.ui.radioButton_Dec.isChecked():
			self.ui.tableWidget_reg_pred.clear()
			self.Write_Advanced_Table(sub_sdts,2)
			self.ui.label_count.setText(str(len(sub_sdts))+''+' record(s)')
	def Write_Advanced_Table(self,class_list_reg,mode):
		'''Defines manner with which to write the advanced widget table. mode=1 means write only list of full names while mode=2 is for names and 
		predictions'''
		self.ui.tableWidget_reg_pred.setRowCount(len(class_list_reg))
		#set mode to write table
		self.ui.tableWidget_reg_pred.setColumnCount(mode)
		Headr_fnc=lambda mode: ['FULL_NAME','Next prediction'] if mode==2 else ['FULL_NAME']
		Headr=Headr_fnc(mode)
		self.ui.tableWidget_reg_pred.setHorizontalHeaderLabels(Headr)
		
		tab_row=0
		if mode==2:
			for row in class_list_reg:
				tab_col=0
				# iterate over dictionary keys
				for key in Headr:
				#Fetch item correspondind to key
					item=QTableWidgetItem(str(row[key]))
					#add item at (tab_row,tab_col) to table
					self.ui.tableWidget_reg_pred.setItem(tab_row,tab_col,item)
					tab_col+=1
				tab_row+=1
		if mode==1:
			tab_col=0
			for row in class_list_reg:
				item=QTableWidgetItem(row)
				self.ui.tableWidget_reg_pred.setItem(tab_row,tab_col,item)
				tab_row+=1
class DBMain_W(QDialog):
	def __init__(self):
		super().__init__()
		self.ui=Ui_DatabaseAccess()
		self.ui.setupUi(self)
		self.hideNewDB()
		self.ui.pushButtonNewDBS.clicked.connect(self.showNewDB)
		self.ui.pushButton_refreshlist.clicked.connect(self.setDB_list)
		self.ui.pushButton_CreateDB.clicked.connect(self.createDB)
		#enable security lock on new database
		self.ui.checkBox_secureLock.stateChanged.connect(self.EnableLock)
		self.ui.pushButton_deleteFile.clicked.connect(self.DeleteDbfile)
		self.ui.pushButton_openDB.clicked.connect(self.OpenNewDB)
		self.ui.pushButton_SignIN.clicked.connect(self.check_Authorization)
		self.ui.commandLinkButton_Prev.clicked.connect(self.GoToHome)
		self.ui.commandLinkButtonHome.clicked.connect(self.GoToHome)
		self.ui.buttonBoxBD.accepted.connect(self.ChooseSelectedDB)
		self.ui.buttonBoxBD.rejected.connect(self.DeselectedList)
		self.ui.pushButton_ShowDB.clicked.connect(self.DisplayDBTable)
		self.ui.pushButtonAddtoDB.clicked.connect(self.Insert_rowsDB)
		self.ui.pushButtonDRDB.clicked.connect(self.DeleteRowDB)
		self.ui.pushButtonInsrtTotals.clicked.connect(self.InsertTotals)
		self.ui.tabWidget.setTabEnabled(1,False)
		self.ui.tabWidget.setTabEnabled(2,False)
		self.setDB_list()
		self.show()
	def hideNewDB(self):
		self.ui.label_DBNameNew.setVisible(False)
		self.ui.label_USRNameNew.setVisible(False)
		self.ui.label_PWDNew.setVisible(False)
		self.ui.label_RetypeNew.setVisible(False)
		self.ui.lineEditBaseName_create.setVisible(False)
		self.ui.lineEditUrName_new.setVisible(False)
		self.ui.lineEdit_PasswordNew.setVisible(False)
		self.ui.lineEdit_RetypeNew.setVisible(False)
		self.ui.labelWarning_DBNew.setVisible(False)
		self.ui.labelWarning_UrsNew.setVisible(False)
		self.ui.labelWarning_PWDNew.setVisible(False)
		self.ui.labelWarning_PWDRettypeNEw.setVisible(False)	
		self.ui.pushButton_CreateDB.setVisible(False)
		self.ui.label_success_create.setVisible(False)
		self.ui.checkBox_secureLock.setVisible(False)
		self.ui.spinBox_MaxSeqDb.setVisible(False)
		self.ui.label_maxSeqDb.setVisible(False)
	def showNewDB(self):
		'''Enables bottom menu of the Database info page/tab'''
		self.ui.label_DBNameNew.setVisible(True)
		self.ui.label_USRNameNew.setVisible(True)
		self.ui.label_PWDNew.setVisible(True)
		self.ui.label_RetypeNew.setVisible(True)
		self.ui.lineEditBaseName_create.setVisible(True)
		self.ui.lineEditUrName_new.setVisible(True)
		self.ui.lineEdit_PasswordNew.setVisible(True)
		self.ui.lineEdit_RetypeNew.setVisible(True)
		self.ui.labelWarning_DBNew.setVisible(True)
		self.ui.labelWarning_UrsNew.setVisible(True)
		self.ui.labelWarning_PWDNew.setVisible(True)
		self.ui.labelWarning_PWDRettypeNEw.setVisible(True)	
		self.ui.pushButton_CreateDB.setVisible(True)
		self.ui.label_success_create.setVisible(True)
		self.ui.checkBox_secureLock.setVisible(True)
		self.disable_lock_input()
		self.ui.spinBox_MaxSeqDb.setVisible(True)
		self.ui.label_maxSeqDb.setVisible(True)
	def EnableLock(self):
		'''If check box for security lock is activated, enable user input'''
		if self.ui.checkBox_secureLock.isChecked():
			self.ui.lineEditUrName_new.setEnabled(True)
			self.ui.lineEdit_PasswordNew.setEnabled(True)
			self.ui.lineEdit_PasswordNew.setEnabled(True) 
			self.ui.lineEdit_RetypeNew.setEnabled(True)
		else:
			self.disable_lock_input()
	def disable_lock_input(self):
		'''Disable the user, and password fields when new Db is clicked'''
		self.ui.lineEditUrName_new.setEnabled(False)
		self.ui.lineEdit_PasswordNew.setEnabled(False)
		self.ui.lineEdit_PasswordNew.setEnabled(False)
		self.ui.lineEdit_RetypeNew.setEnabled(False)
	def setDB_list(self):
		''' Search the DBS folder for files ending in .db and append their string to the listview widget below search'''
		# clear existing list
		self.ui.listWidgetDB.clear()
		#Reference list to hold file names
		global DbFiles
		global curr_DB_fold
		global UserData_dir
		#Get current directory and locate the DBS folder 
		curr_DB_fold=os.path.join(UserData_dir,'DBS')
		# create folder is not exist
		try:
			os.makedirs(curr_DB_fold)
		except FileExistsError:
			pass
		# iterate over files in directory and subdirectory and cpature 3 variables for eeach file
		for dirpath, dirnames, filenames in os.walk(curr_DB_fold):
			for filename in filenames:
				if filename.endswith('.db'):
					DbFiles.append(os.path.join(dirpath, filename))
					self.ui.listWidgetDB.addItem(filename)
	def clearWarnings(self):
		self.ui.labelWarning_DBNew.setText('')
		self.ui.labelWarning_UrsNew.setText('')
		self.ui.labelWarning_PWDNew.setText('')
		self.ui.labelWarning_PWDRettypeNEw.setText('')
		self.ui.label_success_create.setText('')
		
	def createDB(self):
		'''Creates a database in the DBS folder in which a password and user name table is created if that option is enabled'''
		#clear previous warnings if any
		self.clearWarnings()
		# collect input paramters for Db creation
		newDBName=self.ui.lineEditBaseName_create.text()
		usrname=self.ui.lineEditUrName_new.text()
		passwd=self.ui.lineEdit_PasswordNew.text()
		passwd_type=self.ui.lineEdit_RetypeNew.text()
		MaxSeqDB=self.ui.spinBox_MaxSeqDb.value()
		# track error flag
		create_err=False
		#set the locked state of the database
		DBlocked=False
		#check if input fields necessary for database creation are filled
		if newDBName=='':
			self.ui.labelWarning_DBNew.setText('Enter Database name!')
			create_err=True
		if self.ui.checkBox_secureLock.isChecked():
			if usrname=='':
				self.ui.labelWarning_UrsNew.setText('Enter User name!')	
				create_err=True
			if passwd=='':
				self.ui.labelWarning_PWDNew.setText('Enter password!')
				create_err=True
			if passwd_type=='':
				self.ui.labelWarning_PWDRettypeNEw.setText('Retype password!')
				create_err=True
			if passwd!=passwd_type:
				self.ui.label_success_create.setText('Passwords do not match!')
				create_err=True
			#set database lock status if requested
			DBlocked=True
		if not create_err:
			try:
				conn = sqlite3.connect(os.path.join(curr_DB_fold,newDBName+".db"))
				self.ui.label_success_create.setText("Database is created!")
			except Error as e:
				self.label_success_create.setText("Some error has occurred!")
			else:
				#create connection to the database
				c = conn.cursor()
				# create a table of usernames and passwaords if user wishes to secure the database
				if DBlocked:
					tabDefUser="CREATE TABLE IF NOT EXISTS Users ( Username TEXT,Password TEXT);"
					c.execute(tabDefUser)
					# dump new username and hashed password into Users table
					hpasswd=hashlib.sha256(passwd.encode('utf8')).hexdigest()
					c.execute( '''INSERT INTO Users (Username,Password) VALUES (?,?)''',(usrname,hpasswd))
				#create a table of all statistical metrics including scores and pedagogic statistics
				#Cycle through number of sequences and create a table for each
				for seq in range(1,MaxSeqDB+1):
					StatsNumStr="Statistics"+"_"+"S"+str(seq)
					tabDefStats="CREATE TABLE IF NOT EXISTS "+StatsNumStr+" ( Class TEXT, Teacher TEXT ,Roll INT, NBoys INT, NGirls INT,\
					Mean INT,Median INT,Mode INT,standard_dev INT,Min_scr INT, Max_scr INT, Boys_pass INT, Boys_pass_per INT,Girls_pass INT,\
					Girls_pass_per INT,Total_pass INT, Total_pass_per INT, HD_seq INT, HT_seq INT, HT_seq_per INT,HD_yr INT, HT_yr INT,\
					HT_yr_per INT,LD_seq INT, LT_seq INT, LT_seq_per INT,LD_yr INT, LT_yr INT, LT_yr_per INT);"
					c.execute(tabDefStats)
				conn.commit()
				conn.close()
				#update list of databases
				self.setDB_list()
	def DeleteDbfile(self):
		'''Deletes selected file in list of databases'''
		global curr_DB_fold
		global DbFile_selected
		ListDbFile=self.ui.listWidgetDB.currentItem()
		if ListDbFile:
			DbFile_selected=os.path.join(curr_DB_fold,ListDbFile.text())
			try:
				os.remove(DbFile_selected)
				self.setDB_list()
			except OSError:
				pass
	def ChooseSelectedDB(self):
		global curr_DB_fold
		global DbFile_selected
		ListDbFile=self.ui.listWidgetDB.currentItem()
		if ListDbFile:
			DbFile_selected=os.path.join(curr_DB_fold,ListDbFile.text())
			try:
				conn = sqlite3.connect(DbFile_selected)
			except Error as e:
				print("Error accessing Database!")
			else:
				c = conn.cursor()
				c.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Users' ''')
				#If Users table is present move to sign-in form and disable the other tabs
				if c.fetchone()[0]==1:
					self.ui.tabWidget.setTabEnabled(1,True)
					#find index of given page and set it as focus
					self.ui.tabWidget.setCurrentWidget(self.ui.tabWidget.widget(1))
					self.ui.tabWidget.setTabEnabled(1,True)	
					self.ui.tabWidget.setTabEnabled(0,False)
					self.ui.tabWidget.setTabEnabled(2,False)
				# if no Users table is present, move to edit page and disbale previous pages
				else:
					self.ui.tabWidget.setCurrentWidget(self.ui.tabWidget.widget(2))
					self.ui.tabWidget.setTabEnabled(2,True)
					self.ui.tabWidget.setTabEnabled(1,False)	
					self.ui.tabWidget.setTabEnabled(0,False)
					file_name_text=os.path.basename(DbFile_selected)
					self.ui.label_DB_Selected.setText('DB: '+file_name_text)
				conn.commit()
				conn.close()
	def DeselectedList(self):
		self.ui.listWidgetDB.setCurrentItem(None)
	def OpenNewDB(self):
		global DbFile_selected
		DBf_name=QFileDialog.getOpenFileName(self,'Open Databse File','/home','Database Files(*.db)')
		#DBf_name[0] is the actual path name in string format
		DbFile_selected=DBf_name[0]
		conn=self.conToDB()
		if conn:
			c=conn.cursor()
			c = conn.cursor()
			c.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Users' ''')
			if c.fetchone()[0]==1:
				self.ui.tabWidget.setTabEnabled(1,True)
				#find index of given page and set it as focus
				self.ui.tabWidget.setCurrentWidget(self.ui.tabWidget.widget(1))
				self.ui.tabWidget.setTabEnabled(1,True)	
				self.ui.tabWidget.setTabEnabled(0,False)
				self.ui.tabWidget.setTabEnabled(2,False)
			else:
				self.ui.tabWidget.setCurrentWidget(self.ui.tabWidget.widget(2))
				self.ui.tabWidget.setTabEnabled(2,True)
				self.ui.tabWidget.setTabEnabled(1,False)	
				self.ui.tabWidget.setTabEnabled(0,False)
				file_name_text=os.path.basename(DbFile_selected)
				self.ui.label_DB_Selected.setText('DB: '+file_name_text)
			conn.commit()
			conn.close()
	def check_Authorization(self):
		'''Check if user has access to database based on password and username'''
		conn=self.conToDB()
		if conn:
			c = conn.cursor()
			# fetch all ids from the users table and compare with entered inputs
			c.execute('''SELECT* FROM Users''')
			ids=c.fetchall()
			#assume user isn't authorized
			authorizd=False
			#read input from user
			USName=self.ui.lineEditUrName.text()
			PassW=self.ui.lineEdit_Passw.text()
			#Hash password
			HPassW=hashlib.sha256(PassW.encode('utf8')).hexdigest()
			#compare input to ids in database
			for id in ids:
				if (USName,HPassW)==id:
					authorizd=True
			#If authorizd, move to the edit page
			if authorizd:
				self.ui.tabWidget.setCurrentWidget(self.ui.tabWidget.widget(2))
				self.ui.tabWidget.setTabEnabled(2,True)
				self.ui.label_authorizedmessage.setText('')
				self.ui.tabWidget.setTabEnabled(1,False)
				#update middle text
				file_name_text=os.path.basename(DbFile_selected)
				self.ui.label_DB_Selected.setText('DB: '+file_name_text)
				
			else:
				self.ui.label_authorizedmessage.setText("Incorrect username or password!")
			conn.commit()
			conn.close()
	def GoToHome(self):
		# Disables the sign-In form
		self.ui.tabWidget.setCurrentWidget(self.ui.tabWidget.widget(0))
		self.ui.tabWidget.setTabEnabled(0,True)
		self.ui.tabWidget.setTabEnabled(1,False)
		self.ui.tabWidget.setTabEnabled(2,False)
		#clear usernames and passwords on sign_in forms and first page
		self.ui.lineEditUrName.clear()
		self.ui.lineEdit_Passw.clear()
		self.ui.lineEditBaseName_create.clear()
		self.ui.lineEditUrName_new.clear()
		self.ui.lineEdit_PasswordNew.clear()
		self.ui.lineEdit_RetypeNew.clear()
		self.ui.spinBox_MaxSeqDb.setValue(1)
		self.hideNewDB()
		self.ui.tableWidgetDB.clearContents()
	def DisplayDBTable(self):
		'''Display database in table'''
		#Create connection to database
		conn=self.conToDB()
		if conn:
			c=conn.cursor()
			# Extract statistics from specified table
			seq=self.ui.spinBox_DbSeq.value()
			# Table name
			StatsNumStr="Statistics"+"_"+"S"+str(seq)
			#determine if given table exists in DB
			c.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name=? ''',(StatsNumStr,))
			if c.fetchone()[0]==1:
				#clear warning
				self.ui.label_star1.setText('')
				c.execute("SELECT * FROM "+StatsNumStr)
				#define row number count of DB
				rowNum=0
				StatsRows=c.fetchall()
				#set row length of table
				self.ui.tableWidgetDB.setRowCount(len(StatsRows))
				#set column length of DB
				c.execute("PRAGMA table_info(%s)" % StatsNumStr)
				col_sizeDB=c.fetchall()
				self.ui.tableWidgetDB.setColumnCount(len(col_sizeDB))
				#set vertical labels
				HeaderDB=['Class','Teacher','Roll','NBoys','NGirls','Mean' ,'Median','Mode','standard_dev','Min_scr','Max_scr','Boys_pass','Boys_pass%',\
				'Girls_pass','Girls_pass%','Total_pass','Total_pass%','HD_seq','HT_seq','HT_seq%','HD_yr','HT_yr','HT_yr%','LD_seq','LT_seq','LT_seq%',\
				'LD_yr','LT_yr','LT_yr_per']
				self.ui.tableWidgetDB.setHorizontalHeaderLabels(HeaderDB)
				for StatsRow in StatsRows:
					#define column count of DB
					colNum=0
					for Stats in StatsRow:
						#if Stats:
						item=QTableWidgetItem(str(Stats))
						#else:
							#item=QTableWidgetItem('')
						self.ui.tableWidgetDB.setItem(rowNum,colNum,item)
						colNum+=1
					rowNum+=1
			else:
				self.ui.label_star1.setText('Table does not exist')
			conn.commit()
			conn.close()
	def Insert_rowsDB(self):
		'''Insert rows in database'''
		global stats_eval_left_export_coll
		global stats_eval_right_export_coll
		global sex_count_export
		global lessonsHours_export
		conn=self.conToDB()
		if conn:
			c=conn.cursor()
			# Read inputs from users(Teacher, class , sequence)
			seq=self.ui.spinBoxDB_Bottom.value()
			# Table name
			StatsNumStr="Statistics"+"_"+"S"+str(seq)
			intructor=self.ui.lineEdit_Instructor.text()
			classroom=self.ui.lineEdit_class_spc.text()
			#check if table exists
			c.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name=? ''',(StatsNumStr,))
			if c.fetchone()[0]==1:
				#insert class and teacher info
				if intructor and classroom:
					c.execute( "INSERT INTO "+StatsNumStr+" (Class,Teacher) VALUES (?,?)",(classroom,intructor))
					#clear warning
					self.ui.label_star1.setText('')
				else:
					#print('Please specify Intructor name and class')
					self.ui.label_star1.setText('Please specify Intructor name and class!')
					return
					
				# Insert gender stats
				if self.ui.checkBox_classInfo.isChecked():
					if sex_count_export:
						tuple_gender=tuple(sex_count_export.values())
						c.execute( "UPDATE "+StatsNumStr+" SET "+"NBoys=?,NGirls=?,Roll=? WHERE Class=? AND Teacher=?",tuple_gender+(classroom,intructor))
						self.ui.label_star1.setText('')
					else:
						self.ui.label_star1.setText('Roll info not available!')
						
				#insert mean, median, mode, stddv and range
				if self.ui.checkBox_Include_scores.isChecked():
					if  stats_eval_left_export_coll:
						tuple_left=tuple(stats_eval_left_export_coll.values())
						c.execute( "UPDATE "+StatsNumStr+" SET "+"Mean=?,Median=?,Mode=?,standard_dev=?,Min_scr=?,Max_scr=? WHERE Class=? AND Teacher=?",\
						tuple_left+(classroom,intructor))
						self.ui.label_star1.setText('')
					else:
						self.ui.label_star1.setText('Descriptive or Gender statistics Unavailable!')
					#insert gender stats
					if  stats_eval_right_export_coll:
						tuple_right=tuple(stats_eval_right_export_coll.values())
						c.execute( "UPDATE "+StatsNumStr+" SET "+"Boys_pass=?,Boys_pass_per=?,Girls_pass=?,Girls_pass_per=?,Total_pass=?,Total_pass_per=?\
						WHERE Class=? AND Teacher=?",tuple_right+(classroom,intructor))
						self.ui.label_star1.setText('')
					else:
						self.ui.label_star1.setText('Descriptive or Gender statistics Unavailable!')
				# insert lesson and hours stats
				if self.ui.checkBox_IncludePed.isChecked():
					if lessonsHours_export:
						tuple_lessonsHours=tuple(lessonsHours_export.values())
						c.execute( "UPDATE "+StatsNumStr+" SET "+" HD_seq=?,HT_seq=?,HT_seq_per=?,HD_yr=?,HT_yr=?,HT_yr_per=?,LD_seq=?,LT_seq=?,LT_seq_per=?,\
						LD_yr=?,LT_yr=?,LT_yr_per=? WHERE Class=? AND Teacher=?",tuple_lessonsHours+(classroom,intructor))
						self.ui.label_star1.setText('')
					else:
						self.ui.label_star1.setText('Lesson statistics not available!')
				conn.commit()
				conn.close()
				#refresh table
				self.DisplayDBTable()
			else:
				self.ui.label_star1.setText('Table does not exist')
	def DeleteRowDB(self):
		'''Delete a given row from a statistics table'''
		conn=self.conToDB()
		if conn:
			c=conn.cursor()
			# Extract statistics from specified table
			seq=self.ui.spinBox_DbSeq.value()
			# Table name
			StatsNumStr="Statistics"+"_"+"S"+str(seq)
			#determine if given table exists in DB
			c.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name=? ''',(StatsNumStr,))
			if c.fetchone()[0]==1:
				c.execute("SELECT * FROM "+StatsNumStr)	
				#get selected row from table and delete from table
				row2Del=self.ui.tableWidgetDB.currentRow()
				self.ui.tableWidgetDB.removeRow(row2Del)
				#delete row from DB file if it exists
				rows=c.fetchall()
				if row2Del<=len(rows)-1:
					rowclass=rows[row2Del][0]
					rowinstr=rows[row2Del][1]
					c.execute("DELETE FROM "+StatsNumStr+" WHERE Class=? AND Teacher=?",(rowclass,rowinstr))
				conn.commit()
				conn.close()
				#Refresh table
				self.DisplayDBTable()
			else:
				self.ui.label_star1.setText('Table does not exist')
	def InsertTotals(self):
		'''Insert totals at the bottom of the DB table'''
		conn=self.conToDB()
		if conn:
			c=conn.cursor()
			# Extract statistics from specified table
			seq=self.ui.spinBox_DbSeq.value()
			# Table name
			StatsNumStr="Statistics"+"_"+"S"+str(seq)
			#determine if given table exists in DB
			c.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name=? ''',(StatsNumStr,))
			if c.fetchone()[0]==1:
				#get row count on table
				rownum=self.ui.tableWidgetDB.rowCount()
				# increase table size 
				self.ui.tableWidgetDB.setRowCount(rownum+1)
				# GEt row to insert totals
				rownumInst=self.ui.tableWidgetDB.rowCount()-1
				total_label=QTableWidgetItem('Totals')
				self.ui.tableWidgetDB.setItem(rownumInst,0,total_label)
				total_label=QTableWidgetItem('Totals')
				self.ui.tableWidgetDB.setItem(rownumInst,1,total_label)
				#Insert totals labels
				# specify columns to sum over
				HeaderDB=['Class','Teacher','Roll','NBoys','NGirls','Mean','Median','Mode','standard_dev','Min_scr','Max_scr','Boys_pass',\
				'Boys_pass_per','Girls_pass','Girls_pass_per','Total_pass','Total_pass_per','HD_seq','HT_seq','HT_seq_per','HD_yr','HT_yr',\
				'HT_yr_per','LD_seq','LT_seq','LT_seq_per','LD_yr','LT_yr','LT_yr_per']
				#Go back to the first column to account for class and teacher fields
				colnum=0
				#select columns from Db and compute sums
				for label in HeaderDB:
					if label!='Class' and label!='Teacher' and label!='Boys_pass_per' and label!='Girls_pass_per' and label!='Total_pass_per' and label!='HT_seq_per'\
					and label!='HT_yr_per' and label!='LT_seq_per' and label!='LT_yr_per':
						c.execute("SELECT "+label+ " FROM "+StatsNumStr)
						All_col=c.fetchall()
						sumcol=sum([val[0] for val in All_col if val[0]!=None])
						#take average values for given columns
						if label in ['Mean','Median','Mode','standard_dev','Min_scr','Max_scr']:
							item=QTableWidgetItem(str(sumcol/len(All_col)))
						else:
							item=QTableWidgetItem(str(sumcol))
						self.ui.tableWidgetDB.setItem(rownumInst,colnum,item)
					colnum+=1
				#set position for computing total percentages from 'HT_seq_per' to end of row
				for colnum in range(19,29,3):
					item1=int(self.ui.tableWidgetDB.item(rownumInst,colnum-1).text())
					item2=int(self.ui.tableWidgetDB.item(rownumInst,colnum-2).text())
					try:
						item_12_per=(item1/item2)*100
						item=QTableWidgetItem(str(item_12_per))
						self.ui.tableWidgetDB.setItem(rownumInst,colnum,item)					
					except ZeroDivisionError:
						print('Cannot divide by zero!')
				#set percentages from 'Boys_pass_per' to 'Total_pass_per'
				for colnum in range(12,17,2):
					item1=int(self.ui.tableWidgetDB.item(rownumInst,colnum-1).text())
					item2=int(self.ui.tableWidgetDB.item(rownumInst,2).text())
					try:
						item_12_per=(item1/item2)*100
						item=QTableWidgetItem(str(item_12_per))
						self.ui.tableWidgetDB.setItem(rownumInst,colnum,item)					
					except ZeroDivisionError:
						print('Cannot divide by zero!')
			else:
				self.ui.label_star1.setText('Table does not exist')
			conn.commit()
			conn.close()
			#self.DisplayDBTable()
	#def fill_col_sum(self,row,col,):
	
	def conToDB(self):
		'''Create connection to database'''
		global DbFile_selected
		if DbFile_selected:
			try:
				conn = sqlite3.connect(DbFile_selected)
			except Error as e:
				print("Error accessing Database!")
				return None
			else:
				return conn
######################################MAIN#########
if __name__=="__main__":
	app = QApplication(sys.argv)
	#Define clipboard object for copying and pasting from the scores window
	clipboard=app.clipboard()
	#set user app directory
	appname = "Classsroom-Insights"
	appauthor = "LMS"
	UserData_dir=user_data_dir(appname, appauthor)
	try:
		os.makedirs(UserData_dir)
	except FileExistsError:
		pass
	User_rec_dir=os.path.join(UserData_dir,'RX.json')
	#Try to load the previous dump of recent files (max 3)
	try:
		with open(User_rec_dir, 'r') as f:
			recent_Files=json.load(f)
			if len(recent_Files)>max_rec_files:
				recent_Files=recent_Files[len(recent_Files)-3::1]
	except FileNotFoundError:
		recent_Files=[]
	w = Main_ui_class_Ins()
	w.show()
	sys.exit(app.exec_())
