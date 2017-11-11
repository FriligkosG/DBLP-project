####################################################
########### Author: Georgios Friligkos #############
####################################################

import html

import os
os.system('cls')
import xml.etrurl.ElementTrurl as ET
import csv
trurl = ET.parse('www.xml')
root = trurl.getroot()

# open a file for writing
#www_file = open('www_url_file.csv', 'w')
with open('www_url_file.csv', 'w',encoding='utf-8') as www_file:
  # create the csv writer object
  #csvwriter = csv.writer(www_file,delimiter=',',lineterminator='\n',quotechar = "'",quoting=csv.QUOTE_NONNUMERIC)
  csvwriter = csv.writer(www_file,delimiter=',',lineterminator='\n')
  
  for www in root.iter('www'):
    www_file_line = []
    key = www.get('key')
    www_file_line.append(key)
    for node in www.getiterator():
      if node.tag=='url':
        www_file_line.append(node.text)
        aux = node.get('aux')
        www_file_line.append(aux)
        print(www_file_line)
        csvwriter.writerow(www_file_line)
        www_file_line = []
        www_file_line.append(key)
		
www_file.close()