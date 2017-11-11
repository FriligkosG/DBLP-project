####################################################
########### Author: Georgios Friligkos #############
####################################################

import html

import os
os.system('cls')
import xml.etree.ElementTree as ET
import csv
tree = ET.parse('incollection.xml')
root = tree.getroot()

# open a file for writing
#incollection_file = open('incollection_cite_file.csv', 'w')
with open('incollection_cite_file.csv', 'w',encoding='utf-8') as incollection_file:
  # create the csv writer object
  #csvwriter = csv.writer(incollection_file,delimiter=',',lineterminator='\n',quotechar = "'",quoting=csv.QUOTE_NONNUMERIC)
  csvwriter = csv.writer(incollection_file,delimiter=',',lineterminator='\n')
  
  for incollection in root.iter('incollection'):
    incollection_file_line = []
    key = incollection.get('key')
    incollection_file_line.append(key)
    for node in incollection.getiterator():
      if node.tag=='cite':
        incollection_file_line.append(node.text)
        label = node.get('label')
        incollection_file_line.append(label)
        ref = node.get('ref')
        incollection_file_line.append(ref)
        print(incollection_file_line)
        csvwriter.writerow(incollection_file_line)
        incollection_file_line = []
        incollection_file_line.append(key)
		
incollection_file.close()