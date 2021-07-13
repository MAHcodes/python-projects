import requests
from bs4 import BeautifulSoup
import csv

with open("olx-cars.csv", "w", encoding="utf-8") as file:
    file_write = csv.writer(file)
    file_write.writerow(["title", "price", "date", "location", "category", "link", "img"])
    for i in range(1, 308):
        url = 'https://www.olx.com.lb/en/vehicles/cars-for-sale/?page=' + str(i)
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        for article in soup.find_all("div", class_="ads__item"):
            try:
                img = article.find("img", class_="ads__item__photos")["src"]
            except:
                img = "None"
            try:
                title = article.find("a", class_="ads__item__ad--title").text
            except:
                title = "None"
            try:
                link = article.find("a", class_="ads__item__ad--title")["href"]
            except:
                link = "None"
            try:
                price = article.find("p", class_="ads__item__price price").text
            except:
                price = "None"
            try:
                category = article.find("p", class_="ads__item__breadcrumbs").text
            except:
                category = "None"
            try:
                date = article.find("p", class_="ads__item__date").text
            except:
                date = "None"
            try:
                location = article.find("p", class_="ads__item__location").text
            except:
                location = "None"

            title = title.strip()
            price = price.strip()
            date = date.strip()
            location = location.strip()
            category = category.strip()
            link = link.strip()
            img = img.strip()

            if title != "None":
                file_write.writerow(
                    [str(title), str(price), str(date), str(location), str(category), str(link), str(img)])

        print(f"Page {i}...ok")
    print("All pages...ok!")