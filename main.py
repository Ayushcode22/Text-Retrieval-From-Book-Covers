# extract text from all the images in a folder
# storing the text in a single file
from PIL import Image
import pytesseract as pt
from pytesseract import Output
import os
import spacy
import xlsxwriter
import cv2
import re
import sys


def excell_writer(title,author,publisher,ISBN,row,worksheet):
    
    column=0
    for i in range(0,4):
        if(column ==0):
            worksheet.write(row,column,title)
        elif(column == 1):
            worksheet.write(row,column,author)
        elif(column == 2):
            worksheet.write(row,column,ISBN)
        elif(column == 3):
            worksheet.write(row,column,publisher)
        column +=1
    

def getAuthor(str):
    nlp = spacy.load('en_core_web_lg')
    doc = nlp(str)
    author=""
    for ent in doc.ents:
        if(ent.label_=="PERSON"):
            author += ent.text+"\t"       #Author
            print(author,"author")
            break
    return author


def getTitle(data):
    n_boxes = len(data['level'])
    max_height=0
    block_num=0
    str=""
    for i in range(0,n_boxes):
        if(data['height'][i]>max_height and data['text'][i]!=""):
            block_num=data['block_num'][i]
            max_height=data['height'][i]
    for i in range(n_boxes):
        if(max_height/data["height"][i]<1.2 and data["text"][i]!=""):
            str+=" "+data["text"][i]
    print(str,"TITLE")
    return str

def getPublisher(string):
    nlp = spacy.load('en_core_web_lg')
    doc = nlp(string)
    publisher=""
    for ent in doc.ents:
        if(ent.label_=="ORG"):
            publisher = ent.text       #Publisher
            print(publisher,"publisher")
    return publisher

def getISBN(string):
    ISBN=""
    result=string.split("\n")
    # print(result)
    for i in result:
        if(i.find("ISBN")!=-1):
            ISBN+=i+"\t"
    print(ISBN)
    return ISBN


def main(path):
    pt.pytesseract.tesseract_cmd = 'C:\\Users\\HP\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
    row =0
    workbook = xlsxwriter.Workbook('hello.xlsx')
    worksheet = workbook.add_worksheet()
    for imageName in os.listdir(path):
        print(imageName)
        inputPath = os.path.join(path, imageName)
        img = Image.open(inputPath)
        
        string = pt.image_to_string(img, lang ="eng",config='psm 1')
        data = pt.image_to_data(img, lang ="eng",output_type=Output.DICT)

        author = getAuthor(string)

        s= getTitle(data)

        publisher = getPublisher(string)

        ISBN = getISBN(string)
        
        excell_writer(s,author,publisher,ISBN,row,worksheet)
        row+=1
    workbook.close()
    return s	


if __name__ == '__main__':
    main(sys.argv[1])
