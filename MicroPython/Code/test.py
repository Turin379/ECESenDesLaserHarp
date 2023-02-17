"""
test.py
Author: Nick Damato
Team 71: Laser Harp
ECE 49022 Spring 2023
"""
import uos
import usys
import os
from machine import Pin, SDCard
import time
"""
Pins:
    
    SD Card:
      MISO -> GPIO 19
      MOSI -> GPIO 23
      SCK  -> GPIO 18
      CS   -> GPIO 5
    MIDI Out:
      UART_TX0 -> GPIO 1
"""
# This is a working .py file to test different peripherals for the ESP32 and to keep track of the GPIO pins utilized for the laser harp.
# I have mainly been using this to utilize the Python REPL (terminal) by sending individual lines of code to the ESP32 one-by-one to confirm SPI, GPIO, and UART functionality.