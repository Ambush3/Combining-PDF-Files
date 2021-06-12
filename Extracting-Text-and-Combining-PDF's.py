import PyPDF2


def get_text(fname):
    f = open(fname, 'rb')
    pdfr = PyPDF2.PdfFileReader(f)
    pdfr.numPages
    page = pdfr.getPage(0)
    txt = page.extractText()
    f.close()
    return txt


def combine_files(f1, f2, rf):
    pdf1 = open(f1, 'rb')
    pdf2 = open(f2, 'rb')

    pdfr1 = PyPDF2.PdfFileReader(pdf1)
    pdfr2 = PyPDF2.PdfFileReader(pdf2)
    pdfw = PyPDF2.PdfFileWriter()

    for pn in range(pdfr1.numPages):
        po = pdfr1.getPage(pn)
        pdfw.addPage(po)
    for pn in range(pdfr2.numPages):
        po = pdfr2.getPage(pn)
        pdfw.addPage(po)

    pdfo = open(rf, 'wb')
    pdfw.write(pdfo)
    pdfo.close()
    pdf1.close()
    pdf2.close()


f = './combined.pdf'
combine_files('./example1.pdf', '.example2.pdf', f)
print(get_text(f))
