# raspberrypi-fan-controller

This program serves to turn your 5v-fan on/off when the pi reaches a certain temperature. This is set to 60°c by default and will turn off when cooled to 45°c. The script utilizes a controlled infinte loop to consisitantly monitor the temperature every 10 seconds. It therefore should be setup so as to run when the pi is first turned on.

## Setup

There are numerous methods you can use, this is just the way i've applied it. You can use an S8050 transistor to communicate with the pi & control the fan.  The below schematic shows the basic layout, controls are applied via GPIO14.

![schematic](wiring_schematic.png)

## Adjusting settings

Alter the GPIO pin if GPIO14 is already in use.

    fanPin = 16

You can change the temperature which engages the fan by changing the if statements, the below example changes the script so the fan engages at 70°c.


    if temperature >= 70.0: 
        GPIO.output(14,True) #turns the fan on
    if temperature < 45.0: 
        GPIO.output(14,False) #turns the fan off