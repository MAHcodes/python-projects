from pytube import YouTube

link = input("Enter Youtube Video Link: ")
print(f"Loading...Please wait")
vid = YouTube(link)
line = "-" * 20
print(f"Video details:\n{line}\nTitle: {vid.title}\nViews: {vid.views} View\nLength: {vid.length//60} minutes\nChannel: {vid.author}\nPublish date: {vid.publish_date}\n{line}\nDownloading...")


def download_vid():
    vid.streams.get_by_itag(22)
    vid.streams.first().download(output_path="C://Users/User/Downloads") # <<<<---- Choose your path from here


def finish():
    print("Video Download Successfully")


download_vid()
vid.register_on_complete_callback(finish())