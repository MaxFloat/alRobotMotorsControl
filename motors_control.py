import os
#import pandas as pnd
import motor_driver as drv
import bot_model as mdl 

def move_forward(bot, k):
    w1 = bot.get_wheel_by_number(0)
    w2 = bot.get_wheel_by_number(1)
    for i in range(k):
        w1.step(1)
        w2.step(1)

def move_backward(bot, k):
    w1 = bot.get_wheel_by_number(0)
    w2 = bot.get_wheel_by_number(1)
    for i in range(k):
        w1.step(-1)
        w2.step(-1)

if __name__ == '__main__':
    move_forward(10)
    move_backward(10)