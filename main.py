from PIL import Image
import numpy as np
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
    current_arr = np.array(output)
    current_aver = np.abs(current_arr.mean(axis=2)-128)

    for i in filelist:
        if i.mode != "RGB":
            i = i.convert("RGB")
        arr = np.array(i)
        aver = np.abs(arr.mean(axis=2)-128)

        operate = np.less(aver, current_aver)
        for j in range(i.size[1]):
            for k in range(i.size[0]):
                if operate[j][k]:
                    current_arr[j][k] = arr[j][k]
                    current_aver[j][k] = aver[j][k]
    output = Image.fromarray(current_arr)
    output.save("output.png")

if __name__ == "__main__":
    filelist = getfiles()
    print("processing images, please wait...")
    img = processImages(filelist)