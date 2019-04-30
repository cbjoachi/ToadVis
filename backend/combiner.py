import sys
import os
import glob
import pandas as pd
import numpy as np

#set working directory
os.chdir(sys.argv[1])
#find all files in the folder
extension = 'txt'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
# remove file extention
all_names = []
for fn in all_filenames:
	newstr = fn.replace("."+extension, "")
	all_names.append(newstr)

def combine( col_num, col_name):
	#combine columns from all files into one csv
	combined = pd.concat([pd.read_csv(f, usecols = [col_num]) for f in all_filenames ], axis = 1)
	combined.columns = all_names
	#slice
	max = combined.idxmax()
	normal = pd.DataFrame(columns = all_names)
	for i in range(len(all_names)):
		normal[all_names[i]] = combined.loc[max[i]-300:, all_names[i]].reset_index(drop=True)
	#replace index with range
	time = []
	step = 0
	for i in range(len(normal.index)):
		step += .005
		time.append(step)
	normal.insert(0,"Time",time)
	#export to csv
	# combined.to_csv("combined.csv", index=False, encoding='utf-8-sig')
	normal.to_csv( sys.argv[2] + "fp" + col_name + ".csv", index=False, encoding='utf-8-sig')
	
combine(0,"lateral")
combine(1,"fore")
combine(2,"normal")

