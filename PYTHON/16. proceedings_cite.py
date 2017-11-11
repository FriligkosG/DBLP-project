####################################################
########### Author: Georgios Friligkos #############
####################################################

import html

import os
os.system('cls')
import xml.etree.ElementTree as ET
import csv
tree = ET.parse('proceedings.xml')
root = tree.getroot()

# open a file for writing
#proceedings_file = open('proceedings_cite_file.csv', 'w')
with open('proceedings_cite_file.csv', 'w',encoding='utf-8') as proceedings_file:
  # create the csv writer object
  #csvwriter = csv.writer(proceedings_file,delimiter=',',lineterminator='\n',quotechar = "'",quoting=csv.QUOTE_NONNUMERIC)
  csvwriter = csv.writer(proceedings_file,delimiter=',',lineterminator='\n')
  
  for proceedings in root.iter('proceedings'):
    proceedings_file_line = []
    key = proceedings.get('key')
    proceedings_file_line.append(key)
    for node in proceedings.getiterator():
      if node.tag=='cite':
        proceedings_file_line.append(node.text)
        label = node.get('label')
        proceedings_file_line.append(label)
        ref = node.get('ref')
        proceedings_file_line.append(ref)
        print(proceedings_file_line)
        csvwriter.writerow(proceedings_file_line)
        proceedings_file_line = []
        proceedings_file_line.append(key)
		
proceedings_file.close()