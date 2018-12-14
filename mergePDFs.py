##Converts a list of multi-page TIFF files into folders with single page PDFs. Use "mergePDFs.py" to merge the individual page PDFs into multi page PDFs.
#Created 12/2/2018 on Python 2.7.13

from PyPDF2 import PdfFileMerger
import glob
import re
import os


pdfPath = 'C:\Users\????\wherever_u_put_the_PDF_files_dude/' #THIS SHOULD BE THE SAME AS IN convertTIFFS.py
folders = os.listdir(pdfPath)               #Makes a list of every folder in pdfPath

for folder in folders:
    newDir = pdfPath + folder
    print("\n\n Current Folder: " + str(folder))
    os.chdir(newDir)
    paths = glob.glob('*.pdf')                                                               #use glob to find all files in folder with format _____.pdf. Makes a list.

    ############ SORTING pages(paths) NICELY #########
    def tryint(s):
        try:
            return int(s)
        except:
            return s

    def alphanum_key(s):
        return [tryint(c) for c in re.split('([0-9]+)', s)]

    def sort_nicely(paths):
        paths.sort(key=alphanum_key)

    sort_nicely(paths)                                                                         #paths.sort()
    ######################################

    merger = PdfFileMerger()

    for page in paths:
        merger.append(open(page, 'rb'))

    with open(pdfPath + folder + ".pdf", 'wb') as fout:

        merger.write(fout)

