####################################################
########### Author: Georgios Friligkos #############
####################################################

#proceedings

import html

import os
os.system('cls')
import xml.etree.ElementTree as ET
import csv
tree = ET.parse('proceedings.xml')
root = tree.getroot()

# open a file for writing
#proceedings_file = open('proceedings_file.csv', 'w')
with open('proceedings_file.csv', 'w',encoding='utf-8') as proceedings_file:
  # create the csv writer object
  #csvwriter = csv.writer(proceedings_file,delimiter=',',lineterminator='\n',quotechar = "'",quoting=csv.QUOTE_NONNUMERIC)
  csvwriter = csv.writer(proceedings_file,delimiter=',',lineterminator='\n')
  
  for proceedings in root.findall('proceedings'):
    proceedings_file_line = []
    ####################################
    ######       Attributes       ######    
    key = proceedings.get('key')
    proceedings_file_line.append(key)
    mdate = proceedings.get('mdate')
    proceedings_file_line.append(mdate)
    publtype = proceedings.get('publtype')
    proceedings_file_line.append(publtype)
    cdate = proceedings.get('cdate')
    proceedings_file_line.append(cdate)
    ####################################
    #######     Child Elements    ######
    
    ## 1 author - seperate table
    #author = proceedings.find('author')
    #if author is not None:
    #      author = proceedings.find('author').text
    #proceedings_file_line.append(author)		  
    ## 2 editor - seperate table
    #editor = proceedings.find('editor')
    #if editor is not None:
    #      editor = proceedings.find('editor').text
    #proceedings_file_line.append(editor) 
    ## 3 title
    title = proceedings.find('title')
    if title is not None:
          title = proceedings.find('title').text
    proceedings_file_line.append(title)        		  
    ## 4 booktitle
    booktitle = proceedings.find('booktitle')
    if booktitle is not None:
          booktitle = proceedings.find('booktitle').text
    proceedings_file_line.append(booktitle)
    ## 5 pages		
    pages = proceedings.find('pages')
    if pages is not None:
          pages = proceedings.find('pages').text
    proceedings_file_line.append(pages)		  
    ## 6 year		
    year = proceedings.find('year')
    if year is not None:
          year = proceedings.find('year').text
    proceedings_file_line.append(year)		  
    # 7 address 
    address = proceedings.find('address')
    if address is not None:
          address = proceedings.find('address').text
    proceedings_file_line.append(address)
    # 8 journal 
    journal = proceedings.find('journal')
    if journal is not None:
          journal = proceedings.find('journal').text
    proceedings_file_line.append(journal)
    # 9 volume
    volume = proceedings.find('volume')
    if volume is not None:
          volume = proceedings.find('volume').text
    proceedings_file_line.append(volume)
    ## 10 number
    number = proceedings.find('number')
    if number is not None:
          number = proceedings.find('number').text
    proceedings_file_line.append(number)
    ## 11 month	- not relevant
    #month = proceedings.find('month')
    #if month is not None:
    #      month = proceedings.find('month').text
    #proceedings_file_line.append(month)
    ## 12 url
    url = proceedings.find('url')
    if url is not None:
          url = proceedings.find('url').text
    proceedings_file_line.append(url)
    ## 13 ee seperate table
    #ee = proceedings.find('ee')
    #if ee is not None:
    #      ee = proceedings.find('ee').text
    #proceedings_file_line.append(ee)
    ## 14 cdrom - not relevant
    #cdrom = proceedings.find('cdrom')
    #if cdrom is not None:
    #      cdrom = proceedings.find('cdrom').text
    #proceedings_file_line.append(cdrom)		  
    ## 15 cite - seperate table
    #cite = proceedings.find('cite')
    #if cite is not None:
    #      cite = proceedings.find('cite').text
    #proceedings_file_line.append(cite)		 
    ## 16 publisher - seperate table
    #publisher = proceedings.find('publisher')
    #if publisher is not None:
    #      publisher = proceedings.find('publisher').text
    #proceedings_file_line.append(publisher)		  
    ## 17 note - seperate table
    #note = proceedings.find('note')
    #if note is not None:
    #      note = proceedings.find('note').text
    #proceedings_file_line.append(note)		  
    ## 18 crossref
    crossref = proceedings.find('crossref')
    if crossref is not None:
          crossref = proceedings.find('crossref').text
    proceedings_file_line.append(crossref)		  
    ## 19 isbn - seperate table
    #isbn = proceedings.find('isbn')
    #if isbn is not None:
    #      isbn = proceedings.find('isbn').text
    #proceedings_file_line.append(isbn)		  
    # 20 series
    series = proceedings.find('series')
    if series is not None:
          series = proceedings.find('series').text
    proceedings_file_line.append(series)		  
    ## 21 school - not relenat
    #school = proceedings.find('school')
    #if school is not None:
    #      school = proceedings.find('school').text
    #proceedings_file_line.append(school)		  
    ## 22 chapter - not relenat
    #chapter = proceedings.find('chapter')
    #if chapter is not None:
    #      chapter = proceedings.find('chapter').text
    #proceedings_file_line.append(chapter)		  
    ## 23 publnr - not relenat
    #publnr = proceedings.find('publnr')
    #if publnr is not None:
    #      publnr = proceedings.find('publnr').text
    #proceedings_file_line.append(publnr)		  
    #########################################################
    print(proceedings_file_line)	
    csvwriter.writerow(proceedings_file_line)
    
  proceedings_file.close()