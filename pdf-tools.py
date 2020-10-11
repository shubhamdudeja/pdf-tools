import sys
try:
	import PyPDF2
	from PyPDF2	import PdfFileMerger
except:
	print("install PyPDF2: pip install PyPDF2")
	sys.exit(0)

def cut():
	try:
		print(len(sys.argv))
		if(len(sys.argv)<4):
			raise ValueError("")
		source = sys.argv[2]
		pages = sys.argv[3:len(sys.argv)-1]
		target = sys.argv[-1]
	except:
		print("Expected 4 or more arguments got less for cut")
		print("python pdf-tools.py cut <source_file_name.pdf> <pg1> <pg6> ... <pg4> <new_file_name>\n")
		sys.exit(0)
	try:
		pdf = PyPDF2.PdfFileReader(open( source , 'rb'))
	except:
		print("Source file not found!")
		sys.exit(0)

	out = PyPDF2.PdfFileWriter()

	for page in pages:
		try:
			out.addPage(pdf.getPage(int(page)-1))
		except:
			print("Invalid page skipping! page : ",page)
	outputStream = open(target, "wb")
	out.write(outputStream)
	outputStream.close()
	print("New pdf saved!",target+".pdf")

def merge():
	try:
		files = sys.argv[2:len(sys.argv)-1]
		target = sys.argv[-1]
		if(len(files)<1):
			raise ValueError('')
	except:
		print("\nExpected 2 or more arguments got less for merge")
		print("python pdf-tools.py merge <file_name1.pdf> <file_name2.pdf> ... <file_nameX.pdf> <new_file_name>\n")
		sys.exit(0)
	try:
		out = PyPDF2.PdfFileWriter()
		for file in files:
			pdf = PyPDF2.PdfFileReader(open( file, 'rb'))
			doc_length = pdf.getNumPages()
			for page in range(doc_length):
				try:
					out.addPage(pdf.getPage(page))
				except:
					print("Invalid page skipping! page : ",page)
		outputStream = open(target, "wb")
		out.write(outputStream)
		outputStream.close()
		print("New pdf saved!",target+".pdf")
	except:
		print("Source file not found!", file)
		sys.exit(0)

def main():
	try:
		if len(sys.argv)<1:
			raise ValueError('')
		function = sys.argv[1] 
	except:
		print("\nList of valid Commands:")
		print("1) python pdf-tools.py cut <source_file_name.pdf> <pg 1> <pg6> ... <pg4> <new_file_name>")
		print("2) python pdf-tools.py merge <file_name1.pdf> <file_name2.pdf> ... <file_nameX.pdf> <new_file_name>\n")
		sys.exit(0)
	if(function == 'cut'):
		cut()
	elif(function == 'merge'):
		merge()
	
main()

# a python script written by Shubham Dudeja
# References: PyPDF2 documentation