import sys
import os

gff_file = sys.argv[1]
faidx_file = sys.argv[2]
gff_stat = sys.argv[3]

with open(gff_file, 'r') as f:
	gff = f.readlines()

with open(faidx_file, 'r') as f:
    faidx_list = f.readlines()

chrom = list()
length = list()
for i in range(len(faidx_list)):
    chrom.append(faidx_list[i].split()[0])
    length.append(faidx_list[i].split()[1])
faidx_list = dict(zip(chrom,length))

contig = list()
for i in range(len(gff)):
	if 'mRNA' in gff[i]:
		mRNA_len = int(gff[i].split()[4]) - int(gff[i].split()[3])
		if gff[i].split()[0] not in contig:
			contig.append(gff[i].split()[0])
			space = int(gff[i].split()[3]) - 0
			if len(contig) >= 2:
				tail_space = int(faidx_list[up_chrom]) - up_end
				#print(tail_space)
				with open(gff_stat, 'a') as f:
					f.writelines("0" + '\t' + str(tail_space) + '\n')
		else:
			space = int(gff[i].split()[3]) - up_end
		ID = gff[i].split()[8].split(';')[0]
		up_end = int(gff[i].split()[4])
		up_chrom = gff[i].split()[0]
		with open(gff_stat, 'a') as f:
			f.writelines(str(mRNA_len) + '\t' + str(space) + '\t' + ID + '\n')

	
