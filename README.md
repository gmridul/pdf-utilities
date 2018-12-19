# pdf-utilities
Merge, add or remove pages from PDF files

## Merge PDF file
python merge.py infile\_1 infile\_2 ... infile\_n outfile

Merges all the infiles to outfile

## Create a new PDF file by deleteing pages from a PDF file
python del\_pages.py infile p1 p2 ... pn outfile

Outputs outfile by deleting p1, p2, ..., pn from infile 

## Create a new PDF file from selected pages of a PDF file
python select\_pages.py infile p1 p2 ... pn outfile

Outputs outfile using p1, p2, ..., pn pages in outfile
