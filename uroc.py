#! /usr/bin/env python
import argparse 
import csv
import numpy as np
import pandas

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--judge_file')
    parser.add_argument('--student_file')
    # parser.add_argument('--outfile')
    return parser.parse_args()

def list_maker(input_file, delim, bio, eng, phy, column):
	with open(input_file) as csv_file_2:
               csv_reader = csv.reader(csv_file_2, delimiter=delim)
               for row in csv_reader:
                       white_space_remove = list(filter(None, row))
        #nt(white_space_remove)
                       if 'Biological' in row[column]:
                               bio.append(white_space_remove)
                       elif 'Engineering' in row[column]:
                               eng.append(white_space_remove)
                       elif 'Physical' in row[column]:
                               phy.append(white_space_remove)



	return bio 
	return eng
	return phy

def main():
	args = parse_args()
	bio_judge = []
	eng_judge = []
	phy_judge  = []
	bio_student = []
	eng_student = []
	phy_student = []
	judge_list_sort = list_maker(args.judge_file,'\t', bio_judge, eng_judge, phy_judge, 4)
	student_list_sort = list_maker(args.student_file,',',bio_student, eng_student, phy_student,5)
	



#	with open(args.student_file) as csv_file_2:
#                csv_reader = csv.reader(csv_file_2, delimiter=',')
#                for row in csv_reader:
#                        white_space_remove = list(filter(None, row))
#        #nt(white_space_remove)
#                        if 'Biological' in row[5]:
#                                bio_student.append(white_space_remove)
#                        elif 'Engineering' in row[5]:
#                                eng_student.append(white_space_remove)
#                        elif 'Physical' in row[5]:
#                                phy_student.append(white_space_remove)
#    
#	with open(args.judge_file) as csv_file:
#		csv_reader = csv.reader(csv_file, delimiter='\t')
#		for row in csv_reader:
#			white_space_remove = list(filter(None, row))
#	#nt(white_space_remove)
#			if 'Biological' in row[4]:
#				bio_judge.append(white_space_remove)
#			elif 'Engineering' in row[4]:
#				eng_judge.append(white_space_remove)
#			elif 'Physical' in row[4]:
#				phy_judge.append(white_space_remove)
#	print("this is physical list")
#	print(phy_judge)
#	print("this is engineering list")
#	print(eng_judge)
#	print("this is biological list")
#	print(bio_judge)	
#	print("this is physical list")
#	print(phy_student)
#	print("this is engineering list")
#	print(eng_student)
#	print("this is biological list")
#	print(bio_student)






if __name__ == '__main__':
	main()
