'''
This module comprises a collection of functions for computing various statistical metrics of descriptive type and much more. In this module,
class_list mostly refers the the global variable class_list from the ClassroomInsights main file. Here, it is passed as an argument in various functions.
Stats_op hold the values of the various options selected for descriptive statistics (mean, median, mode etc), in the main file. Seq_num refers the
a given sequence number specified in the main file. Se_range refers the range of sequences in the form S1,S2...SN.
'''
def fetch_scores_seq(seq_num,class_list):
	''' Fetches all the scores on a given column or sequence SN
	'''
	scores=[]
	seq_numstr='S'+str(seq_num)
	for student in class_list:
	#Check is score for sequence N is not empty and is number
		if student[seq_numstr].isnumeric():
		#request only positive scores
			if int(student[seq_numstr])>=0:
				scores.append(student[seq_numstr]) 
	if scores:
		scores_int=[eval(i) for i in scores]
		return scores_int
	else:
		print('Please check scores!')
		return None

def sequence_stats(seq_num,stats_op,class_list):
	''' Computes descriptive statistics for scores of sequence N
	'''
	scores_int=fetch_scores_seq(seq_num,class_list)
	if scores_int:
	#Call the main function forcomputing descriptive statistics
		return General_statistics(scores_int,stats_op)
	else:
		return None
def fetch_scores_sdt(sdt_n,seq_range,class_list):
	''' Fetches the scores of a given student across a sequence range
	'''
	scores=[]
	for student in class_list:
	#Search the student
		if sdt_n == student['REG_NUM'] or sdt_n == student['FULL_NAME']:
			for i in seq_range:
				if student[i].isnumeric():
					if int(student[i])>=0: 
						scores.append(student[i])
			#Leave loop once student is found
			break
	if scores:
		scores_int=[eval(i) for i in scores]
		return scores_int
	else:
		print('Please check scores!')
		return None
def student_stats(sdt_n,seq_range,stats_op,class_list):
	''' Computes descriptive statistics for scores of over a range of sequences 
	'''
	scores_int=fetch_scores_sdt(sdt_n,seq_range,class_list)
	if scores_int:
		return General_statistics(scores_int,stats_op)
	else:
		return None
    
def General_statistics(scores_int,stats_op):
	''' Computes descriptive statistics for a given scores and options
	'''
	from statistics import mean,mode,median,pstdev
	Gen_stats={}
	if 1 in stats_op:
		s_val=round(mean(scores_int),2)
		Gen_stats['mean']=s_val
	if 2 in stats_op:
		s_val=round(median(scores_int),2)
		Gen_stats['median']=s_val
	if 3 in stats_op:
		s_val=round(mode(scores_int),2)
		Gen_stats['mode']=s_val        
	if 4 in stats_op:
		s_val=round(pstdev(scores_int),2)
		Gen_stats['stdv']=s_val
	if 5 in stats_op:
		max_sc=max(scores_int)
		min_sc=min(scores_int)
		Gen_stats['min_scr']=min_sc
		Gen_stats['max_scr']=max_sc
	return Gen_stats
def Find_student(sdt_n,class_list):
	''' Find student and return the location along the class_list
	'''
	pos=0
	for student in class_list:
		if student['REG_NUM']==sdt_n or student['FULL_NAME']==sdt_n:
			print('Record found!: {}'.format(student['FULL_NAME']))
			return pos
		else:
			pos=pos+1
	print('No results found!')

def add_student(sdt_Biometric,class_list):
	'''Append a dictionary containing student's information to classlist
	'''
	class_list.append(sdt_Biometric)
	return class_list
	
def find_greatest_smallest_score(class_list,cutoff):
	'''Search for the list of top N-students and bottom N-students with a certain regression score. Reg_score define the slope of the regression
		line of the student's scores while class_list here is a special list of students' FULL_NAME and regression score (Reg_score) only. sup_sdts defines
		the top N-students while sub_sdts refers the bottom N-students. This function imports the module heapq which does the ranking. cutoff is just N
	'''
	import heapq
	sup_sdts=heapq.nlargest(cutoff,class_list, key= lambda sdt: sdt['Reg_score'])
	sub_sdts=heapq.nsmallest(cutoff,class_list, key= lambda sdt: sdt['Reg_score'])
	return [sup_sdts,sub_sdts]
	
def find_greatest_smallest_score_sq(class_list,seq_numstr,cutoff):
	''' Search for the list of top N-students and bottom N-students ranked based on their scores on a given sequence. sub_sdts stores the list of the
		top N-students while sub_sdts stores the list of bottom N-students. The ranking is done by the functions from heapq module. Cutoff is just N. The
		class_list here is the regular classlist with FULL_NAMES ,seqences and sexes.
	'''
	import heapq
	sup_sdts=heapq.nlargest(cutoff,class_list, key= lambda sdt:int(sdt['S'+seq_numstr]) if sdt['S'+seq_numstr].isnumeric() else 0)
	sub_sdts=heapq.nsmallest(cutoff,class_list, key= lambda sdt: int(sdt['S'+seq_numstr]) if sdt['S'+seq_numstr].isnumeric() else 0)
	return [sup_sdts,sub_sdts]
	
def count_sexes(class_list):
	''' Computes the list of the boy(M) and girls (F) in class_list and returns their respective counts
	'''
	if class_list:
		cls_boys=[sdt for sdt in class_list if sdt['SEX']=='M']
		n_boys=len(cls_boys)
		cls_girls=[sdt for sdt in class_list if sdt['SEX']=='F']
		n_girls=len(cls_girls)	
		return [n_boys,cls_boys,n_girls,cls_girls]

def find_sdt_passed(class_list,seq_num,pass_thres,stats_op):
	''' Search for students in class_list satisfying scores> threshold for a particular sequence number
	'''
	# Create a dictionary storing info on he gender statistics and counts
	Gen_stats={}
	seq_numstr='S'+str(seq_num)
	#Search boy and girls above threshold(thres) as well as their total
	BP=[sdt for sdt in class_list if sdt['SEX']=='M' and sdt[seq_numstr]!='' and int(sdt[seq_numstr])>=pass_thres]
	GP=[sdt for sdt in class_list if sdt['SEX']=='F' and sdt[seq_numstr]!='' and int(sdt[seq_numstr])>=pass_thres]
	TP=[sdt for sdt in class_list if sdt[seq_numstr]!='' and int(sdt[seq_numstr])>=pass_thres]
	if 1 in stats_op:
		Gen_stats['boys_pass']=BP
		Gen_stats['n_boys_pass']=len(BP)
	if 2 in stats_op:
		Gen_stats['n_boysP']=compute_percentage(BP,class_list)
	if 3 in stats_op:
		Gen_stats['girls_pass']=GP
		Gen_stats['n_girls_pass']=len(GP)
	if 4 in stats_op:
		Gen_stats['n_girlsP']=compute_percentage(GP,class_list)
	if 5 in stats_op:
		Gen_stats['n_total_pass']=len(TP)
	if 6 in stats_op:
		Gen_stats['n_total_passP']=compute_percentage(TP,class_list)
	return Gen_stats
def compute_percentage(metric_size1,metric_size2):
	''' Compute the percentage score of two metrics (1 and 2) and returns a message if division by zero occurs
	'''
	try:
		return round((len(metric_size1)/len(metric_size2))*100,2)
	except ZeroDivisionError:
		print('Cannot divide by zero!')
def compute_reg(x,y):
	'''Compute the regression metric of a given scores and return the slope of the latter
	'''
	from scipy import stats
	slope, intercept, r, p, std_err = stats.linregress(x, y)
	return slope, intercept