# -*- coding: utf-8 -*-
# @Time    : 2022/4/14 15:26
# @Author  : Kenny Zhou
# @FileName: main.py
# @Software: PyCharm
# @Email    ：l.w.r.f.42@gmail.com

import time

from ImgLoad import load_img
from ePaper import *


def led():
    led = Pin(25, Pin.OUT)

    while True:
        led(1)
        time.sleep(1)
        led(0)
        time.sleep(1)


def test():
    # # Portrait
    # epd = EPD_2in9_Portrait()
    # epd.Clear(0xff)
    #
    # epd.fill(0xff)
    #
    # epd.text("Kenny Zhou", 5, 10, 0x00)
    # epd.text("Pico_ePaper-2.9", 5, 20, 0x00)
    # epd.text("Raspberry Pico", 5, 30, 0x00)
    # epd.display(epd.buffer)
    # epd.delay_ms(2000)

    epd = EPD_2in9_Portrait()
    epd.Clear(0xff)

    epd.fill(0xff)

    epd.display(load_img())
    epd.delay_ms(2000)

    # epd.sleep()

    # epd.text("Kenny Zhou", 5, 10, 0x00)
    # epd.text("Pico_ePaper-2.9", 5, 20, 0x00)
    # epd.text("Raspberry Pico", 5, 30, 0x00)

    # epd.display(epd.buffer)
    # epd.delay_ms(2000)


if __name__ == "__main__":
    # led = Pin(25, Pin.OUT)
    # led.value(0)
    # pass
    test()
