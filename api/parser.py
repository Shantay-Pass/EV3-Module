#import controller
import controller_ev3 as controller
from os import remove
from os.path import isfile
from time import sleep

def parse_instructions(instructions, iteration):
    print("Parsing instructions: {}".format(instructions))
    for instruction in instructions:
        if isfile('terminate'):
            remove('terminate')
            break

        parts = instruction.split(' ')
        if parts[0] == "mov":
            controller.move(int(parts[1]), int(parts[2]))
        elif parts[0] == "rot":
            controller.rotate(int(parts[1]), int(parts[2]))
        elif parts[0] == "say":
            controller.say(" ".join(parts[1:]))
        elif parts[0] == "pause":
            controller.pause(int(parts[1]))
        elif parts[0] == "loop":
            if iteration < int(parts[1]):
                parse_instructions(instructions, iteration + 1)
                return
        else:
            print("Illegal instruction: {}".format(parts[0]))
            #Invalid instruction
            pass
    remove('lock')
