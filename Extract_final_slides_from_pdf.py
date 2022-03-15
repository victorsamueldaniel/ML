#%%
from doctest import OutputChecker
import os
os.system("pdfgrep \"Slide 53\" --page-number  02_What_is_ML.pdf")

# %%
import subprocess
subprocess.Popen('wsl.exe',shell=True)
print(subprocess.check_output("pdfgrep \"Slide 5\" --page-number  02_What_is_ML.pdf",shell=True))
# %%
import subprocess
filtered = ['[A-Z].+Jane'] # the list of regexes is shortened to one string, to keep the example simple.
for regex in filtered: 
    arg = ['pdfgrep',  '-PrH',  f"{regex}"]
    process_match = subprocess.run(arg, stdout=subprocess.PIPE, shell=True)
# %%
import PyPDF2 as PDF #import pdf module 
import re

p = PDF.PdfFileReader("02_What_is_ML.pdf")

# get number of pages
NumPages = p.getNumPages()

#define keyterms; David, Final, End, Score, Birthday, Hello Ben

kTerm = "Slide 2"

#extract text and do the search
for i in range(0, NumPages):
    PageObj = p.getPage(i)
    print("Looking through page " + str(i))
    Text = PageObj.extractText()
    Result = re.search(kTerm,Text)

    if Result:
         print(f"{kTerm} found")
    else:
         print("0")
# %%
from PyPDF2 import PdfFileReader,PdfFileWriter
import tkinter.filedialog
import tkinter as tk
import os
import re

####choosing pdf file
root = tk.Tk()
root.withdraw() #use to hide tkinter window

currdir = os.getcwd()
pdf_dir_and_name = tk.filedialog.askopenfilename(parent=root, initialdir=currdir, title='Please select a directory')
if len(pdf_dir_and_name) > 0:
    print ("You chose %s" % pdf_dir_and_name)

####creating list with finished slides
# open the PDF file
pdfFile = open(pdf_dir_and_name, 'rb')
pdf_dir=re.findall(r"(.+\/)([^\/]+.pdf)",pdf_dir_and_name)[0][0]
pdf_name=re.findall(r"(.+\/)([^\/]+.pdf)",pdf_dir_and_name)[0][1]
# create PDFFileReader object to read the file
pdfReader = PdfFileReader(pdfFile)


numOfPages = pdfReader.getNumPages()
L=[0]*numOfPages
for n in range(1,numOfPages):
    for i in range(n, numOfPages):
        pageObj = pdfReader.getPage(i)
        my_str=pageObj.extractText()
        if "Slide" + str(n) in my_str:
            L[n-1]=i
L=[k for k in L if k!=0]
L.insert(0, 0)
#####creating pdf with extracted pages
pdf_writer = PdfFileWriter()
for page in range(len(L)):
    pdf_writer.addPage(pdfReader.getPage(L[page]))
output_filename = pdf_dir + 'extracted_' + pdf_name
with open(output_filename,'wb') as out:
    pdf_writer.write(out)


# close the PDF file object
pdfFile.close()
# %%
