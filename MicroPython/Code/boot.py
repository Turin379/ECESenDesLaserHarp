# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

import uos
import os
from machine import SDCard

#print(uos.uname())
print('Root Directory:{}'.format(os.listdir()))
os.mount(SDCard(slot=2), "/sd")
print('Root Directory:{}'.format(os.listdir()))
os.chdir('sd')
print('SD Card contains:{}'.format(os.listdir()))