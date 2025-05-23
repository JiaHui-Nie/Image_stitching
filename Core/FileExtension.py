from PIL import Image
from io import BytesIO
import datetime
import os

def GetLocalImages(path):
    filelist = []
    for file in os.listdir(path):
        img = Image.open(path+'\\'+file)
        filelist.append((img, file))
    return filelist

def GetScreenshot():
    now = datetime.datetime.now()
    Image_content = os.popen("adb exec-out screencap -p").read()
    Image = Image.open(BytesIO(Image_content))
    return (Image, F"Screenshot_{now.year}-{str(now.month).zfill(2)}-{str(now.day).zfill(2)}-{str(now.hour).zfill(2)}-{str(now.minute).zfill(2)}-{str(now.second).zfill(2)}-{str(now.microsecond).zfill(6)[0:3]}.png")