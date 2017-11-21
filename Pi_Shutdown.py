import RPi.GPIO as GPIO
import time 
import os 

GPIO.setmode(GPIO.BCM) #Defines how we name the GPIO pins
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP) #Define your GPIO pin

#Define the bash command to shutdown the Pi
def Shutdown(channel): 
    os.system("sudo shutdown -h now") 

#Describe when the function will execute 
GPIO.add_event_detect(18, GPIO.FALLING, callback = Shutdown, bouncetime = 2000) 

#Wait time
while 1: 
    time.sleep(1) 
