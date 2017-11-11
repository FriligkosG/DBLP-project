####################################################
########### Author: Georgios Friligkos #############
####################################################

import html

import os
os.system('cls')
import xml.etree.ElementTree as ET
import csv
tree = ET.parse('inproceedings.xml')
root = tree.getroot()

# open a file for writing
#inproceedings_file = open('inproceedings_ee_file.csv', 'w')
with open('inproceedings_ee_file.csv', 'w',encoding='utf-8') as inproceedings_file:
  # create the csv writer object
  #csvwriter = csv.writer(inproceedings_file,delimiter=',',lineterminator='\n',quotechar = "'",quoting=csv.QUOTE_NONNUMERIC)
  csvwriter = csv.writer(inproceedings_file,delimiter=',',lineterminator='\n')
  
  for inproceedings in root.iter('inproceedings'):
    inproceedings_file_line = []
    key = inproceedings.get('key')
    inproceedings_file_line.append(key)
    for node in inproceedings.getiterator():
      if node.tag=='ee':
        inproceedings_file_line.append(node.text)
        aux = node.get('aux')
        inproceedings_file_line.append(aux)
        type = node.get('type')
        inproceedings_file_line.append(type)
        print(inproceedings_file_line)
        csvwriter.writerow(inproceedings_file_line)
        inproceedings_file_line = []
        inproceedings_file_line.append(key)
		
inproceedings_file.close()