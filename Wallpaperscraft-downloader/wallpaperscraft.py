import urllib.request
import requests
from bs4 import BeautifulSoup
import os


def main():

    start_page = 1
    end_page = 10
    cat = "black"
    res = "2560x1440"

    # headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

    try:
        os.makedirs(cat)
    except:
        print(f"({cat}) directory exsists")

    for i in range(start_page, end_page):
        URL = f"https://wallpaperscraft.com/catalog/{cat}/{res}/page{str(i)}"

        try:
            page = requests.get(URL, headers=headers)
        except:
            return "network error"

        soup = BeautifulSoup(page.content, "html.parser")

        images_list = soup.find_all("a", class_="wallpapers__link")

        j = 1
        for img_url in images_list:

            try:
                img_page = requests.get(f'https://wallpaperscraft.com{img_url["href"]}', headers=headers)
            except:
                return "network error"

            soup_page = BeautifulSoup(img_page.content, "html.parser")

            wallpaper = soup_page.find("img", class_="wallpaper__image")

            try:
                img_src = wallpaper["src"]
            except:
                print(f"{j} Err")
                urllib.request.urlretrieve(img_src, f"./{cat}/{img_name}")
                j += 1
                continue

            img_name = img_src.split("/")[-1]

            if os.path.isfile(f"./{cat}/{img_name}"):
                print(f"{img_name} exsists")

            else:
                urllib.request.urlretrieve(img_src, f"./{cat}/{img_name}")
                print(f"{j} OK")
                j += 1
            
        print(f"Page {str(i)} done.")


if __name__ == "__main__":
    main()
