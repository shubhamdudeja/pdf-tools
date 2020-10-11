# pdf-tools
pdf-tools is a feature-rich lightweight python script that enables you to extract specific pages of your choice, reorder, merge, split a pdf file.
## Features
* Extract specific pages
* Reorder pages of a PDF file.
* Merge multiple PDF files
## Requirements
* PyPDF2 
~~~
pip install PyPDF2
~~~
In order to use the python script you need to have PyPDF2 installed and that's it.

## How to use

* #### Extract Specific pages
~~~
python pdf-tools.py cut source.pdf 1 3 newfile
~~~
This command, <b> (cut), </b> creates a new pdf (newfile.pdf) which contains only page 1 and page 3 from the source file (source.pdf).
* #### Reorder pages
~~~
python pdf-tools.py cut source.pdf 2 3 1 4 newfile
~~~
This command, <b> (cut), </b> creates a new pdf (nwefile.pdf) which contains pages in the order (2, 3, 1, 4) from the source file(source.pdf).
* #### Merge PDFs
~~~
python pdf-tools.py merge file1.pdf file2.pdf ... fileX.pdf newfile
~~~
This command, <b> (merge), </b> creates a new pdf (newfile.pdf) which is the merged pdf of all the files: file1.pdf file2.pdf ... fileX.pdf (appended one after the other).
<br>
<br>
* Upcoming features
    * Remove specific pages from a pdf
    * encrypt a pdf file
<br>
<br>
:heart:
