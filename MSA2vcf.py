import sys

msa_file = sys.argv[1]
bed_file = sys.argv[2]
ref_name = sys.argv[3]
query_name = sys.argv[4]
vcf_file = sys.argv[5]

with open(msa_file, 'r') as f:
	msa = f.readlines()
with open(bed_file, 'r') as f:
	bed = f.readlines()

chrom = bed[0].split()[0]
ref_gene_ID = bed[0].split()[3]
ref_info = msa[0].split()[0].strip('>')
query_info = msa[2].split()[0].strip('>')
query_gene_ID = msa[2].split()[1]

ref_strat = int(bed[0].split()[1]) - 5000
if(ref_strat < 0):
	ref_strat = 0

# lowcase character to upper
low2cap = {'a': 'A', 'g': 'G', 'c': 'C', 't': 'T'}

msa_dict = dict()
msa_dict['ref'] = msa[1].strip()
msa_dict["query"] = msa[3].strip()

# remove header '-'
ref_header = 0
for i in range(0, len(msa_dict['ref']), 1):
	if (msa_dict['ref'][i] == '-' or msa_dict['query'][i] == '-'):
		if(msa_dict['ref'][i] != '-'):
			ref_header += 1
		continue
	else:
		start = i
		break

end = len(msa_dict['ref']) - 1
# remove tail '-'
#for i in range(len(msa_dict['ref'])-1, -1, -1):
#	if (msa_dict['ref'][i] == '-' or msa_dict['query'] == '-'):
#		continue
#	else:
#		end = i
#		break

# write VCF header
with open(vcf_file, 'a') as f:
	f.writelines("##fileformat=VCFv4.2\n")
	f.writelines("##mafft aligned fileformat to VCF fileformat\n")
	f.writelines("##mafft --auto mafft.fa > mafft.out\n")
	f.writelines("##mafft.out start: " + str(start) + ', end: ' + str(end) + '\n')
	f.writelines("##remove reference header: " + str(ref_header) + '\n')
	f.writelines("##reference start: " + str(ref_strat) + '\n')
	f.writelines("##reference info, genome name: " + ref_name + ", position: " + ref_info + ", gene ID: " + ref_gene_ID + '\n')
	f.writelines("##query info, genome name: " + query_name + ", position: " + query_info + ", gene ID: " + query_gene_ID + '\n')
	f.writelines('#CHROM' + '\t' + 'POS' + '\t' + 'ID' + '\t' + 'REF' + '\t' + 'ALT' + '\t' + 
			'QUAL' + '\t' + 'FILTER' + '\t' + "INFO" + '\t' + 'FORMAT' + '\t' + 
			query_name + '\n')

pos = ref_header + ref_strat
i = start
while (i <= end):
	offset = 0
	if (msa_dict['ref'][i] == msa_dict['query'][i]):
		#if (msa_dict['ref'][i] != '-'):
		i += 1
		pos += 1
		continue
	else:
		if (msa_dict['ref'][i] == '-'):
			REF = low2cap[msa_dict['ref'][i-1]]
			ALT = low2cap[msa_dict['query'][i-1]]
			while (i <= end and msa_dict['ref'][i] == '-'):
				ALT = (ALT, low2cap[msa_dict['query'][i]])
				ALT = ''.join(ALT)
				i += 1
		elif (msa_dict['query'][i] == '-'):
			REF = low2cap[msa_dict['ref'][i-1]]
			ALT = low2cap[msa_dict['query'][i-1]]
			while (i <= end and msa_dict['query'][i] == '-'):
				REF = (REF, low2cap[msa_dict['ref'][i]])
				REF = ''.join(REF)
				i += 1
				pos += 1
				offset += 1
		elif (msa_dict['ref'][i] != '-' and msa_dict['query'][i] != '-'):
			REF = low2cap[msa_dict['ref'][i]]
			ALT = low2cap[msa_dict['query'][i]]
			pos += 1
			i += 1
		with open(vcf_file, 'a') as f:
			f.writelines(chrom + '\t' + str(pos - offset) + '\t' + '.' + '\t' + REF + '\t' + ALT + '\t'
					'.' + '\t' + 'PASS' + '\t' + '.' + '\t' + 'GT' + '\t' +
					'1/1' + '\n')
			REF = ''
			ALT = ''

