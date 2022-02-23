import os
import sys

o_protein_file = sys.argv[1]
name_list_file = sys.argv[2]
r_protein_file = sys.argv[3]

with open(name_list_file, 'r') as f:
	name = f.readlines()
with open(o_protein_file, 'r') as f:
	o_protein = f.readlines()

key = list()
val = list()
for i in range(len(name)):
	key.append(name[i].split()[1])
	val.append(name[i].split()[0])

name_dict = dict(zip(key, val))

for i in range(len(o_protein)):
	if ">" in o_protein[i]:
		o_name = o_protein[i].strip()[1:]
		with open(r_protein_file, 'a') as f:
			f.writelines(">" + name_dict[o_name] + "\n")
	else:
		with open(r_protein_file, 'a') as f:
			f.writelines(o_protein[i])



