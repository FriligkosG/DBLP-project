####################################################
########### Author: Georgios Friligkos #############
####################################################

import html

import os
os.system('cls')
import xml.etree.ElementTree as ET
import csv
tree = ET.parse('book.xml')
root = tree.getroot()

# open a file for writing
#book_file = open('book_cite_file.csv', 'w')
with open('book_cite_file.csv', 'w',encoding='utf-8') as book_file:
  # create the csv writer object
  #csvwriter = csv.writer(book_file,delimiter=',',lineterminator='\n',quotechar = "'",quoting=csv.QUOTE_NONNUMERIC)
  csvwriter = csv.writer(book_file,delimiter=',',lineterminator='\n')
  
  for book in root.iter('book'):
    book_file_line = []
    key = book.get('key')
    book_file_line.append(key)
    for node in book.getiterator():
      if node.tag=='cite':
        book_file_line.append(node.text)
        label = node.get('label')
        book_file_line.append(label)
        ref = node.get('ref')
        book_file_line.append(ref)
        print(book_file_line)
        csvwriter.writerow(book_file_line)
        book_file_line = []
        book_file_line.append(key)
		
book_file.close()