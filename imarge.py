# 同じディレクトリ内部の画像を名前の早い順に二枚縦に合成する

from PIL import Image
import os

def marg_v(im1, im2):
    dst = Image.new("RGB", (im1.width, im1.height + im2.height))
    dst.paste(im1, (0,0))
    dst.paste(im2, (0, im1.height))
    return dst

PATH = "."
im = []
count = 0

dir_list = os.listdir(PATH)
for i in dir_list:
    if ("png" in i or "jpg" in i) and count <= 1:
        im.append(Image.open(i))
        count += 1

marg_v(im[0], im[1]).save("HOGE.png")
