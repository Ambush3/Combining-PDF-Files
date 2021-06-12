import os
import sys


from collections import OrderedDict
from PyPDF2 import PdfFileReader


def readFields(obj, t=None, res=None, fo=None):
    fa = {'/FT': 'Field Type', '/Parent': 'Parent', '/T': 'Field Name', '/TU': 'Alternate Field Name', #Defining attrib.
          'TM': 'Mapping Name', '/Ff': 'Field Flags', '/V': 'Value', '/DV': 'Default Value'}
    if res is None:
        res = OrderedDict()
        items = obj.trailer["/Root"] #Check the root of the pdf. Check for form.
        if "/AcroForm" in items:
            t = items["/AcroForm"]
        else:
            return None
    if t is None:
        return res
    obj._checkKids(t, res, fo) #Check child elements of this form
    for attr in t: #Check which are really fields
        obj._buildField(t, res, fo, fa)
        break
    if "/Fields" in t:
        flds = t["/Fields"]
        for f in flds:
            fld = f.getObject()
            obj._buildField(fld, res, fo, fa)
    return res


def get_form_fields(infile):
    infile = PdfFileReader(open(infile, 'rb'))
    fields = readFields(infile)
    return OrderedDict((k, v.get('/V', '')) for k, v in fields.items())


print(get_form_fields('./example1.pdf'))
