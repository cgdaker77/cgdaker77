import random as rand
from door import *

def run_game():

    # make the doors
    success = 0
    failure = 0

    for i in range(0,100):
        g = Game()
        result = g.run_game_stay()

        if result == 1:
            success += 1
        else:
            failure += 1

    print('success: ' + str(success))
    print('failures: ' + str(failure))
    print('ratio: ' + str(success/failure))
    print()

def run_game_switch():

    # make the doors
    success = 0
    failure = 0

    for i in range(0,100):
        g = Game()
        result = g.run_game_change()

        if result == 1:
            success += 1
        else:
            failure += 1

    print('success: ' + str(success))
    print('failures: ' + str(failure))
    print('ratio: ' + str(success/failure))
    print()

run_game()
run_game_switch()
