##the code is adapted from "https://gist.github.com/eyllanesc/f8464b57e091777a5aef48fdd9ea9067"

import RPi.GPIO as GPIO
import time

TRIG = 18
ECHO = 24

GPIO.setmode(GPIO.BCM)

print ("Distance Measurement In Progress")
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setwarnings (False)


isRunning = True
while isRunning:
    GPIO.output(TRIG, False)
    print ("Waiting For Sensor To Settle")
    time.sleep(2)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time() #measuring the time
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start #time taken for the echo to reach
    distance = pulse_duration * 17150 #changing the time to distance
    distance = round(distance, 2) #rounding of teh decimal to two decimal
    print ("Distance:", distance, "cm")
    if distance < 5: #this is for testing. we will be editing it in future so that every time teh meaurement is less than particluar value, it stores the data.
        print("testing")


GPIO.cleanup()

