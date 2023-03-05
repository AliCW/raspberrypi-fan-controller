import schedule #package required to run the fan task at a set time(s)
import time #package required to gauge time itself for scheduled tasks
import subprocess #required to run tempreture command
import RPi.GPIO as GPIO #imports the RPi.GPIO library
from gpiozero import Button

fanPin = 14 #defines GPIO14 as the fan pin - as per internal connection

GPIO.setmode(GPIO.BCM) #sets the board mode for GPIO pinout
GPIO.setwarnings(False) #turns GPIO warnings off - required as you get a 'channel always in use' error without it
GPIO.setup(fanPin, GPIO.OUT) #defines the fan pin as an output pin

def fanOn():
    tempRaw = subprocess.check_output("vcgencmd measure_temp", shell=True).strip()
    tempString = tempRaw.decode("utf-8") #decodes the output into a string
    tempStrLeft = tempString.lstrip("btemop=")
    tempStrRight = tempStrLeft.rstrip("'C")
    temperature = float(tempStrRight)
    if temperature >= 60.0: 
        GPIO.output(14,True) #turns the fan on
    if temperature < 45.0: 
        GPIO.output(14,False) #turns the fan off
        
schedule.every(10).seconds.do(fanOn) #runs the fan_on task every ten seconds

while True:
    schedule.run_pending()
    time.sleep(1)

