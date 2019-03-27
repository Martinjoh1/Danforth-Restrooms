#the code for ultrasonic sensor is adapted from "https://gist.github.com/eyllanesc/f8464b57e091777a5aef48fdd9ea9067"
import RPi.GPIO as GPIO
import time
from datetime import datetime #
from datetime import date


class ProjectTwo(object):
    "the class for the  project to meausre the distance and based on teh distance meaured it stores the date"
    def __init__(self):
        GPIO.setwarnings(False)
        self.TRIG = 18 #defining the pins
        self.ECHO = 24 #defining the pins
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)
        self.distance = 0
        self.myfile = open("indreswaranl.csv", "a+")  #to create a csv file
        #self.myfile.write("Date" + ","+"Time"+","+"\n")# to name the rows

    def find_distance(self):
        isRunning = True
        GPIO.output(self.TRIG, False)
        time.sleep(.8)
        GPIO.output(self.TRIG, True)
        time.sleep(0.00001)
        GPIO.output(self.TRIG, False)
        while GPIO.input(self.ECHO) == 0:
            pulse_start = time.time() #measuring the time
        while GPIO.input(self.ECHO) == 1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start #time taken for the echo to reach
        self.distance = pulse_duration * 17150 #changing the time to distance
        self.distance = round(self.distance, 2) #rounding of the decimal to two decimal
        #print (self.distance)
        #return self.distance

    def write_file(self): 
        #for creating a file and storing data
        #due to the location where we placed the pi, the sound waves always reach the wall which is 97cm away from the pi and considering the door can
        #not be opened neyod a certain distnce we wanted to filter the data below 89cm
        if self.distance < 89:
                #for our project, we want to store the data only when the distance meaured by the
                #sensor is less than 89cm so that we know people entered the restroom.               #we are using 5cm here    
            self.myfile.write (str(date.today())+ "," + str(datetime.time(datetime.now())) + "," + "\n")# save the data in the file created above in two columns
            self.myfile.close()

def main():
    
    while True:
        dist = ProjectTwo()
        dist.find_distance()
        dist.write_file()
        
        
    GPIO.cleanup()

main()
        
