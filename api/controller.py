from os import remove
from os.path import isfile
from time import sleep

def move(speed, mm):
    print("Moving with {}% speed for {} millimeters".format(speed, mm))
    sleep(5)

def rotate(speed, degrees):
    print("Rotating {} degrees at {}% speed".format(degrees, speed))
    sleep(5)

def say(message):
    print("Say: {}".format(message))

def pause(seconds):
    print("Pausing for {} seconds".format(seconds))
    i = 0
    while i < seconds:
        if isfile('terminate'):
            remove('terminate')
            remove('lock')
            return
        sleep(1)
        i += 1