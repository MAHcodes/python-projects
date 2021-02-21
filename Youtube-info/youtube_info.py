from apiclient.discovery import build

#-----API-KEY-----#
key = 'AIzaSyB9wA_ywK-xsBl-shsSFbRgQFdu_JifZYE'
youtube = build('youtube', 'v3', developerKey= key)
res = youtube.channels().list(id="UCMbleSlNSOJZvWF3tqY5bCw", part="statistics").execute()
print("ANDRO TOP YouTube Channel")
print(res['items'][0]['statistics']['subscriberCount'] + " Subscribe")
print(res['items'][0]['statistics']['viewCount'] + " Views")
print(res['items'][0]['statistics']['videoCount'] + " Video")