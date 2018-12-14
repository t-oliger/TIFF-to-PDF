##Converts a list of multi-page TIFF files into folders with single page PDFs. Use "mergePDFs.py" to merge the individual page PDFs into multi page PDFs.
#Created 12/2/2018 on Python 2.7.13

from PIL import Image
import os
from PyPDF2 import PdfFileReader, PdfFileMerger
import glob
import sys

i = 0 #page number
j = 0 #tiff number
k = 0 #count number (for percentge complete)

tiffPath = 'C:\Users\????\wherever_u_put_the_TIFFS_dude/'
pdfPath = 'C:\Users\????\wherever_u_want_the_PDF_files_dude/'
merger = PdfFileMerger()

os.chdir(tiffPath)                                          #Changes working directory to where-ever the .tif files are

tiffs = glob.glob('*.tif')                                  #Gathers all of the .tif files from working directory
strippedTiffs = [s.strip('.tif') for s in tiffs]            #takes the .tif off the files (for easy naming)

for j in strippedTiffs:                                     #for each file (j) in the list of .tif files....
    k += 1  #this is just for the percentage of files complete
    try:
        print('Now Converting FileName (j): ' + j)
        #printing a percent complete, for convenience.
        print("\n\nFile # (k):  " + str(k) + " out of " + str(len(strippedTiffs)) + " , Percentage Complete: " + str(round(float(k)/float(len(strippedTiffs))*float(100), 2)) + "%")
        os.makedirs(pdfPath + j)
        i = 0                                               #Starts back at the original page

        while True:
            try:

                img = Image.open(tiffPath + j + ".tif")     #opens the tif
                img.seek(i)
                image = img.convert("RGB")                  #converts .tif to an image format that PDFs use
            except EOFError:                                #Once you get to the end of the page
                break
            i += 1                                          #We start at i=0 because programmers hate humanity and like to count starting from 0. Thus, we gotta add 1 to the page number for the file name to make sense.
            image.save(pdfPath + j + '/' + '00' + str(i)+'.pdf') #save this converted page to the PDF directory
            sys.stdout.write('\r' + "Currently on Page:  " + str(i))


    #~If an error is encountered, it will list it and continue with the process~#
    except Exception as e:
        print("THERE WAS AN ERROR HERE. K = " + str(k) + "\nI = " + str(i) + "\nj = " + j)
        print e
        pass

