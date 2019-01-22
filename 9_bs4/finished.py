import bs4
import requests
from tqdm import tqdm

html = requests.get('https://news.ycombinator.com/').text

soup = bs4.BeautifulSoup(html, "html.parser")
for story_link in tqdm(soup.select('.storylink')):
    page = requests.get(story_link['href']).text
    page_content = bs4.BeautifulSoup(page, "html.parser")
    title = page_content.find('title')
    if title:
        tqdm.write(title.text)
