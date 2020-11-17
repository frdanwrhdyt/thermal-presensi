import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def shutdown(channel):
    print('Shutting Down')
    time.sleep(1)
    os.system('sudo shutdown -h now')


time.sleep(20)
#os.system('sudo date -s "$(wget -qSO- --max-redirect=0 google.com 2>&1 | grep Date: | cut -d' ' -f5-8)Z"')
GPIO.add_event_detect(21,GPIO.FALLING, callback = shutdown, bouncetime = 2000)

while True:
    time.sleep(1)