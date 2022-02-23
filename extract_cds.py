import sys
import gffutils

db_name = sys.argv[1]
mRNA_ID = sys.argv[2]
bed_file = sys.argv[3]

db = gffutils.FeatureDB(db_name, keep_order=True)

CDS = list()
mRNA = db[mRNA_ID]
for i in db.children(mRNA, featuretype='CDS', order_by='start'):
	CDS.append(i)
	
with open(bed_file, 'w') as f:
	f.writelines(CDS[0][0] + '\t' + str(CDS[0][3]) + '\t' + str(CDS[-1][4]) + '\t' + mRNA_ID + '\t' + '0' + '\t' + CDS[-1][6] + '\n')


