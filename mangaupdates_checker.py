#mangaupdates_checker.py: Pinging mangaupdates.com for new manga chapters

import webbrowser

import requests
from requests.exceptions import HTTPError

link = 'https://www.mangaupdates.com/releases.html'
chrome_loc = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
