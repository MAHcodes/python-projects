from bs4 import BeautifulSoup
import requests
import csv

with open("cars2.csv", "w", encoding="utf-8") as file:
    file_write = csv.writer(file)
    file_write.writerow(["title", "price", "city", "location", "time", "car", "model", "year", "link", "img"])
    for i in range(1, 11):
        source = requests.get("https://lb.opensooq.com/en/cars/cars-for-sale?page="+str(i)+"&per-page=30").text
        soup = BeautifulSoup(source, "html.parser")

        for article in soup.find_all("li", class_="rectLi relative mb15"):
            try:
                img = article.find("img", class_="block")["src"]
            except:
                img = "None"
            try:
                title = article.find("a", class_="block postLink notEg postSpanTitle").text
            except:
                title = "None"
            try:
                link = article.find("a", class_="block postLink notEg postSpanTitle")["href"]
            except:
                link = "None"
            try:
                location = article.find("div", class_="clear font-12").text
            except:
                location = "None"
            try:
                price = article.find("div", class_="price-wrapper fLeft listingPrice").text
            except:
                price = "None"

            link = "https://lb.opensooq.com" + link
            title = title.strip()

            try:
                car = location.split("|")[3].strip()
            except:
                car = "None"
            try:
                model = location.split("|")[4].strip()
            except:
                model = "None"
            try:
                year = location.split("|")[5].strip()
            except:
                year = "None"
            try:
                time = location.split("|")[2].strip()[:13]
            except:
                time = "None"

            try:
                city = location.split("|")[1].strip()
            except:
                city = "None"

            try:
                location = location.split("|")[0].strip()
            except:
                location = "None"

            # if str(location) == "Nabatieh":
            file_write.writerow([str(title), str(price), str(location), str(city), str(time), str(car), str(model), str(year), str(link), str(img)])

        print(f"Page {i}...ok")
    print("All pages...ok!")
