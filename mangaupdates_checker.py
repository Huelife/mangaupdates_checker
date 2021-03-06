#mangaupdates_checker.py: Pinging mangaupdates.com for new manga chapters

import webbrowser
import urllib.request
import re
import time

import requests
from requests.exceptions import HTTPError

#Manga superclass
class Manga():
  manga_title = ''
  
  #creating shared variables for subclasses
  def __init__(self,title,chrome_loc,link,page,match):
    self.title = title
    self.chrome_loc = ('C:/Program Files (x86)/Google/Chrome/Application/'
                       'chrome.exe %s')
    self.link = ('https://www.mangaupdates.com/releases.html?search={}'
                 .format(self.series))
    self.page = urllib.request.urlopen(self.link).read().decode('utf-8')
    self.match = re.findall(self.chapter, self.page)
    
  #if new chapter == True, attempt to open webpage  
  def verify_chapter(self):
    if self.match is None or len(self.match) == 0:
      print(self.manga_title+':')
      print('No new chapter...')
      print('')    
    else:
      print(self.manga_title+':')
      try:
        response = requests.get(self.link)
        response.raise_for_status()
      except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
      except Exception as err:
        print(f'Other error occurred: {err}')
      else:
        print('New chapter is out!')
        print('')
        time.sleep(1.5)
        webbrowser.get(self.chrome_loc).open_new_tab(self.link)
        #open link if no errors

#One Piece manga subclass, new chapter
class OnePiece(Manga):
  def __init__(self,title,chrome_loc,link,page,match):
    self.manga_title = 'One Piece'
    self.series = '33&stype=series'
    self.chapter = '968<'    
    super().__init__(title,chrome_loc,link,page,match)
    
#Vinland Saga manga subclass, new chapter
class VinlandSaga(Manga):
  def __init__(self,title,chrome_loc,link,page,match):
    self.manga_title = 'Vinland Saga'
    self.series = '1568&stype=series'
    self.chapter = '169<'
    super().__init__(title,chrome_loc,link,page,match)

#D.Gray-man manga subclass, new chapter
class DGrayman(Manga):
  def __init__(self,title,chrome_loc,link,page,match):
    self.manga_title = 'D.Gray-man'
    self.series = '95&stype=series'
    self.chapter = '235<'
    super().__init__(title,chrome_loc,link,page,match)

#One Punch-Man manga subclass, new chapter
class OnePunchMan(Manga):
  def __init__(self,title,chrome_loc,link,page,match):
    self.manga_title = 'One Punch-Man'
    self.series = '80345&stype=series'
    self.chapter = '125<'
    super().__init__(title,chrome_loc,link,page,match)
        
#Berserk manga subclass, new chapter
class Berserk(Manga):
  def __init__(self,title,chrome_loc,link,page,match):
    self.manga_title = 'Berserk'
    self.series = '88&stype=series'
    self.chapter = '360<'
    super().__init__(title,chrome_loc,link,page,match)
        
#grouping all manga titles together                
manga_tuple = {
  0:OnePiece('','','','','').verify_chapter(),
  1:VinlandSaga('','','','','').verify_chapter(),
  2:DGrayman('','','','','').verify_chapter(), 
  3:OnePunchMan('','','','','').verify_chapter(),
  4:Berserk('','','','','').verify_chapter(),
  }

#checking each manga titles for new chapters
for new in range(5):
  manga_tuple[new]
