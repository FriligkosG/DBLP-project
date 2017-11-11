####################################################
########### Author: Georgios Friligkos #############
####################################################

#inproceedings

import html

import os
os.system('cls')
import xml.etree.ElementTree as ET
import csv
tree = ET.parse('inproceedings.xml')
root = tree.getroot()

# open a file for writing
#inproceedings_file = open('inproceedings_file.csv', 'w')
with open('inproceedings_file.csv', 'w',encoding='utf-8') as inproceedings_file:
  # create the csv writer object
  #csvwriter = csv.writer(inproceedings_file,delimiter=',',lineterminator='\n',quotechar = "'",quoting=csv.QUOTE_NONNUMERIC)
  csvwriter = csv.writer(inproceedings_file,delimiter=',',lineterminator='\n')
  
  for inproceedings in root.findall('inproceedings'):
    inproceedings_file_line = []
    ####################################
    ######       Attributes       ######    
    key = inproceedings.get('key')
    inproceedings_file_line.append(key)
    mdate = inproceedings.get('mdate')
    inproceedings_file_line.append(mdate)
    publtype = inproceedings.get('publtype')
    inproceedings_file_line.append(publtype)
    cdate = inproceedings.get('cdate')
    inproceedings_file_line.append(cdate)
    ####################################
    #######     Child Elements    ######
    
    ## 1 author - seperate table
    #author = inproceedings.find('author')
    #if author is not None:
    #      author = inproceedings.find('author').text
    #inproceedings_file_line.append(author)		  
    ## 2 editor - seperate table
    #editor = inproceedings.find('editor')
    #if editor is not None:
    #      editor = inproceedings.find('editor').text
    #inproceedings_file_line.append(editor) 
    ## 3 title
    title = inproceedings.find('title')
    if title is not None:
          title = inproceedings.find('title').text
    inproceedings_file_line.append(title)        		  
    ## 4 booktitle
    booktitle = inproceedings.find('booktitle')
    if booktitle is not None:
          booktitle = inproceedings.find('booktitle').text
    inproceedings_file_line.append(booktitle)
    ## 5 pages		
    pages = inproceedings.find('pages')
    if pages is not None:
          pages = inproceedings.find('pages').text
    inproceedings_file_line.append(pages)		  
    ## 6 year		
    year = inproceedings.find('year')
    if year is not None:
          year = inproceedings.find('year').text
    inproceedings_file_line.append(year)		  
    ## 7 address - not relevant 
    #address = inproceedings.find('address')
    #if address is not None:
    #      address = inproceedings.find('address').text
    #inproceedings_file_line.append(address)
    ## 8 journal - not relevant
    #journal = inproceedings.find('journal')
    #if journal is not None:
    #      journal = inproceedings.find('journal').text
    #inproceedings_file_line.append(journal)
    ## 9 volume - not relevant
    #volume = inproceedings.find('volume')
    #if volume is not None:
    #      volume = inproceedings.find('volume').text
    #inproceedings_file_line.append(volume)
    ## 10 number
    number = inproceedings.find('number')
    if number is not None:
          number = inproceedings.find('number').text
    inproceedings_file_line.append(number)
    ## 11 month	
    month = inproceedings.find('month')
    if month is not None:
          month = inproceedings.find('month').text
    inproceedings_file_line.append(month)
    ## 12 url
    url = inproceedings.find('url')
    if url is not None:
          url = inproceedings.find('url').text
    inproceedings_file_line.append(url)
    ## 13 ee seperate table
    #ee = inproceedings.find('ee')
    #if ee is not None:
    #      ee = inproceedings.find('ee').text
    #inproceedings_file_line.append(ee)
    ## 14 cdrom - seperate table
    #cdrom = inproceedings.find('cdrom')
    #if cdrom is not None:
    #      cdrom = inproceedings.find('cdrom').text
    #inproceedings_file_line.append(cdrom)		  
    ## 15 cite - seperate table
    #cite = inproceedings.find('cite')
    #if cite is not None:
    #      cite = inproceedings.find('cite').text
    #inproceedings_file_line.append(cite)		 
    ## 16 publisher - not relenat
    #publisher = inproceedings.find('publisher')
    #if publisher is not None:
    #      publisher = inproceedings.find('publisher').text
    #inproceedings_file_line.append(publisher)		  
    ## 17 note
    note = inproceedings.find('note')
    if note is not None:
          note = inproceedings.find('note').text
    inproceedings_file_line.append(note)		  
    ## 18 crossref
    crossref = inproceedings.find('crossref')
    if crossref is not None:
          crossref = inproceedings.find('crossref').text
    inproceedings_file_line.append(crossref)		  
    ## 19 isbn - not relenat
    #isbn = inproceedings.find('isbn')
    #if isbn is not None:
    #      isbn = inproceedings.find('isbn').text
    #inproceedings_file_line.append(isbn)		  
    ## 20 series - not relenat
    #series = inproceedings.find('series')
    #if series is not None:
    #      series = inproceedings.find('series').text
    #inproceedings_file_line.append(series)		  
    ## 21 school - not relenat
    #school = inproceedings.find('school')
    #if school is not None:
    #      school = inproceedings.find('school').text
    #inproceedings_file_line.append(school)		  
    ## 22 chapter - not relenat
    #chapter = inproceedings.find('chapter')
    #if chapter is not None:
    #      chapter = inproceedings.find('chapter').text
    #inproceedings_file_line.append(chapter)		  
    ## 23 publnr - not relenat
    #publnr = inproceedings.find('publnr')
    #if publnr is not None:
    #      publnr = inproceedings.find('publnr').text
    #inproceedings_file_line.append(publnr)		  
    #########################################################
    print(inproceedings_file_line)	
    csvwriter.writerow(inproceedings_file_line)
    
  inproceedings_file.close()