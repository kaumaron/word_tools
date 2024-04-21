import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta

today = datetime.today() - timedelta(days=0)
today = today.strftime("%b %-d, %Y")

print(today)

answers = 'https://word.tips/todays-nyt-connections-answers/'

headers = {'user-agent': 'nyt-cheat-kit/0.0.1'}
r = requests.get(answers,headers=headers)

if r.status_code != 200:
    print(f'Error with site: {r.status_code}')

soup = bs(r.text, 'html.parser')

headers = soup.find_all('h3', class_ = 'text-[1rem] font-bold mb-2 leading-[25px]')

for h in headers:
    if h.text.startswith(today):
        for item in h.next_sibling:
            print(item.text)