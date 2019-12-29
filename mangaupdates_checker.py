#mangaupdates_checker.py: Pinging mangaupdates.com for new manga chapters

import webbrowser
import urllib.request
import re

import requests
from requests.exceptions import HTTPError

class Manga():
  manga_title = ''
  series = ''
  chapter = ''
  chrome_loc = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
  link = 'https://www.mangaupdates.com/releases.html?search={}'.format(series)
  page = urllib.request.urlopen(link).read().decode('utf-8')
  match = re.findall(chapter, page)
  
  def __init__(self,title):
    self.title = title
    
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
    
class OnePiece(Manga):
  def __init__(self,title,series,chapter):
    self.manga_title = 'One Piece'
    self.series = '33&stype=series'
    self.chapter = '968'
    super().__init__(title)
    
class VinlandSaga(Manga):
  def __init__(self,title,series,chapter):
    self.manga_title = 'Vinland Saga'
    self.series = '1568&stype=series'
    self.chapter = '169'
    super().__init__(title)

#variables for webbrowser, website link, reading webpage, and re
#link_01 = 'https://www.mangaupdates.com/releases.html?search=33&stype=series'
#link_02 = 'https://www.mangaupdates.com/releases.html?search=1568&stype=series'
#page_01 = urllib.request.urlopen(link_01).read().decode('utf-8')
#page_02 = urllib.request.urlopen(link_02).read().decode('utf-8')
#match_01 = re.findall("967<", page_01)
#match_02 = re.findall("169<", page_02)

#grouping multiple links and matches in tuples
#link = {
#  0:link_01,
#  1:link_02,
#  }
#match = {
#  0:match_01,
#  1:match_02,
#  }

#if new chapter == True, attempt to open webpage
#for x in range(2):
 # if match[x] is None or len(match[x]) == 0:
  #  if link[x] == link_01:
   #   print('One Piece:')    
    #elif link[x] == link_02:
    #  print('Vinland Saga:')
    #print('No new chapter...')
    #print('')
  #else:
#    if link[x] == link_01:
 #     print('One Piece:')
  #    try:
   #     response = requests.get(link[x])
    #    response.raise_for_status()
     # except HTTPError as http_err:
      #  print(f'HTTP error occurred: {http_err}')
      #except Exception as err:
 #       print(f'Other error occurred: {err}')
  #    else:
   #     print('New chapter is out!')
    #    print('')
     #   webbrowser.get(chrome_loc).open_new_tab(link[x])
        #open link if no errors
 #   elif link[x] == link_02:
  #    print('Vinland Saga:')
   #   try:
#        response = requests.get(link[x])
 #       response.raise_for_status()
  #    except HTTPError as http_err:
   #     print(f'HTTP error occurred: {http_err}')
    #  except Exception as err:
     #   print(f'Other error occurred: {err}')
#      else:
 #       print('New chapter is out!')
  #      print('')
   #     webbrowser.get(chrome_loc).open_new_tab(link[x])
        #open link if no errors
