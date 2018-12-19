from PyPDF3 import PdfFileMerger as merger
import sys

if  len(sys.argv)==1 or sys.argv[1]=='-h':
    print('''args: infile_1 infile_2 .... infile_n outflie
             merges all the infiles and outputs outfile''')
    exit()

m=merger()

for f in sys.argv[1:-1]:
    m.append(f)

m.write(sys.argv[-1])
