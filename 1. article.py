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
#article_file = open('article_file.csv', 'w')
with open('article_file_v3.csv', 'w',encoding='utf-8') as article_file:
  # create the csv writer object
  #csvwriter = csv.writer(article_file,delimiter=',',lineterminator='\n',quotechar = "'",quoting=csv.QUOTE_NONNUMERIC)
  csvwriter = csv.writer(article_file,delimiter=',',lineterminator='\n')
  
  for article in root.findall('article'):
    article_file_line = []
    ####################################
    ######       Attributes       ######    
    key = article.get('key')
    article_file_line.append(key)
    mdate = article.get('mdate')
    article_file_line.append(mdate)
    publtype = article.get('publtype')
    article_file_line.append(publtype)      	
    reviewid = article.get('reviewid')
    article_file_line.append(reviewid)	
    rating = article.get('rating')
    article_file_line.append(rating)
    cdate = article.get('cdate')
    article_file_line.append(cdate)
    ####################################
    #######     Child Elements    ######
    
    ## 1 author
    #author = article.find('author')
    #if author is not None:
    #      author = article.find('author').text
    #article_file_line.append(author)		  
    ## 2 editor
    #editor = article.find('editor')
    #if editor is not None:
    #      editor = article.find('editor').text
    #article_file_line.append(editor) 
    ## 3 title
    title = article.find('title')
    if title is not None:
          title = article.find('title').text
    article_file_line.append(title)        		  
    ## 4 booktitle
    booktitle = article.find('booktitle')
    if booktitle is not None:
          booktitle = article.find('booktitle').text
    article_file_line.append(booktitle)
    ## 5 pages	
    pages = article.find('pages')
    if pages is not None:
          pages = article.find('pages').text
    article_file_line.append(pages)		  
    ## 6 year		
    year = article.find('year')
    if year is not None:
          year = article.find('year').text
    article_file_line.append(year)		  
    ## 7 address		
    #address = article.find('address')
    #if address is not None:
    #      address = article.find('address').text
    #article_file_line.append(address)
    ## 8 journal
    journal = article.find('journal')
    if journal is not None:
          journal = article.find('journal').text
    article_file_line.append(journal)
    ## 9 volume 		
    volume = article.find('volume')
    if volume is not None:
          volume = article.find('volume').text
    article_file_line.append(volume)
    ## 10 number
    number = article.find('number')
    if number is not None:
          number = article.find('number').text
    article_file_line.append(number)
    ## 11 month	
    month = article.find('month')
    if month is not None:
          month = article.find('month').text
    article_file_line.append(month)
    ## 12 url
    url = article.find('url')
    if url is not None:
          url = article.find('url').text
    article_file_line.append(url)
    ## 13 ee		
    #ee = article.find('ee')
    #if ee is not None:
    #      ee = article.find('ee').text
    #article_file_line.append(ee)
    ## 14 cdrom
    cdrom = article.find('cdrom')
    if cdrom is not None:
          cdrom = article.find('cdrom').text
    article_file_line.append(cdrom)		  
    ## 15 cite
    #cite = article.find('cite')
    #if cite is not None:
    #      cite = article.find('cite').text
    #article_file_line.append(cite)		 
    ## 16 publisher		
    publisher = article.find('publisher')
    if publisher is not None:
          publisher = article.find('publisher').text
    article_file_line.append(publisher)		  
    ## 17 note
    #note = article.find('note')
    #if note is not None:
    #      note = article.find('note').text
    #article_file_line.append(note)		  
    ## 18 crossref
    crossref = article.find('crossref')
    if crossref is not None:
          crossref = article.find('crossref').text
    article_file_line.append(crossref)		  
    ## 19 isbn
    #isbn = article.find('isbn')
    #if isbn is not None:
    #      isbn = article.find('isbn').text
    #article_file_line.append(isbn)		  
    ## 20 series
    #series = article.find('series')
    #if series is not None:
    #      series = article.find('series').text
    #article_file_line.append(series)		  
    ## 21 school
    #school = article.find('school')
    #if school is not None:
    #      school = article.find('school').text
    #article_file_line.append(school)		  
    ## 22 chapter
    #chapter = article.find('chapter')
    #if chapter is not None:
    #      chapter = article.find('chapter').text
    #article_file_line.append(chapter)		  
    ## 23 publnr
    #publnr = article.find('publnr')
    #if publnr is not None:
    #      publnr = article.find('publnr').text
    #article_file_line.append(publnr)		  
    #########################################################
    print(article_file_line)	
    csvwriter.writerow(article_file_line)
    
  article_file.close()