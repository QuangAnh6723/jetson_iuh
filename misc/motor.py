
# import Jetson.GPIO as GPIO
import time
from misc.config import *


__in1 = 7
__in2 = 11
__in3 = 13
__in4 = 15

def m1_thuan():
    GPIO.output(__in1, GPIO.LOW)
    GPIO.output(__in2, GPIO.HIGH)
    
def m1_ngich():
    GPIO.output(__in1, GPIO.HIGH)
    GPIO.output(__in2, GPIO.LOW)
    
def m2_thuan():
    GPIO.output(__in3, GPIO.LOW)
    GPIO.output(__in4, GPIO.HIGH)

def m2_ngich():
    GPIO.output(__in3, GPIO.HIGH)
    GPIO.output(__in4, GPIO.LOW)

def m1_stop():
    GPIO.output(__in3, GPIO.LOW)
    GPIO.output(__in4, GPIO.LOW)
    
def m2_stop():
    GPIO.output(__in1, GPIO.LOW)
    GPIO.output(__in2, GPIO.LOW)

def menu():
    print("0. M1 va M2 ngung")
    print("1. M1 quay thuan")
    print("2. M2 quay thuan")
    print("3. M1 va M2 quay ngich")
    # print("4. M1 quay thuan")

def go(m:int, dir: int):
    print(go.__name__ + ' motor ' + str(m) + ' dir ')
    if m == 1:
        if dir == CW:
            m1_thuan()
        elif dir == CCW:
            m1_ngich()
        else:
            m1_stop()
    elif m == 2:
        if dir == CW:
            m2_thuan()
        elif dir == CCW:
            m2_ngich()
        else:
            m2_stop()


def init():
    GPIO.setmode(GPIO.BOARD)  # BOARD pin-numbering scheme
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)
    GPIO.setup(in3, GPIO.OUT)
    GPIO.setup(in4, GPIO.OUT)

    