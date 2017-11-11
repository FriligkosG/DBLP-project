####################################################
########### Author: Georgios Friligkos #############
####################################################

#incollection

import html

import os
os.system('cls')
import xml.etree.ElementTree as ET
import csv
tree = ET.parse('incollection.xml')
root = tree.getroot()

# open a file for writing
#incollection_file = open('incollection_file.csv', 'w')
with open('incollection_file.csv', 'w',encoding='utf-8') as incollection_file:
  # create the csv writer object
  #csvwriter = csv.writer(incollection_file,delimiter=',',lineterminator='\n',quotechar = "'",quoting=csv.QUOTE_NONNUMERIC)
  csvwriter = csv.writer(incollection_file,delimiter=',',lineterminator='\n')
  
  for incollection in root.findall('incollection'):
    incollection_file_line = []
    ####################################
    ######       Attributes       ######    
    key = incollection.get('key')
    incollection_file_line.append(key)
    mdate = incollection.get('mdate')
    incollection_file_line.append(mdate)
    publtype = incollection.get('publtype')
    incollection_file_line.append(publtype)
    cdate = incollection.get('cdate')
    incollection_file_line.append(cdate)
    ####################################
    #######     Child Elements    ######
    
    # 1 author - seperate table
    #author = incollection.find('author')
    #if author is not None:
    #      author = incollection.find('author').text
    #incollection_file_line.append(author)		  
    # 2 editor - not relevant
    #editor = incollection.find('editor')
    #if editor is not None:
    #      editor = incollection.find('editor').text
    #incollection_file_line.append(editor) 
    # 3 title
    title = incollection.find('title')
    if title is not None:
          title = incollection.find('title').text
    incollection_file_line.append(title)        		  
    # 4 booktitle
    booktitle = incollection.find('booktitle')
    if booktitle is not None:
          booktitle = incollection.find('booktitle').text
    incollection_file_line.append(booktitle)
    # 5 pages		
    pages = incollection.find('pages')
    if pages is not None:
          pages = incollection.find('pages').text
    incollection_file_line.append(pages)		  
    # 6 year		
    year = incollection.find('year')
    if year is not None:
          year = incollection.find('year').text
    incollection_file_line.append(year)		  
    # 7 address - not relevant
    #address = incollection.find('address')
    #if address is not None:
    #      address = incollection.find('address').text
    #incollection_file_line.append(address)
    # 8 journal - not relevant 
    #journal = incollection.find('journal')
    #if journal is not None:
    #      journal = incollection.find('journal').text
    #incollection_file_line.append(journal)
    # 9 volume - not relevant
    #volume = incollection.find('volume')
    #if volume is not None:
    #      volume = incollection.find('volume').text
    #incollection_file_line.append(volume)
    # 10 number
    number = incollection.find('number')
    if number is not None:
          number = incollection.find('number').text
    incollection_file_line.append(number)
    # 11 month - not relevant
    #month = incollection.find('month')
    #if month is not None:
    #      month = incollection.find('month').text
    #incollection_file_line.append(month)
    # 12 url
    url = incollection.find('url')
    if url is not None:
          url = incollection.find('url').text
    incollection_file_line.append(url)
    # 13 ee
    ee = incollection.find('ee')
    if ee is not None:
          ee = incollection.find('ee').text
    incollection_file_line.append(ee)
    # 14 cdrom
    cdrom = incollection.find('cdrom')
    if cdrom is not None:
          cdrom = incollection.find('cdrom').text
    incollection_file_line.append(cdrom)		  
    # 15 cite - seperate table
    #cite = incollection.find('cite')
    #if cite is not None:
    #      cite = incollection.find('cite').text
    #incollection_file_line.append(cite)		 
    # 16 publisher
    publisher = incollection.find('publisher')
    if publisher is not None:
          publisher = incollection.find('publisher').text
    incollection_file_line.append(publisher)		  
    # 17 note
    note = incollection.find('note')
    if note is not None:
          note = incollection.find('note').text
    incollection_file_line.append(note)		  
    # 18 crossref
    crossref = incollection.find('crossref')
    if crossref is not None:
          crossref = incollection.find('crossref').text
    incollection_file_line.append(crossref)		  
    # 19 isbn - not relevant
    #isbn = incollection.find('isbn')
    #if isbn is not None:
    #      isbn = incollection.find('isbn').text
    #incollection_file_line.append(isbn)		  
    # 20 series - not relevant
    #series = incollection.find('series')
    #if series is not None:
    #      series = incollection.find('series').text
    #incollection_file_line.append(series)		  
    # 21 school - not relevant
    #school = incollection.find('school')
    #if school is not None:
    #      school = incollection.find('school').text
    #incollection_file_line.append(school)		  
    # 22 chapter
    chapter = incollection.find('chapter')
    if chapter is not None:
          chapter = incollection.find('chapter').text
    incollection_file_line.append(chapter)		  
    # 23 publnr - not relenat
    #publnr = incollection.find('publnr')
    #if publnr is not None:
    #      publnr = incollection.find('publnr').text
    #incollection_file_line.append(publnr)		  
    #########################################################
    print(incollection_file_line)	
    csvwriter.writerow(incollection_file_line)
    
  incollection_file.close()