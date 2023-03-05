#import module python tube
import pytube
from tkinter import filedialog

print("Videos Download")
url = input("Enter URL Here: ")

type = input("Need audio or video: ").lower().strip()

folder_name = filedialog.askdirectory()

if type == "video" or type == "v":
     pytube.YouTube(url).streams.get_highest_resolution().download(folder_name)
     print("Done")

elif type == "audio" or type == "a":
     pytube.YouTube(url).streams.get_audio_only().download(folder_name)
     print("Done")
else:
    print("please enter correct type such video , audio , v or a")    


