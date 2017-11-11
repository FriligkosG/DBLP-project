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
#proceedings_file = open('proceedings_editor_file.csv', 'w')
with open('proceedings_editor_file.csv', 'w',encoding='utf-8') as proceedings_file:
  # create the csv writer object
  #csvwriter = csv.writer(proceedings_file,delimiter=',',lineterminator='\n',quotechar = "'",quoting=csv.QUOTE_NONNUMERIC)
  csvwriter = csv.writer(proceedings_file,delimiter=',',lineterminator='\n')
  
  for proceedings in root.iter('proceedings'):
    proceedings_file_line = []
    key = proceedings.get('key')
    proceedings_file_line.append(key)
    for node in proceedings.getiterator():
      if node.tag=='editor':
        proceedings_file_line.append(node.text)
        aux = node.get('aux')
        proceedings_file_line.append(aux)
        orcid = node.get('orcid')
        proceedings_file_line.append(orcid)
        print(proceedings_file_line)
        csvwriter.writerow(proceedings_file_line)
        proceedings_file_line = []
        proceedings_file_line.append(key)
		
proceedings_file.close()