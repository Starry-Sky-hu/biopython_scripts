import os
import sys

print("Usage: python id_check.py o_protein_file r_protein_file name_list_file diff_file same_file \nprotein file is one sequence only in one line.\nseqkit seq -w 0 seq_file > seq_file_w0\n\n")

o_protein_file = sys.argv[1]
r_protein_file = sys.argv[2]
name_list_file = sys.argv[3]
diff_file = sys.argv[4]
same_file = sys.argv[5]

with open(o_protein_file, 'r') as f:
    o_protein = f.readlines()
with open(r_protein_file, 'r') as f:
    r_protein = f.readlines()
with open(name_list_file, 'r') as f:
    name = f.readlines()

key = list()
val = list()
for i in range(len(name)):
    key.append(name[i].split()[1])
    val.append(name[i].split()[0])
name_dict = dict(zip(key, val))

key = list()
val = list()
for i in range(0, len(o_protein), 2):
	key.append(o_protein[i].split()[0][1:])
	val.append(o_protein[i+1].strip())
o_protein_dict = dict(zip(key, val))

key = list()
val = list()
for i in range(0, len(r_protein), 2):
	key.append(r_protein[i].split()[0][1:])
	val.append(r_protein[i+1].strip())
r_protein_dict = dict(zip(key, val))

for key in o_protein_dict.keys():
	if o_protein_dict[key] != r_protein_dict[name_dict[key]]:
		with open(diff_file, 'a') as f:
			f.writelines(name_dict[key] + '\n')
	else:
		with open(same_file, 'a') as f:
			f.writelines(name_dict[key] + '\n')




