import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta

today = datetime.today() - timedelta(days=0)
today = today.strftime("%b %-d, %Y")

print(today)

answers = "https://word.tips/todays-nyt-connections-answers/"

headers = {"user-agent": "nyt-cheat-kit/0.0.1"}
r = requests.get(answers, headers=headers)

if r.status_code != 200:
    print(f"Error with site: {r.status_code}")

soup = bs(r.text, "html.parser")

headers = soup.find_all("h3", class_="text-[1rem] font-bold mb-2 leading-[25px]")

difficulty = {0: "green", 1: "yellow", 2: "blue", 3: "purple"}

answer_list = []
for h in headers:
    if h.text.startswith(today):
        for item in h.next_sibling:
            answer_list.append(item.text)

categories = {
    difficulty[idx]: answer.split(":")[0] for idx, answer in enumerate(answer_list)
}
answers = {
    difficulty[idx]: answer.split(":")[1] for idx, answer in enumerate(answer_list)
}

if input("Do you want hints? (y/n) ").lower().strip() == "y":
    cheat = True
    print('\tType "end" to exit.')
    print("\tDifficulties -- green, yellow, blue, purple, all")
    while cheat:
        choice = input("\nWhich difficulty are you looking for? ").lower().strip()
        if choice == "end":
            cheat = False
        elif choice == "all":
            print("\n".join(categories.values()))
        else:
            try:
                print(categories[choice])
            except IndexError:
                print("Try again.")

if (input("\nAre you sure you want to cheat? (y/n) ").lower().strip()) == "y":
    cheat = True
    print('\tType "end" to exit.')
    print("\tDifficulties -- green, yellow, blue, purple, all")
    while cheat:
        choice = input("\nWhich difficulty are you looking for? ").lower().strip()
        if choice == "end":
            cheat = False
        elif choice == "all":
            print("\n".join(answers.values()))
        else:
            try:
                print(answers[choice])
            except IndexError:
                print("Try again.")
else:
    print("\n** Good for you.  **\n")
