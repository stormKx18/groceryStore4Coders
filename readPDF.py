#python code to read pdf files
import PyPDF2

pdfFileObj = open('Web_Scraping.pdf', 'rb') #Read a specific pdf file
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print(pdfReader.numPages) #Print number of pages

pageObj = pdfReader.getPage(118) #Read specific page
print(pageObj.extractText()) #Extract the text
