#mangaupdates_checker.py: Pinging mangaupdates.com for new manga chapters

import webbrowser
import urllib.request
import re

import requests
from requests.exceptions import HTTPError

class Manga():
  #master variables
  manga_title = ''
  series = ''
  chapter = ''
  chrome_loc = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
  link = 'https://www.mangaupdates.com/releases.html?search={}'.format(series)
  page = urllib.request.urlopen(link).read().decode('utf-8')
  match = re.findall(chapter, page)
  
  def __init__(self,title):
    self.title = title
    
  #if new chapter == True, attempt to open webpage  
  def verify_chapter(self):
    if match is None or len(match) == 0:
      print(self.title+':')
      print('No new chapter...')
      print('')    
    else:
      print(self.title+':')
      try:
        response = requests.get(link)
        response.raise_for_status()
      except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
      except Exception as err:
        print(f'Other error occurred: {err}')
      else:
        print('New chapter is out!')
        print('')
        webbrowser.get(chrome_loc).open_new_tab(link)
        #open link if no errors

#One Piece manga, current chapter
class OnePiece(Manga):
  def __init__(self,title,series,chapter):
    self.manga_title = 'One Piece'
    self.series = '33&stype=series'
    self.chapter = '968'
    super().__init__(title)
 
#Vinland Saga manga, current chapter
class VinlandSaga(Manga):
  def __init__(self,title,series,chapter):
    self.manga_title = 'Vinland Saga'
    self.series = '1568&stype=series'
    self.chapter = '169'
    super().__init__(title)
