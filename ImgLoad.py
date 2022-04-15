# -*- coding: utf-8 -*-
# @Time    : 2022/4/15 09:33
# @Author  : Kenny Zhou
# @FileName: ImgLoad.py
# @Software: PyCharm
# @Email    ：l.w.r.f.42@gmail.com

def load_img():
	with open("binary.out", "rb") as file:
		buf = bytearray(file.read())
		file.close()
		return buf
