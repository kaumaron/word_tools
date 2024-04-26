import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta

today = datetime.today() - timedelta(days=0)
today = today.strftime("%b %-d, %Y")

print(today)

answers = "https://word.tips/todays-nyt-mini-crossword-clues-answers/"
across_id = "Across Clues and Answers for Today's Puzzle"
down_class = "text-[1.5rem] mb-5 leading-[38px]"
across_mark = "********** ACROSS **********"
down_mark = "********** DOWN **********"

headers = {"user-agent": "nyt-cheat-kit/0.0.1"}
r = requests.get(answers, headers=headers)

if r.status_code != 200:
    print(f"Error with site: {r.status_code}")

soup = bs(r.text, "html.parser")

across = soup.find("div", {"id": across_id})

clues = across.findChildren("h3")
all_answers = [a.next_sibling.text for a in clues]

# sort
across_answers = [
    a for idx, a in enumerate(all_answers) if idx < all_answers.index("") and a != ""
]

down_answers = [
    a for idx, a in enumerate(all_answers) if idx > all_answers.index("") and a != ""
]

print(across_mark)
for ans in across_answers:
    print(ans.split(" ")[-1].replace(".", ""))

print(down_mark)
for ans in down_answers:
    print(ans.split(" ")[-1].replace(".", ""))
