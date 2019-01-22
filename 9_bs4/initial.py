import bs4
import requests

html = requests.get('https://news.ycombinator.com/').text
print(html)
