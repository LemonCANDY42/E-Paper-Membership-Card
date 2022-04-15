# -*- coding: utf-8 -*-
# @Time    : 2022/4/15 09:09
# @Author  : Kenny Zhou
# @FileName: ImgBuilt.py
# @Software: PyCharm
# @Email    ：l.w.r.f.42@gmail.com
from PIL import Image, ImageOps

# width = 64
# height = 90

img = Image.open('E-Paper-orin.bmp', 'r')
im_flip = ImageOps.flip(img)


# im_flip.save('E-Paper.bmp', 'BMP')
def build_img():
	with open("E-Paper-orin.bmp", "rb") as file:
		buf = img.convert('1').tobytes()
		# buf = buf.replace(b'\x00', b'\xfe')
		# buf = buf.replace(b'\xff', b'\x00')
		# buf = buf.replace(b'\xfe', b'\xff')
		with open('binary.out', 'wb') as out:
			out.write(buf)
			out.close()


build_img()
# img.resize((width, height))
# with open('binary.out', 'wb') as out:
# 	out.write(img.convert('1').tobytes())
# 	out.close()
