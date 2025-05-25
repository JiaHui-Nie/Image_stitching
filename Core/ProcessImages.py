from PIL import Image
import numpy as np

def MergeImages(filelist):
    current_arr = np.zeros((filelist[0][0].size[1], filelist[0][0].size[0], 3), 'uint8')
    current_aver = np.full((filelist[0][0].size[1], filelist[0][0].size[0]), 128, 'float64')

    for i in filelist:
        if i[0].mode != "RGB":
            img = i[0].convert("RGB")
        else:
            img = i[0]

        arr = np.array(img)
        aver = np.abs(arr.mean(axis=2)-128)

        operate = np.less(aver, current_aver)
        np.copyto(current_aver, aver, where=operate)
        operate = operate.repeat(3)
        operate.resize(arr.shape)
        np.copyto(current_arr, arr, where=operate)
    return Image.fromarray(current_arr)