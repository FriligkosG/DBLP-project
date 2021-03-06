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
#book_file = open('book_ee_file.csv', 'w')
with open('book_ee_file.csv', 'w',encoding='utf-8') as book_file:
  # create the csv writer object
  #csvwriter = csv.writer(book_file,delimiter=',',lineterminator='\n',quotechar = "'",quoting=csv.QUOTE_NONNUMERIC)
  csvwriter = csv.writer(book_file,delimiter=',',lineterminator='\n')
  
  for book in root.iter('book'):
    book_file_line = []
    key = book.get('key')
    book_file_line.append(key)
    for node in book.getiterator():
      if node.tag=='ee':
        book_file_line.append(node.text)
        aux = node.get('aux')
        book_file_line.append(aux)
        type = node.get('type')
        book_file_line.append(type)
        print(book_file_line)
        csvwriter.writerow(book_file_line)
        book_file_line = []
        book_file_line.append(key)
		
book_file.close()