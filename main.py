import requests
from bs4 import BeautifulSoup
import re
import csv




page = {}

url1 = "https://helion.pl/kategorie/programowanie"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
}




page_num = 1

with open("ksiazki_helion.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(["Tytuł", "Cena"])
    
    for i in range(0, 42):
        if page_num == 1:
            page = requests.get(url1, headers=headers).text
        else:
            page = requests.get(f"https://helion.pl/kategorie/programowanie/{page_num}", headers=headers).text
        doc = BeautifulSoup(page, "html.parser")
        prices = doc.find_all("ins")
        titles = doc.find_all("p", class_="heading3")

        for title, price in zip(titles, prices):
            writer.writerow([title.a.string.strip(), price.string.strip()])
            print(f"{title.a.string.strip()} - {price.string.strip()}")
        page_num += 1


