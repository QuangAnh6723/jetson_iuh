
import Jetson.GPIO as GPIO
import time

# Pin Definitons:
pinLeds = [29, 31, 33, 35]

in1 = 7
in2 = 11
in3 = 13
in4 = 15

def onLed(num: int):
    GPIO.output(num, GPIO.HIGH)
    for i in pinLeds:
        if i == num:
            GPIO.output(num, GPIO.LOW)


def m1_thuan():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    
def m1_ngich():
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    
def m2_thuan():
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)

def m2_ngich():
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)

def m1_stop():
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    
def m2_stop():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)

def menu():
    print("0. M1 va M2 ngung")
    print("1. M1 quay thuan")
    print("2. M2 quay thuan")
    print("3. M1 va M2 quay ngich")
    # print("4. M1 quay thuan")

def main():
    GPIO.setmode(GPIO.BOARD)  # BOARD pin-numbering scheme
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)
    GPIO.setup(in3, GPIO.OUT)
    GPIO.setup(in4, GPIO.OUT)

    for pinLed in pinLeds:
        GPIO.setup(pinLed, GPIO.OUT)
    
    while True:
        menu()
        key = input("nhap vao: ")
        
        if key == '1':
            print('nhan so 1')
            m1_thuan()
            onLed(1)
        elif key == '2':
            print('nhan so 2')
            m2_thuan()
            onLed(2)
        elif key == '3':
            print('nhan so 3')
            m1_ngich()
            m2_ngich()
            onLed(3)
        # elif key == '4':
        #     print('nhan so 4')
        elif key == '0':
            print('nhan so 0')
            m1_stop()
            m2_stop()
            onLed(0)
        else:
            print("========================= nhan sai")
        
        
if __name__ == '__main__':
    main()
