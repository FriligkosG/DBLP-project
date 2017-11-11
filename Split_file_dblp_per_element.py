#############################################################################
#####################            article                 ####################
#############################################################################

import os
os.system('cls')

#count the #article: 1.677.951
count = 0
import xml.etree.ElementTree as ET
context = ET.iterparse('dblp.xml', events=("start",))

with open('article.xml', 'wb') as f:
  print('I begin....')
  for event, elem in context:
    if elem.tag == 'article':
    #title = elem.find('title').text
    #filename = format(title + ".xml")
      #f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
      count += 1	  
      f.write(ET.tostring(elem))
  print(count)	  
  print('Just Finished, I am exhausted!!!')
	  
#############################################################################
###################          inproceedings                 ##################
#############################################################################
	  
import xml.etree.ElementTree as ET
context = ET.iterparse('dblp.xml', events=("start",))

#count the #inproceedings: 2.020.159
count = 0
with open('inproceedings.xml', 'wb') as f:
  print('I begin....')
  for event, elem in context:
    if elem.tag == 'inproceedings':
    #title = elem.find('title').text
    #filename = format(title + ".xml")
      #f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
      count += 1	  
      f.write(ET.tostring(elem))
  print(count)	  
  print('Just Finished, I am exhausted!!!')
	  
#############################################################################
###################          proceedings                   ##################
#############################################################################	  

import xml.etree.ElementTree as ET
context = ET.iterparse('dblp.xml', events=("start",))

#count the #proceedings: 34.326
count = 0
with open('proceedings.xml', 'wb') as f:
  print('I begin....')
  for event, elem in context:
    if elem.tag == 'proceedings':
    #title = elem.find('title').text
    #filename = format(title + ".xml")
      #f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
      count += 1
      f.write(ET.tostring(elem))
  print('Number of proceedings {}'.format(count))
  print('Just Finished, I am exhausted!!!')

#############################################################################
###################               book                     ##################
#############################################################################

import xml.etree.ElementTree as ET
context = ET.iterparse('dblp.xml', events=("start",))

#count the #book: 13.719
count = 0
with open('book.xml', 'wb') as f:
  print('I begin....')
  for event, elem in context:
    if elem.tag == 'book':
    #title = elem.find('title').text
    #filename = format(title + ".xml")
      #f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
      count += 1	  
      f.write(ET.tostring(elem))
  print('Number of book {}'.format(count))
  print('Just Finished, I am exhausted!!!')
  

#############################################################################
###################           incollection                 ##################
#############################################################################

import xml.etree.ElementTree as ET
context = ET.iterparse('dblp.xml', events=("start",))

#count the #incollection: 45.326
count = 0
with open('incollection.xml', 'wb') as f:
  print('I begin....')
  for event, elem in context:
    if elem.tag == 'incollection':
    #title = elem.find('title').text
    #filename = format(title + ".xml")
      #f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
      count += 1
      f.write(ET.tostring(elem))
  print('Number of incollection {}'.format(count))
  print('Just Finished, I am exhausted!!!')
  
#############################################################################
###################           phdthesis                    ##################
#############################################################################

import xml.etree.ElementTree as ET
context = ET.iterparse('dblp.xml', events=("start",))

#count the #phdthesis: 59.353
count = 0
with open('phdthesis.xml', 'wb') as f:
  print('I begin....')
  for event, elem in context:
    if elem.tag == 'phdthesis':
    #title = elem.find('title').text
    #filename = format(title + ".xml")
      #f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
      count += 1
      f.write(ET.tostring(elem))
  print('Number of phdthesis {}'.format(count))
  print('Just Finished, I am exhausted!!!')
  
#############################################################################
###################           mastersthesis                ##################
#############################################################################

import xml.etree.ElementTree as ET
context = ET.iterparse('dblp.xml', events=("start",))

#count the #mastersthesis: 10
count = 0
with open('mastersthesis.xml', 'wb') as f:
  print('I begin....')
  for event, elem in context:
    if elem.tag == 'mastersthesis':
    #title = elem.find('title').text
    #filename = format(title + ".xml")
      #f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
      count += 1
      f.write(ET.tostring(elem))
  print('Number of mastersthesis {}'.format(count))
  print('Just Finished, I am exhausted!!!')
  
#############################################################################
###################           www                          ##################
#############################################################################

import xml.etree.ElementTree as ET
context = ET.iterparse('dblp.xml', events=("start",))

#count the #www: 1.943.685
count = 0
with open('www.xml', 'wb') as f:
  print('I begin....')
  for event, elem in context:
    if elem.tag == 'www':
    #title = elem.find('title').text
    #filename = format(title + ".xml")
      #f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
      count += 1
      f.write(ET.tostring(elem))
  print('Number of www {}'.format(count))
  print('Just Finished, I am exhausted!!!')
  
#############################################################################
###################           person                       ##################
#############################################################################

import xml.etree.ElementTree as ET
context = ET.iterparse('dblp.xml', events=("start",))

#count the #person: 0
count = 0
with open('person.xml', 'wb') as f:
  print('I begin....')
  for event, elem in context:
    if elem.tag == 'person':
    #title = elem.find('title').text
    #filename = format(title + ".xml")
      #f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
      count += 1
      f.write(ET.tostring(elem))
  print('Number of person {}'.format(count))
  print('Just Finished, I am exhausted!!!')
  
#############################################################################
###################           data                       ##################
#############################################################################

import xml.etree.ElementTree as ET
context = ET.iterparse('dblp.xml', events=("start",))

#count the #data: 0
count = 0
with open('data.xml', 'wb') as f:
  print('I begin....')
  for event, elem in context:
    if elem.tag == 'data':
    #title = elem.find('title').text
    #filename = format(title + ".xml")
      #f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
      count += 1
      f.write(ET.tostring(elem))
  print('Number of data {}'.format(count))
  print('Just Finished, I am exhausted!!!')
  
#############################################################################
#############################################################################
#############################################################################