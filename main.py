from PIL import Image
import os

def getfiles():
    filelist = []
    i = input("please DRAG the filefolder to there (don't put any other files in the folder) -->")
    for j in os.listdir(i):
        img = Image.open(i+'\\'+j)
        if len(filelist) and (img.size != filelist[-1].size):
            print("Image size seems like not the same. Please check it.")
            img.close()
        else:
            filelist.append(img)
    return filelist

def processImages(filelist):
    output = Image.new("RGB", filelist[0].size)
    for i in filelist:
        for j in range(i.size[0]):
            for k in range(i.size[1]):
                pixel = i.getpixel((j, k))
                if (pixel[0] != 0 or pixel[1] != 0 or pixel[2] != 0):
                    current = output.getpixel((j, k))
                    m = (current[0] + current[1] + current[2]) / 3
                    n = (pixel[0] + pixel[1] + pixel[2])/3
                    if m > 128:
                        a = 255-m
                    else:
                        a = m
                    if n > 128:
                        b = 255-n
                    else:
                        b = n
                    if(b > a) or ((m == 0) and (n != 0)):
                        output.putpixel((j, k), pixel)
    output.save("output.png")

if __name__ == "__main__":
    filelist = getfiles()
    print("processing images, please wait...")
    img = processImages(filelist)