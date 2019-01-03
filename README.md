# pdf-utilities
Merge, add or remove pages from PDF files

## Merge PDF file
```python merge.py infile_1 infile_2 ... infile_n outfile```

Merges all the infiles to outfile

## Create a new PDF file by deleteing pages from a PDF file
```python del_pages.py infile p1 p2 ... pn outfile```

Outputs outfile by deleting p1, p2, ..., pn from infile 

## Create a new PDF file from selected pages of a PDF file
```python select_pages.py infile p1 p2 ... pn outfile```

Outputs outfile using p1, p2, ..., pn pages in outfile
