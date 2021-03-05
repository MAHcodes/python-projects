from bs4 import BeautifulSoup
import requests

def today():
    global soup
    global today
    source = requests.get("https://www.daysoftheyear.com/").text
    soup1 = BeautifulSoup(source, "lxml")

    all = soup1.find("a", class_="section__cta section__cta--desktop desktop-only")["href"]

    source2 = requests.get(all).text
    soup = BeautifulSoup(source2, "lxml")

    today = soup.find("div", class_="date_day").text
    print(f"Today is: {today}")
    getev()

def custom(d, m):
    global soup
    global today
    source = requests.get("https://www.daysoftheyear.com/days/2021/"+m+"/"+d+"/").text
    soup = BeautifulSoup(source, "lxml")
    today = soup.find("div", class_="date_day").text
    print(today)
    getev()


def getev():
    for article in soup.find_all("div", class_="card card--day linked"):
        img = article.find("img")["src"]
        date = article.find("div", class_="date_day").text
        event = article.find("h3").text
        if date == today:
            print(event)
        else:
            break


if __name__ == '__main__':
    while True:
        whatday = int(input("1. Get today events.\n2. Get custom day events.\nChoose for get events: "))
        if whatday == 1:
            today()
            break
        elif whatday == 2:
            d = str(input("Enter which day: "))
            m = str(input("Enter which month: "))
            custom(d, m)
            break
        else:
            print("Invalid input! Enter only 1 or 2...")