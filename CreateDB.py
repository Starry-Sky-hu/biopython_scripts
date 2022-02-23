import sys
import gffutils

gff_file = sys.argv[1]
db_name = sys.argv[2]

db = gffutils.create_db(gff_file, dbfn=db_name, keep_order=True, force=False, sort_attribute_values=True)

