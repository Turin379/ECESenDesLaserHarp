# Spring 2023 ECE 49022 Sec 7: Laser Harp
Microcontroller: ESP32-WROOM-32D
Development Board: NodeMCU ESP-32S 
Development Framework: MicroPython v1.19.1
IDE: Thonny v4.0.2 running on Ubuntu 22.04.1

# Code Overview
boot.py - Code that executes when the ESP32 is powered on or reset. Initializes and mounts SD card to ESP32 filesystem. More initializing functionality to be added for other peripherals.

umidiparser.py - Reads MIDI files (SMF files) and gets all the MIDI events contained in the file. It also can return each event at the corresponding time. Does not contain a sound synthesizer, only the capabilities to read and interpret a MIDI file. Memory and CPU usage are optimized for a microcontroller with limited resources with Micropython. From https://github.com/bixb922/umidiparser

test.py - A temporary working .py file to test different peripherals for the ESP32 and to keep track of the GPIO pins utilized for the laser harp. I have mainly been using this to utilize the Python REPL (terminal) by sending individual lines of code to the ESP32 one-by-one to confirm SPI, GPIO, and UART functionality.
