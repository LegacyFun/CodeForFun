"""
Way too easy?! Youtube Downloader, Just for Fun!!
"""
from pytube import YouTube

URL = input('Please enter the URL: ')
Dir = input('Where do you prefer to save it: ')
yt = YouTube(URL)
stream = yt.streams.first()
stream.download(Dir)

