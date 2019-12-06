from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveDifferential, SpeedRPM
from ev3dev2.wheel import EV3EducationSetRim
from ev3dev2.sound import Sound
from os import remove
from os.path import isfile
from time import sleep

tank_drive = MoveDifferential(OUTPUT_A, OUTPUT_B, EV3EducationSetRim, 250)
sound = Sound()

def move(speed, mm):
    print("Moving with {}% speed for {} millimeters".format(speed, mm))
    _move_tank(speed, mm)

def rotate(speed, degrees):
    print("Rotating {} degrees at {}% speed".format(degrees, speed))
    _rotate_tank(speed, degrees)

def say(message):
    print("Say: {}".format(message))
    sound.speak(message)

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

def _move_tank(speed, mm):
    tank_drive.on_for_distance(speed, mm)

def _rotate_tank(speed, degrees):
    if degrees < 0:
        tank_drive.turn_left(speed, abs(degrees))
    elif degrees > 0:
        tank_drive.turn_right(speed, degrees)