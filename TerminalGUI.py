import Core.FileExtension
import Core.ProcessImages

if __name__ == "__main__":
    print("Please choose a method to get the images.")
    print("1.Local file")
    print("2.Screenshots(android) *adb is needed")
    choice = int(input("Please choose:"))
    if choice == 1:
        path = input("please DRAG the filefolder to there (don't put any other files in the folder) -->")
        filelist = Core.FileExtension.GetLocalImages(path)
    elif choice == 2:
        print("Press Enter to capture screenshot, the press anykey and then press Enter to process images.")
        filelist = []
        choice = input()
        while(choice == ''):
            filelist.append(Core.FileExtension.GetScreenshot())
            print("Successful got screenshot.")
            choice = input()
    print("processing images, please wait...")
    img = Core.ProcessImages.MergeImages(filelist)
    img.save("output.png")