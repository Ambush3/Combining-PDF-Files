import PyPDF2

pdf1 = open('./example1.pdf', 'rb')   #Opens the example1.pdf file
pdf2 = open('./example2.pdf', 'rb')  #Opens the example2.pdf file
pdfr1 = PyPDF2.PdfFileReader(pdf1)  #Accesses the content of example1.pdf
pdfr2 = PyPDF2.PdfFileReader(pdf2)  #Access the content of example2.pdf
pdfw = PyPDF2.PdfFileWriter()  #Creates and instance of PdfFileWriter

for pn in range(pdfr1.numPages):  #Loops through each page of example1.pdf
    po = pdfr1.getpage(pn)  #Gets a specific page within example1.pdf
    pdfw.addPage(po)  #Adds that page to the combined file
for pn in range(pdfr2.numPages):  #Loops through aeach page of example2.pdf
    po = pdfr2.getpage(pn)  #Gets a specific page within example2.pdf
    pdfw.addPage(po)  #Adds that page to the combined file
pdfo = open('./combined.pdf', 'wb')  #Combined file is opened in write mode
pdfw.write(pdfo)  #Combined file is written to disk
pdfo.close()  #Combined file is closed
pdf1.close()  #The file example1.pdf is closed
pdf2.close()  #The file example2.pdf is closed
