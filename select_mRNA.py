import os
import sys

print("python select.py All Primary select")

All_list = sys.argv[1]
Primary_list = sys.argv[2]
Select_list = sys.argv[3]

with open (All_list, "r") as f:
	All = f.readlines()

with open (Primary_list, "r") as f:
    Primary = f.readlines()

for i in range(len(Primary)):
	for j in range(len(All)):
		if Primary[i].strip() in All[j].strip():
			#print(Primary[i].strip(),All[j])
			with open(Select_list, 'a') as f:
				f.writelines(All[j])
			break




