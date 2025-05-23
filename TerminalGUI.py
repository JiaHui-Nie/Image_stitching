import Core.FileExtension
import Core.ProcessImage

if __name__ == "__main__":
    path = input("please DRAG the filefolder to there (don't put any other files in the folder) -->")
    filelist = Core.FileExtension.GetLocalImages(path)
    print("processing images, please wait...")
    img = Core.ProcessImage.MergeImages(filelist)
    img.save("output.png")