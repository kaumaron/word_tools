import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta


today = datetime.today()
wordle_1 = datetime(2021, 6, 19, 0, 0, 0)
wordle_number = today - wordle_1

answers = 'https://www.tomsguide.com/news/what-is-todays-wordle-answer'

headers = {'user-agent': 'nyt-cheat-kit/0.0.1'}
r = requests.get(answers,headers=headers)

if r.status_code != 200:
    print(f'Error with site: {r.status_code}')

soup = bs(r.text, 'html.parser')

print(f'{today.strftime("%b %-d, %Y")} - Wordle #{wordle_number.days}\n')

# <strong> text surrounds a hint on the first letter and the answer
# they are the final two uses of <strong>
bold = soup.find_all('strong')[-2:]

if input('Do you want a hint? (y/n) ') == 'y':
    print(bold[0].text[:-1] + '\n')
else:
    print('\n')

if input('You sure you want the answer? (y/n) ') == 'y':
    print(bold[1].text)

