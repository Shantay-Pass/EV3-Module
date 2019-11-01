from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveDifferential, SpeedRPM
from ev3dev2.wheel import EV3Tire
from ev3dev2.sound import Sound
from time import sleep

tank_drive = MoveDifferential(OUTPUT_A, OUTPUT_B, EV3Tire, 8 * 16)
sound = Sound()

def move(speed, mm):
    print("Moving with {}% speed for {} millimeters".format(speed, mm))
    #sleep(5)
    _move_tank(speed, mm)

def rotate(speed, degrees):
    print("Rotating {} degrees at {}% speed".format(degrees, speed))
    #sleep(5)
    _rotate_tank(speed, degrees)

def say(message):
    print("Say: {}".format(message))
    sound.speak(message)

def _move_tank(speed, mm):
    tank_drive.on_for_distance(speed, mm)

def _rotate_tank(speed, degrees):
    if degrees < 0:
        tank_drive.turn_left(speed, abs(degrees))
    elif degrees > 0:
        tank_drive.turn_right(speed, degrees)
