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
    # Portrait
    epd = EPD_2in9_Portrait()
    epd.Clear(0xff)
    epd.fill(0xff)

    epd.buffer = load_img()
    epd.display(epd.buffer)
    epd.delay_ms(2000)

    epd.init()

    epd = EPD_2in9_Portrait()

    epd.Clear(0xff)
    epd.fill(0xff)

    epd.text("Token: 3", 32, 130, 0x00)
    epd.display(epd.buffer)

    epd.delay_ms(5000)

    epd.init()
    epd.Clear(0xff)
    epd.delay_ms(2000)
    print("sleep")
    epd.sleep()

    # epd = EPD_2in9_Landscape()
    # epd.Clear(0xff)
    #
    # epd.fill(0xff)
    #
    # epd.display(load_img())
    # epd.delay_ms(2000)
    #
    #
    # for i in range(0, 10):
    #     epd.fill_rect(40, 270, 40, 10, 0xff)
    #     epd.text(str(i), 60, 270, 0x00)
    #     epd.display_Partial(epd.buffer)

    epd.init()
    epd.Clear(0xff)
    epd.delay_ms(2000)
    print("sleep")
    epd.sleep()

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
    led = Pin(25, Pin.OUT)
    led.on()
    test()
    led.off()
