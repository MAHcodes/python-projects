from bs4 import BeautifulSoup
import requests

r = requests.get("https://weather.com/weather/today/l/33.24,35.38?par=google&temp=c").text
soup = BeautifulSoup(r, "lxml")
location = soup.find("h1", class_="CurrentConditions--location--1Ayv3").text
time = soup.find("div", class_="CurrentConditions--timestamp--1SWy5").text
temp = soup.find("span", class_="CurrentConditions--tempValue--3KcTQ").text
status = soup.find("div", class_="CurrentConditions--phraseValue--2xXSr").text
time = time.split()[2:4]

def main(forecast):
    sec = soup.find("section", title=forecast)
    print(f"\n{location} | {time[0]} {time[1]}")
    for i in sec.find_all("li", class_="Column--column--2bRa6"):
        today = i.find("h3", class_="Column--label--L3RrD Column--default--2gARi").text
        today_temp = i.find("div", class_="Column--temp--2v_go").text
        divtitle = i.find("div", class_="Column--icon--1fMZT")
        title = divtitle.find("title").text
        if today_temp == "--" and today == "Today":
            today_temp = temp
        print(f"{today}: {today_temp} ({title})")


if __name__ == "__main__":
    user = int(input(f"{location} | {time[0]} {time[1]}\nCurrent weather: {temp} ({status})\n\n1. Hourly Forecast\n2. Daily Forecast\nChoose number to get more info: "))
    if user == 1:
        forecast = "Hourly Forecast"
    elif user == 2:
        forecast = "Daily Forecast"
    main(forecast)