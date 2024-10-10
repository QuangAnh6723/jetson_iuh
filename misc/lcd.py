from RPi_GPIO_i2c_LCD import lcd
from time import sleep

## Address of backpack
i2c_address = 0x27

## Initalize display

def padding_left(msg):
    l = len(msg)
    # print(type(l))
    a = (int)((20 - l))
    print(a)
    m1 =""
    for i in range(0, a):
        m1 += " "
    msg = msg + m1
    print(msg)
    return msg

def padding_center(msg):
    l = len(msg)
    # print(type(l))
    a = (int)((20 - l)/ 2)
    print(a)
    m1 =""
    for i in range(0, a):
        m1 += " "
    msg = m1 + msg + m1 +" " 
    print(msg)
    return msg

def padding_right(msg):
    l = len(msg)
    # print(type(l))
    a = (int)((20 - l))
    print(a)
    m1 =""
    for i in range(0, a):
        m1 += " "
    msg = m1 + msg +" "
    print(msg)
    return msg

def trai(msg:str, line:int):
    print("can trai")
    # print(len(qa))
    lcdDisplay.set(padding_left(msg),line)
    # lcdDisplay.set(padding_left(vy),2)
    # lcdDisplay.set(padding_left(hung),3)
    # lcdDisplay.clear()

def giua(msg:str, line:int):
    print("can giua")
    lcdDisplay.set(padding_center(msg),line)
    # lcdDisplay.set(padding_center(vy),2)
    # lcdDisplay.set(padding_center(hung),3)
    # lcdDisplay.clear()
    
def phai(msg:str, line:int):
    print("can phai") 
    lcdDisplay.set(padding_right(msg),line)
    # lcdDisplay.set(padding_right(vy),2)
    # lcdDisplay.set(padding_right(hung),3)
    # lcdDisplay.clear()
    
def init():
    lcdDisplay = lcd.HD44780(i2c_address)

