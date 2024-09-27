import Jetson.GPIO as GPIO
from time import sleep
in1 = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)
while True:
    GPIO.output(in1, GPIO.LOW)
    sleep(1)
    GPIO.output(in1, GPIO.HIGH)
    sleep(1)