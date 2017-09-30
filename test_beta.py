from pyA20.gpio import gpio
from pyA20.gpio import port

#import RPi.GPIO as GPIO
import dht22
import time
import datetime

# initialize GPIO
#gpio.setwarnings(False)
#gpio.setmode(GPIO.BCM)
PIN2 = port.PA6
gpio.init()
#gpio.cleanup()


# read data using pin 14
instance = dht22.DHT22(pin=PIN2)

print("Start program")
i = 0

while True:
    result = instance.read()
    if result.is_valid():


        while i < 10 :
            list_temp = []
            list_temp = [%.2f]
            list_hum = []
            list_hum.append(%.2f %)
            print list_temp
            print list_hum
            i = i +1
            time.sleep(15)


       #print("Horodatage: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
       #print("Temperature: %.2f C" % result.temperature)
       #print("Humidity: %.2f %%" % result.humidity)
        
        #fichier = open("data.txt", "w")
        #fichier.write("Horodatage: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        #fichier.write("\nTemperature: %.2f C" % result.temperature)
        #fichier.write("\nHumidite: %.2f %%" % result.humidity)
        #fichier.close()

    time.sleep(1)