####################################################
########### Author: Georgios Friligkos #############
####################################################

import html

import os
os.system('cls')
import xml.etree.ElementTree as ET
import csv
tree = ET.parse('article.xml')
root = tree.getroot()

# open a file for writing
#article_file = open('article_cite_file.csv', 'w')
with open('article_cite_file.csv', 'w',encoding='utf-8') as article_file:
  # create the csv writer object
  #csvwriter = csv.writer(article_file,delimiter=',',lineterminator='\n',quotechar = "'",quoting=csv.QUOTE_NONNUMERIC)
  csvwriter = csv.writer(article_file,delimiter=',',lineterminator='\n')
  
  for article in root.iter('article'):
    article_file_line = []
    key = article.get('key')
    article_file_line.append(key)
    for node in article.getiterator():
      if node.tag=='cite':
        article_file_line.append(node.text)
        label = node.get('label')
        article_file_line.append(label)
        ref = node.get('ref')
        article_file_line.append(ref)
        print(article_file_line)
        csvwriter.writerow(article_file_line)
        article_file_line = []
        article_file_line.append(key)
		
article_file.close()