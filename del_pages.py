from PyPDF3 import PdfFileWriter, PdfFileReader
import sys

if  len(sys.argv)==1 or sys.argv[1]=='-h':
    print('''args: infile p1 p2 .. pn outfile
             Program outputs outfile with p1, p2, ..., pn removed from infile.''')
    exit()

infile = PdfFileReader(sys.argv[1], 'rb')
outfile = PdfFileWriter()

page_del = list(map(int, sys.argv[2:-1]))
ptr=0
for i in range(infile.getNumPages()):
    if ptr == len(page_del) or i < page_del[ptr]:
        p = infile.getPage(int(i))
        outfile.addPage(p)
    elif i == page_del:
        ptr+=1

with open(sys.argv[-1], 'wb') as f:
    outfile.write(f)
