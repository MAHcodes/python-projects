import requests
from bs4 import BeautifulSoup
import csv

year = "2021"
session = "5"
start_id = 2310285
end_id =  2310290

verification = "CfDJ8MXRrayate9EkeJ6Hvz4LBe4VW5FnVfGv7zUGIrc8bgdniEavB38be-8iZw_PLkHNSmLKXTOOaZez1lF9Ua3C6jcIsstqc7unCduHYtU5WC5LW3pfAvDiaTFtd1miGCXq_FHbQoOxHUhNfk-sF-bhLg"
url = "http://results.vte-gov.com/Home/Check"
headers = { 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}
cookies = { "_ga":"GA1.2.2062735799.1655550382", "gat_gtag_UA_158183402_1": "1", "_gid":"GA1.2.694362085.1655550382", ".AspNetCore.Antiforgery.nJXLmC48KdQ":"CfDJ8MXRrayate9EkeJ6Hvz4LBcbZH_A8YbinjioDu9f7_X4JcJ66WBo_z5f5IRS0lB4IMUs9mqn80cewxLRy33iPleT0K1p_Tci7EEJalxlrnEEsTJm4aqoxJnIgTDmWtJfLRfBzByWj-cTmMf2NM-RFiU"}

with open("vte-results.csv", "w", encoding="utf-8") as file:
    file_write = csv.writer(file)
    file_write.writerow(["StudentID", "Student Name", "Speciality", "Total /2000", "Avarage /20", "Estlhak", "Result", "Project /20"])
    for i in range(start_id, end_id ):
        st_id = i
        data = {'year': year, 'studentId' : st_id, 'session' : session,'__RequestVerificationToken': verification }

        page = requests.post(url, headers=headers, cookies=cookies, data=data)
        soup = BeautifulSoup(page.content, 'html.parser')

        studentInfo = soup.find("div", { "id": "student_infos"})
        st_name = studentInfo.findAll("div", class_="tag_select padtxt")[3].text
        st_spec = studentInfo.findAll("div", class_="tag_select padtxt")[4].text
        st_result = studentInfo.findAll("div", class_="tag_select padtxt green")[0].find("span").text
        st_avg = studentInfo.findAll("div", class_="tag_select padtxt eng_lang")[1].text
        st_total = soup.findAll("tr", class_="total")[-1].findAll("b")[-1].text
        st_es = soup.findAll("tr", class_="total")[-2].findAll("b")[-1].text
        st_proj = float(soup.find("div", { "id": "student_notes" }).findAll("tr")[-3].findAll("td")[-1].text) / 12

        file_write.writerow([str(st_id), str(st_name), str(st_spec), str(st_total), str(st_avg), str(st_es), str(st_result), str(st_proj)]) 

        print("id " + str(st_id) + " done" )
