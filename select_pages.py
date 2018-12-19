from PyPDF3 import PdfFileWriter, PdfFileReader
import sys

if  len(sys.argv)==1 or sys.argv[1]=='-h':
    print('''args: infile p1 p2 .. pn outfile
             Program outputs outfile with just p1, p2, ..., pn from infile.''')
    exit()

infile = PdfFileReader(sys.argv[1], 'rb')
outfile = PdfFileWriter()

for i in sys.argv[2:-1]:
    p = infile.getPage(int(i))
    outfile.addPage(p)

with open(sys.argv[-1], 'wb') as f:
    outfile.write(f)
