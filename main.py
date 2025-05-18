from PIL import Image
import time

def getfiles():
    filelist = []
    while True:
        i = input("please DRAG the file to there -->")
        if (not len(i)) or (i.isspace()):
            if len(filelist) == 0:
                print("You haven't put any file yet! Process will exit in 5 seconds.")
                time.sleep(5)
                exit(-1)
            else:
                break
        img = Image.open(i)
        if len(filelist) and (img.size != filelist[-1].size):
            print("Image size seems like not the same as the one before. Please choose another one.")
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
