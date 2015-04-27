#!/usr/bin/python

import pyPdf, sys, os
from PIL import Image
from pyPdf import PdfFileWriter, PdfFileReader
if len(sys.argv) == 1:
    print "USAGE: makePdf folder_name"
    sys.exit(2)
path = sys.argv[1]+"/"
output = PdfFileWriter()
images = os.listdir(path)
images.sort()
for i in images: # Create temporary images and save them as pdfs
    imagePath = path+i
    print imagePath
    tempImagePath = imagePath+".temp"
    img = Image.open(imagePath)
    img.save(tempImagePath, "PDF", resolution=100.0)
    inputConvertedImage = PdfFileReader(file(tempImagePath, "rb"))
    output.addPage(inputConvertedImage.getPage(0))
outputStream = file("output.pdf", "wb")
output.write(outputStream)
outputStream.close()
for i in images: #Delete all the temporary pdf files created
    os.remove(path+i+".temp")
