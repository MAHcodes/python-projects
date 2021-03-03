import tkinter
from apiclient.discovery import build

#>>>>>>>>>>>> YOUR API KEY <<<<<<<<<<<<<<<
key = 'AIzaSyB9wA_ywK-xsBl-shsSFbRgQFdu_JifZYE'
youtube = build('youtube', 'v3', developerKey= key)
res = youtube.channels().list(id="UCMbleSlNSOJZvWF3tqY5bCw", part="statistics").execute()
# res = youtube.channels().list(forUsername= , part="statistics").execute()

subct = res['items'][0]['statistics']['subscriberCount'] +" Subscribe"
vwsct = res['items'][0]['statistics']['viewCount'] +" Views"
vidct = res['items'][0]['statistics']['videoCount'] +" Video"

root = tkinter.Tk()
root.title("ANDRO TOP")
root.geometry("250x120+600+100")


def func():
    channel_lbl4.config(text=subct)
    channel_lbl5.config(text=vwsct)
    channel_lbl6.config(text=vidct)


channel_lbl0 = tkinter.Label(root, text="ANDRO TOP channel info: ")
channel_lbl0.grid(row=0, column=0)
channel_lbl1 = tkinter.Label(root, text=" Subscribers Count: ")
channel_lbl1.grid(row=1, column=0)
channel_lbl2 = tkinter.Label(root, text=" Views Count: ")
channel_lbl2.grid(row=2, column=0)
channel_lbl3 = tkinter.Label(root, text=" Videos Count: ")
channel_lbl3.grid(row=3, column=0)
channel_lbl4 = tkinter.Label(root, text="")
channel_lbl4.grid(row=1, column=1)
channel_lbl5 = tkinter.Label(root, text="")
channel_lbl5.grid(row=2, column=1)
channel_lbl6 = tkinter.Label(root, text="")
channel_lbl6.grid(row=3, column=1)

btn = tkinter.Button(root, text="Search", command=func)
btn.grid(row= 4, column=0)
btn2 = tkinter.Button(root, text="Quit", command=quit)
btn2.grid(row=4,column=1)
root.mainloop()