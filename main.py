import requests
from bs4 import BeautifulSoup

import time

betting_page_content = requests.get('https://olimpbet.kz/betting')

#betting_file_path = 'C:/Users/saparov.m.HSK/Documents/Olimp/parser/data/betting.txt'


while True:
    html_text = betting_page_content.text
    soup = BeautifulSoup(html_text, 'html.parser')

    table_tennis_list = soup.findAll("tr", {"data-sport" : "40", "data-kek":"row"})

    print(len(table_tennis_list))

    for tennis_match in table_tennis_list:
        for tags in tennis_match.findAll("a", {"class" : "l-name-tab"}):
            print(tags.text, ' - ', tags.get("href"))
            print("----------------------------------")
            
    time.sleep(5)
#with open(betting_file_path, 'w', encoding="utf-8") as f:
#    f.write(html_text)
