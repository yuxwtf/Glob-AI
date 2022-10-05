# Copyright - Yux
# Made With <3 By Yux

import time, os, colorama, random

	
class Utils:

    def CenterX(arg):
        return arg.center(os.get_terminal_size().columns)

    def CenterY(arg):
        for i in range(int(os.get_terminal_size().lines/5)):
            print('\n')
        return arg.center(0)

    def Center(arg):
        for i in range(int(os.get_terminal_size().lines/5)):
            print('\n')
        return arg.center(os.get_terminal_size().columns)

    def clear():
        os.system("cls" if os.name == "nt" else "clear")

    def colorclear():
        os.system(f'color 0F')
        Utils.clear()
        for i in range(200):
            print('')
        Utils.clear()



class COLORS:

    black = "0"
    blue = "1"
    green = "2"
    blue_gray = '3'
    red = "4"
    purple = "5"
    yellow = "6"
    white = "F"


class Loading:

    colorama.init()

    def bar(delay: int = 1, text: str = "pyload - bar load", textcolor=COLORS.black, background_color=COLORS.black):
        Utils.clear()
        percent_ascii = "██"
        percent = 0
        bar = ""
        while percent != 100:
            os.system(f'color {background_color}{textcolor}')
            time.sleep(delay)
            percent += 4
            Utils.clear()
            bar = str(bar) + str(percent_ascii)
            print(Utils.Center(str(text)))
            print('\n')
            print(Utils.CenterX(f'[{bar}] - ({percent}%/100%)'), flush=True, end="\r")
        Utils.colorclear()
        return

    def simple(duration: int = 1, text: str = "pyload - simple text load", textcolor=COLORS.black, background_color=COLORS.black):
        Utils.clear()
        duration_ = 0
        while duration_ < duration:
            os.system(f'color {background_color}{textcolor}')
            time.sleep(.1)
            Utils.clear()
            print(Utils.Center(str(text) + ""))
            time.sleep(.1)
            Utils.clear()
            print(Utils.Center(str(text) + "."))
            time.sleep(.1)
            Utils.clear()
            print(Utils.Center(str(text) + ".."))
            time.sleep(.1)
            Utils.clear()
            print(Utils.Center(str(text) + "..."))
            time.sleep(0.6)
            duration_ += 1
        os.system(f'color')
        Utils.colorclear()
        return


