#mangaupdates_checker.py: Pinging mangaupdates.com for new manga chapters

import webbrowser
import urllib.request
import re
import time

import requests
from requests.exceptions import HTTPError

class Manga():
  def __init__(self,title):
    self.title = title

#One Piece manga, current chapter
class OnePiece(Manga):
  def __init__(self,title):
    self.manga_title = 'One Piece'
    self.series = '33&stype=series'
    self.chapter = '968<'
    self.chrome_loc = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    self.link = 'https://www.mangaupdates.com/releases.html?search={}'.format(self.series)
    self.page = urllib.request.urlopen(self.link).read().decode('utf-8')
    self.match = re.findall(self.chapter, self.page)
    super().__init__(title)
    
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
 
#Vinland Saga manga, current chapter
class VinlandSaga(Manga):
  def __init__(self,title):
    self.manga_title = 'Vinland Saga'
    self.series = '1568&stype=series'
    self.chapter = '169<'
    self.chrome_loc = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    self.link = 'https://www.mangaupdates.com/releases.html?search={}'.format(self.series)
    self.page = urllib.request.urlopen(self.link).read().decode('utf-8')
    self.match = re.findall(self.chapter, self.page)
    super().__init__(title)
    
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
