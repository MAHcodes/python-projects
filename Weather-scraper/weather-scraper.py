from bs4 import BeautifulSoup
import requests

r = requests.get("https://weather.com/weather/today/l/33.24,35.38?par=google&temp=c").text
soup = BeautifulSoup(r, "lxml")

location = soup.find("h1", class_="CurrentConditions--location--1Ayv3").text
time = soup.find("div", class_="CurrentConditions--timestamp--1SWy5").text
temp = soup.find("span", class_="CurrentConditions--tempValue--3KcTQ").text
status = soup.find("div", class_="CurrentConditions--phraseValue--2xXSr").text
time = time.split()[2:4]

def now_temp():
    print(f"{location}\n{time[0]}{time[1]}\nTemperature: {temp} ({status})")

def today_temp():
    sec = soup.find("section", class_="card Card--card--4VS_Q")
    print(f"{location} | {time[0]} {time[1]}")
    for i in sec.find_all("li", class_="Column--column--2bRa6"):
        today = i.find("h3", class_="Column--label--L3RrD Column--default--2gARi").text
        today_temp = i.find("div", class_="Column--temp--2v_go").text
        divtitle = sec.find("div", class_="Column--icon--1fMZT")
        title = divtitle.find("title").text
        print(f"{today}: {today_temp} ({title})")

def hourly_temp():
    sec = soup.find("section", title="Hourly Forecast")
    print(f"{location} | {time[0]} {time[1]}")
    for i in sec.find_all("li", class_="Column--column--2bRa6"):
        today = i.find("h3", class_="Column--label--L3RrD Column--default--2gARi").text
        today_temp = i.find("div", class_="Column--temp--2v_go").text
        divtitle = sec.find("div", class_="Column--icon--1fMZT")
        title = divtitle.find("title").text
        print(f"{today}: {today_temp} ({title})")

def daily_tmep():
    sec = soup.find("section", title="Daily Forecast")
    print(f"{location} | {time[0]} {time[1]}")
    for i in sec.find_all("li", class_="Column--column--2bRa6"):
        today = i.find("h3", class_="Column--label--L3RrD Column--default--2gARi").text
        today_temp = i.find("div", class_="Column--temp--2v_go").text
        divtitle = sec.find("div", class_="Column--icon--1fMZT")
        title = divtitle.find("title").text
        print(f"{today}: {today_temp} ({title})")
