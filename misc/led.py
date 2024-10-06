import Jetson.GPIO as GPIO
import time

# Pin Definitons:
pinLeds = [29, 31, 33, 35]

def off_all():
    for pinLed in pinLeds:
        GPIO.output(pinLed, GPIO.LOW)


# on 1 led off all
def on_Led(pin int):
    # off_all()
    GPIO.output(pinLeds[pin], GPIO.LOW)

def init():
    GPIO.setmode(GPIO.BOARD)  # BOARD pin-numbering scheme
    for pinLed in pinLeds:
        GPIO.setup(pinLed, GPIO.OUT)

    