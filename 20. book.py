####################################################
########### Author: Georgios Friligkos #############
####################################################

#book

import html

import os
os.system('cls')
import xml.etree.ElementTree as ET
import csv
tree = ET.parse('book.xml')
root = tree.getroot()

# open a file for writing
#book_file = open('book_file.csv', 'w')
with open('book_file.csv', 'w',encoding='utf-8') as book_file:
  # create the csv writer object
  #csvwriter = csv.writer(book_file,delimiter=',',lineterminator='\n',quotechar = "'",quoting=csv.QUOTE_NONNUMERIC)
  csvwriter = csv.writer(book_file,delimiter=',',lineterminator='\n')
  
  for book in root.findall('book'):
    book_file_line = []
    ####################################
    ######       Attributes       ######    
    key = book.get('key')
    book_file_line.append(key)
    mdate = book.get('mdate')
    book_file_line.append(mdate)
    publtype = book.get('publtype')
    book_file_line.append(publtype)
    cdate = book.get('cdate')
    book_file_line.append(cdate)
    ####################################
    #######     Child Elements    ######
    
    # 1 author - seperate table
    #author = book.find('author')
    #if author is not None:
    #      author = book.find('author').text
    #book_file_line.append(author)		  
    # 2 editor - seperate table
    #editor = book.find('editor')
    #if editor is not None:
    #      editor = book.find('editor').text
    #book_file_line.append(editor) 
    # 3 title
    title = book.find('title')
    if title is not None:
          title = book.find('title').text
    book_file_line.append(title)        		  
    # 4 booktitle
    booktitle = book.find('booktitle')
    if booktitle is not None:
          booktitle = book.find('booktitle').text
    book_file_line.append(booktitle)
    # 5 pages		
    pages = book.find('pages')
    if pages is not None:
          pages = book.find('pages').text
    book_file_line.append(pages)		  
    # 6 year		
    year = book.find('year')
    if year is not None:
          year = book.find('year').text
    book_file_line.append(year)		  
    # 7 address - not relevant
    #address = book.find('address')
    #if address is not None:
    #      address = book.find('address').text
    #book_file_line.append(address)
    # 8 journal - not relevant 
    #journal = book.find('journal')
    #if journal is not None:
    #      journal = book.find('journal').text
    #book_file_line.append(journal)
    # 9 volume
    volume = book.find('volume')
    if volume is not None:
          volume = book.find('volume').text
    book_file_line.append(volume)
    # 10 number - not relevant
    #number = book.find('number')
    #if number is not None:
    #      number = book.find('number').text
    #book_file_line.append(number)
    # 11 month
    month = book.find('month')
    if month is not None:
          month = book.find('month').text
    book_file_line.append(month)
    # 12 url
    url = book.find('url')
    if url is not None:
          url = book.find('url').text
    book_file_line.append(url)
    # 13 ee seperate table
    #ee = book.find('ee')
    #if ee is not None:
    #      ee = book.find('ee').text
    #book_file_line.append(ee)
    # 14 cdrom
    cdrom = book.find('cdrom')
    if cdrom is not None:
          cdrom = book.find('cdrom').text
    book_file_line.append(cdrom)		  
    # 15 cite - seperate table
    #cite = book.find('cite')
    #if cite is not None:
    #      cite = book.find('cite').text
    #book_file_line.append(cite)		 
    # 16 publisher - seperate table
    #publisher = book.find('publisher')
    #if publisher is not None:
    #      publisher = book.find('publisher').text
    #book_file_line.append(publisher)		  
    # 17 note
    note = book.find('note')
    if note is not None:
          note = book.find('note').text
    book_file_line.append(note)		  
    # 18 crossref - not relevant
    #crossref = book.find('crossref')
    #if crossref is not None:
    #      crossref = book.find('crossref').text
    #book_file_line.append(crossref)		  
    # 19 isbn - seperate table
    #isbn = book.find('isbn')
    #if isbn is not None:
    #      isbn = book.find('isbn').text
    #book_file_line.append(isbn)		  
    # 20 series
    series = book.find('series')
    if series is not None:
          series = book.find('series').text
    book_file_line.append(series)		  
    # 21 school
    school = book.find('school')
    if school is not None:
          school = book.find('school').text
    book_file_line.append(school)		  
    # 22 chapter - not relenat
    #chapter = book.find('chapter')
    #if chapter is not None:
    #      chapter = book.find('chapter').text
    #book_file_line.append(chapter)		  
    # 23 publnr - not relevant
    #publnr = book.find('publnr')
    #if publnr is not None:
    #      publnr = book.find('publnr').text
    #book_file_line.append(publnr)		  
    #########################################################
    print(book_file_line)	
    csvwriter.writerow(book_file_line)
    
  book_file.close()