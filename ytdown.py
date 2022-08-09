from pytube import YouTube;
import requests;
import shutil;

link = input("Enter the yt link to download: ")
vid = YouTube(link)

thumbnail_link = vid.thumbnail_url
resp = requests.get(thumbnail_link, stream=True)
local_file = open(r'local_image.jpg', 'wb')
resp.raw.decode_content = True
shutil.copyfileobj(resp.raw, local_file)
del resp

print("Title : ",vid.title)
stream = vid.streams.get_highest_resolution()

print("Downloading .....")
stream.download()
print("Download completed.!!")
