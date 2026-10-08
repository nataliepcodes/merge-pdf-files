# A program to merge PDF files

from pypdf import PdfWriter

merger = PdfWriter()

# Input: a list of files, pdf files, located in the root directory
files = ["file-1.pdf", "file-2.pdf", "file-3.pdf", "file-4.pdf"]

for file in files: 
    merger.append(file)

# Output: one file that includes all input files
merger.write("combined-files.pdf")