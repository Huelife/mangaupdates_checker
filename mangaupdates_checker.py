#mangaupdates_checker.py: Pinging mangaupdates.com for new manga chapters

import webbrowser
import urllib.request
import re

import requests
from requests.exceptions import HTTPError

link = 'https://www.mangaupdates.com/releases.html'
chrome_loc = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

for url in [link]:
  try:
    response = requests.get(url)
    response.raise_for_status()
  except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
  except Exception as err:
    print(f'Other error occurred: {err}')
  else:
    print('Success!')
    webbrowser.get(chrome_loc).open_new_tab(link)  #open link if no errors
