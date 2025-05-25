from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from threading import Thread
import os

import Core.FileExtension
import Core.ProcessImages

def ImportImages():
    if method.get() == "本地文件夹":
        folder = path.get()
        if os.path.exists(folder):
            newimages = Core.FileExtension.GetLocalImages(folder)
            filelist.extend(newimages)
            for i in newimages:
                img_list.insert(END, i[1])
        else:
            showerror("错误", "所填写的目录不存在")
    elif method.get() == "安卓设备截图(adb)":
        newimage = Core.FileExtension.GetScreenshot()
        filelist.append(newimage)
        img_list.insert(END, newimage[1])
    elif method.get() == "抖音图文":
        newimages = Core.FileExtension.GetDouyinImages(path.get())
        filelist.extend(newimages)
        for i in newimages:
            img_list.insert(END, i[1])

def DeleteImage():
    filelist.pop(img_list.curselection()[0])
    img_list.delete(img_list.curselection()[0])

def ProcessImages():
    img = Core.ProcessImages.MergeImages(filelist)
    outname = asksaveasfilename(title="选择保存输出文件的位置",
                                initialfile="output.png",
                                filetypes=[("PNG", ".png"),
                                           ("JPEG", ".jpg"),
                                           ("BMP", ".bmp"),
                                           ("GIF", ".gif"),
                                           ("TIFF", ".tiff"),
                                           ("WEBP", ".webp")])
    img.save(outname)

def ChooseImage(event):
    img = filelist[img_list.curselection()[0]][0]
    img.show()

if __name__ == "__main__":
    filelist = []

    root = Tk()
    root.title("Image Stitching")
    root.minsize(410, 225)
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=5)
    root.grid_columnconfigure(4, weight=1)

    import_group = LabelFrame(root, text="导入图片")
    import_group.grid_columnconfigure(1, weight=1)
    import_group.grid_rowconfigure(0, weight=1)
    import_group.grid_rowconfigure(1, weight=1)

    method_text = Label(import_group, text="方式")
    method_text.grid(row=0, column=0)
    method = Combobox(import_group)
    method["values"] = ("本地文件夹", "安卓设备截图(adb)", "抖音图文")
    method.current(0)
    method.grid(row=0, column=1, columnspan=3, sticky=N+S+W+E, padx=4, pady=4)

    path_text = Label(import_group, text="路径/链接")
    path_text.grid(row=1, column=0)
    path = Entry(import_group)
    path.grid(row=1, column=1, columnspan=3, sticky=N+S+W+E, padx=4, pady=4)

    import_button = Button(import_group, text="导入", command=lambda :Thread(target=ImportImages).start())
    import_button.grid(row=0, column=4, rowspan=2, sticky=N+S+W+E)

    import_group.grid(row=0, column=0, rowspan=2, columnspan=5, sticky=N+S+W+E, padx=4, pady=4)

    delete_group = LabelFrame(root, text="删除图片")
    delete_button = Button(delete_group, text="删除", command=lambda :Thread(target=DeleteImage).start())
    delete_button.grid(row=0, column=0)
    delete_group.grid(row=0, column=5, columnspan=2, padx=2, pady=2)


    process_group = LabelFrame(root, text="处理图片")
    process_button = Button(process_group, text="处理", command=lambda :Thread(target=ProcessImages).start())
    process_button.grid(row=0, column=0)
    process_group.grid(row=1, column=5, columnspan=2, padx=2, pady=2)

    list_group = LabelFrame(root, text="待处理图片列表（可点选预览）")
    list_group.grid_rowconfigure(0, weight=1)
    list_group.grid_columnconfigure(0, weight=1)

    img_scroolbar = Scrollbar(list_group)
    img_scroolbar.grid(row=0, column=1, sticky=N+S)
    img_list = Listbox(list_group, yscrollcommand=img_scroolbar.set)
    img_list.grid(row=0, column=0,sticky=N+S+W+E)
    img_scroolbar.config(command=img_list.yview)

    img_list.bind("<<ListboxSelect>>", lambda event:Thread(target=ChooseImage, args=(event,)).start())

    list_group.grid(row=2, column=0, rowspan=3, columnspan=7, sticky=N+S+W+E, padx=4, pady=2)

    root.mainloop()