import sys

vcf_list_file = sys.argv[1]
merge_vcf_file = sys.argv[2]
query_name = sys.argv[3]

with open(vcf_list_file, 'r') as f:
	vcf_list = f.readlines()
with open(merge_vcf_file, 'a') as f:
	f.writelines("##fileformat=VCFv4.2\n")
	f.writelines('#CHROM' + '\t' + 'POS' + '\t' + 'ID' + '\t' + 'REF' + '\t' + 'ALT' + '\t' +
			'QUAL' + '\t' + 'FILTER' + '\t' + "INFO" + '\t' + 'FORMAT' + '\t' +
			query_name + '\n')
	
variant_dict = dict() # record variant position
for i in range(len(vcf_list)):
	with open(vcf_list[i].strip(), 'r') as f:
		vcf = f.readlines()
	for j in range(len(vcf)):
		if ("#" != vcf[j][0]):
			chrom_pos = vcf[j].split('.')[0]
			var = vcf[j].split('.')[1]
			var_ref = vcf[j].split('.')[1].split()[0]
			var_query = vcf[j].split('.')[1].split()[1]
			if (chrom_pos not in variant_dict.keys()) :
				variant_dict[chrom_pos] = var
				with open(merge_vcf_file, 'a') as f:
					f.writelines(vcf[j])
			elif (var_ref !=  variant_dict[chrom_pos].split()[0]) or ((var_ref ==  variant_dict[chrom_pos].split()[0]) and ( len(var_query) !=  len(variant_dict[chrom_pos].split()[1]) )):
				with open(merge_vcf_file, 'a') as f:
					f.writelines(vcf[j])


