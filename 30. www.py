####################################################
########### Author: Georgios Friligkos #############
####################################################

#www

import html

import os
os.system('cls')
import xml.etree.ElementTree as ET
import csv
tree = ET.parse('www.xml')
root = tree.getroot()

# open a file for writing
#www_file = open('www_file.csv', 'w')
with open('www_file.csv', 'w',encoding='utf-8') as www_file:
  # create the csv writer object
  #csvwriter = csv.writer(www_file,delimiter=',',lineterminator='\n',quotechar = "'",quoting=csv.QUOTE_NONNUMERIC)
  csvwriter = csv.writer(www_file,delimiter=',',lineterminator='\n')
  
  for www in root.findall('www'):
    www_file_line = []
    ####################################
    ######       Attributes       ######    
    key = www.get('key')
    www_file_line.append(key)
    mdate = www.get('mdate')
    www_file_line.append(mdate)
    publtype = www.get('publtype')
    www_file_line.append(publtype)
    cdate = www.get('cdate')
    www_file_line.append(cdate)
    ####################################
    #######     Child Elements    ######
    
    # 1 author - seperate table
    #author = www.find('author')
    #if author is not None:
    #      author = www.find('author').text
    #www_file_line.append(author)		  
    # 2 editor - not relevant
    #editor = www.find('editor')
    #if editor is not None:
    #      editor = www.find('editor').text
    #www_file_line.append(editor) 
    # 3 title
    title = www.find('title')
    if title is not None:
          title = www.find('title').text
    www_file_line.append(title)        		  
    # 4 booktitle
    booktitle = www.find('booktitle')
    if booktitle is not None:
          booktitle = www.find('booktitle').text
    www_file_line.append(booktitle)
    # 5 pages - not relevant	
    #pages = www.find('pages')
    #if pages is not None:
    #      pages = www.find('pages').text
    #www_file_line.append(pages)		  
    # 6 year		
    year = www.find('year')
    if year is not None:
          year = www.find('year').text
    www_file_line.append(year)		  
    # 7 address - not relevant
    #address = www.find('address')
    #if address is not None:
    #      address = www.find('address').text
    #www_file_line.append(address)
    # 8 journal - not relevant 
    #journal = www.find('journal')
    #if journal is not None:
    #      journal = www.find('journal').text
    #www_file_line.append(journal)
    # 9 volume - not relevant
    #volume = www.find('volume')
    #if volume is not None:
    #      volume = www.find('volume').text
    #www_file_line.append(volume)
    # 10 number - not relevant
    #number = www.find('number')
    #if number is not None:
    #      number = www.find('number').text
    #www_file_line.append(number)
    # 11 month - not relevant
    #month = www.find('month')
    #if month is not None:
    #      month = www.find('month').text
    #www_file_line.append(month)
    # 12 url - seperate table
    #url = www.find('url')
    #if url is not None:
    #      url = www.find('url').text
    #www_file_line.append(url)
    # 13 ee
    ee = www.find('ee')
    if ee is not None:
          ee = www.find('ee').text
    www_file_line.append(ee)
    # 14 cdrom - not relevant
    #cdrom = www.find('cdrom')
    #if cdrom is not None:
    #      cdrom = www.find('cdrom').text
    #www_file_line.append(cdrom)		  
    # 15 cite - seperate table
    #cite = www.find('cite')
    #if cite is not None:
    #      cite = www.find('cite').text
    #www_file_line.append(cite)		 
    # 16 publisher - not relevant
    #publisher = www.find('publisher')
    #if publisher is not None:
    #      publisher = www.find('publisher').text
    #www_file_line.append(publisher)		  
    # 17 note - seperate table
    #note = www.find('note')
    #if note is not None:
    #      note = www.find('note').text
    #www_file_line.append(note)		  
    # 18 crossref
    crossref = www.find('crossref')
    if crossref is not None:
          crossref = www.find('crossref').text
    www_file_line.append(crossref)		  
    # 19 isbn - not relevant
    #isbn = www.find('isbn')
    #if isbn is not None:
    #      isbn = www.find('isbn').text
    #www_file_line.append(isbn)		  
    # 20 series - not relevant
    #series = www.find('series')
    #if series is not None:
    #      series = www.find('series').text
    #www_file_line.append(series)		  
    # 21 school - not relevant
    #school = www.find('school')
    #if school is not None:
    #      school = www.find('school').text
    #www_file_line.append(school)		  
    # 22 chapter
    #chapter = www.find('chapter')
    #if chapter is not None:
    #      chapter = www.find('chapter').text
    #www_file_line.append(chapter)		  
    # 23 publnr - not relevant
    #publnr = www.find('publnr')
    #if publnr is not None:
    #      publnr = www.find('publnr').text
    #www_file_line.append(publnr)		  
    #########################################################
    print(www_file_line)	
    csvwriter.writerow(www_file_line)
    
  www_file.close()