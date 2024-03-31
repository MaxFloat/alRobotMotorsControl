import os
#import pandas as pnd
import motor_driver as drv
import bot_model as mdl 

def move_forvard(bot, k):
    w1 = bot.get_wheel(0)
    w2 = bot.get_wheel(1)
    for i in range(k):
        w1.step(1)
        w2.step(1)

def move_backward(bot, k):
    w1 = bot.get_wheel(0)
    w2 = bot.get_wheel(1)
    for i in range(k):
        w1.step(-1)
        w2.step(-1)

if __name__ == '__main__':
    move_forvard(10)
    move_backward(10)