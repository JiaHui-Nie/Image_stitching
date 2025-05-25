from PIL import Image

import os
def GetLocalImages(path):
    filelist = []
    for filename in os.listdir(path):
        img = Image.open(path+"\\"+filename)
        filelist.append((img, filename))
    return filelist

from subprocess import Popen, PIPE
from io import BytesIO
import datetime
def GetScreenshot():
    now = datetime.datetime.now()
    command = Popen("adb exec-out screencap -p", shell=True, stdout=PIPE)
    Image_data = command.stdout.read()

    PNG_ENDING = bytes.fromhex("AE426082")
    while(Image_data[-4::] != PNG_ENDING):
        Image_data += command.stdout.read()

    img = Image.open(BytesIO(Image_data))
    return (img, F"Screenshot_{now.year}-{str(now.month).zfill(2)}-{str(now.day).zfill(2)}-{str(now.hour).zfill(2)}-{str(now.minute).zfill(2)}-{str(now.second).zfill(2)}-{str(now.microsecond).zfill(6)[0:3]}.png")

from selenium import webdriver
import requests, time
def GetDouyinImages(url,driver = None, timewait=3, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"}):
    filelist = []

    if driver == None:
        driver = webdriver.Edge("msedgedriver.exe")
    driver.get(url)
    time.sleep(timewait)
    detail = driver.find_element_by_class_name("note-detail-container")
    img_elements = detail.find_elements_by_tag_name("img")
    img_urls = set([i.get_attribute("src") for i in img_elements])

    for i in img_urls:
        img_request = requests.get(i, headers=headers)
        img = Image.open(BytesIO(img_request.content))
        filelist.append((img, i.split("?")[0].split("/")[-1]))

    driver.close()
    return filelist