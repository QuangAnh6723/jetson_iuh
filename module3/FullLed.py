import Jetson.GPIO as GPIO
import time

# Pin Definitons:
fullLed = [7, 11, 12, 13, 15, 16, 18, 19, 21, 22, 23, 24, 26, 29, 31, 32, 33, 35, 36, 37, 38, 40]
def main():
    # Pin Setup:
    GPIO.setmode(GPIO.BOARD)  # BOARD pin-numbering scheme
    for pin in fullLed:
        GPIO.setup(pin, GPIO.OUT)  # LED pin set as output

    for pin in fullLed:
        GPIO.output(pin, GPIO.LOW)

    print("Blink LED")
    
    while True:        
        for pin in fullLed:
            GPIO.output(pin, GPIO.LOW)
        time.sleep(1)

        for pin in fullLed:
            GPIO.output(pin, GPIO.HIGH)
        time.sleep(1)
	

main()
