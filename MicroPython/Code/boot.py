"""
boot.py
Author: Nick Damato
Team 71: Laser Harp
ECE 49022 Spring 2023
"""
# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

import uos
import os
from machine import SDCard

print('Root Directory:{}'.format(os.listdir())) #List items within the root directory of the ESP32 filesystem
os.mount(SDCard(slot=2), "/sd") #Initialize and mount an SD Card to the ESP32 filesystem
print('Root Directory:{}'.format(os.listdir())) #Relist items in the root directory to ensure that the SD card is shown
os.chdir('sd') #Change directory to the SD card
print('SD Card contains:{}'.format(os.listdir())) #List items in the root directory of the SD card