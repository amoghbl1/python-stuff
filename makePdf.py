#!/usr/bin/python

import pyPdf, sys, os
from PIL import Image, ImageEnhance
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
    sharpener = ImageEnhance.Sharpness(img)
    img = sharpener.enhance(1.5)
    if "RT90" in tempImagePath:
        img = img.rotate(-90)
    elif "LT90" in tempImagePath:
        img = img.rotate(90)
    elif "UT180" in tempImagePath:
        img = img.rotate(180)
    img.save(tempImagePath, "PDF", resolution=100.0)
    inputConvertedImage = PdfFileReader(file(tempImagePath, "rb"))
    output.addPage(inputConvertedImage.getPage(0))
outputStream = file("output.pdf", "wb")
output.write(outputStream)
outputStream.close()
for i in images: #Delete all the temporary pdf files created
    os.remove(path+i+".temp")
