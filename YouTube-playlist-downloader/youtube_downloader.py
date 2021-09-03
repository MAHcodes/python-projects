from pytube import Playlist
from pytube import YouTube
import os
from pathlib import Path

def clear():
    os.system("cls" if os.name == "nt" else "clear")


url = input("Enter YouTube Video/Playlist URL: ")
while True:
    download_format = str(input("1. Video/mp4\n2. Audio/mp3\nChoose File Type: "))
    if download_format == "1" or download_format == "2":
        clear()
        print("Making request please wait...")
        break


def download_playlist():
    p = Playlist(url)
    p_duration = 0
    ptitle = p.title
    try:
        os.makedirs(ptitle)
    except:
        print(f'Failed to create folder "{ptitle}"... folder already exists?')

    try:
        print(f"Playlist: {ptitle}\n{p.length} Videos | {'{:,}'.format(p.views)} Views | Last updated on: {p.last_updated}\n")
    except:
        pass

    for link in p:
        yt = YouTube(link)
        if download_format == "1":
            video = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first().default_filename
        elif download_format == "2":
            video = yt.streams.filter(type="audio").order_by("abr").desc().first().default_filename
        if Path(f"./{ptitle}/{p.index(link) + 1}. {video}").is_file():
            print(f'Failed downloading file: "{p.index(link) + 1}. {video}"... file already exists?')
        else:
            if download_format == "1":
                yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first().download(output_path=os.path.abspath(ptitle))
                os.rename(f"./{ptitle}/{video}", f"./{ptitle}/{p.index(link) + 1}. {video}")
            else:
                yt.streams.filter(type="audio").get_by_itag(251).download(output_path=os.path.abspath(ptitle))
                os.rename(f"./{ptitle}/{video}", f"./{ptitle}/{p.index(link) + 1}. {yt.title}.mp3")
            print(f"{p.index(link) + 1}. {yt.title} | OK")
            p_duration += yt.length
            print(f"Current playlist duration = {'{:.2f}'.format(p_duration / 3600)} hours\n")


def download_video():
    yt = YouTube(url)
    try:
        print(f"Video: {yt.title}\nVideo Duration: {'{:.2f}'.format(yt.length / 60)} minute | {'{:,}'.format(yt.views)} Views | Publish Date: {str(yt.publish_date).split(' ')[0]}")
    except:
        pass
    if download_format == "1":
        yt.streams.filter(progressive=True, file_extension="mp4").order_by( "resolution").desc().first().download()
    elif download_format == "2":
        yt.streams.filter(type="audio").get_by_itag(251).download()
        os.rename(f"./{yt.title}.webm", f"./{yt.title}.mp3")
    print(f"{yt.title} Successfully Downloaded")

if url.split("/")[-1].startswith("playlist"):
    download_playlist()
elif url.split("/")[-1].startswith("watch"):
    download_video()