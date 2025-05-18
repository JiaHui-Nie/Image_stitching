import os, datetime

while True:
    a = input()
    if a != "":
        exit()
    else:
        now = datetime.datetime.now()
        os.popen(F'adb exec-out screencap -p > "Screenshot_{now.year}-{str(now.month).zfill(2)}-{str(now.day).zfill(2)}-{str(now.hour).zfill(2)}-{str(now.minute).zfill(2)}-{str(now.second).zfill(2)}-{str(now.microsecond).zfill(6)[0:3]}.png"')