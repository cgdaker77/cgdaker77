import random as rd

class Door:
    has_car = False
    has_goat = False

    def __init__(self):
        has_car = False
        has_goat = False

    def set_car(self):
        has_car = True

    def set_goat(self):
        has_goat = True

class Game:
    doors = []
    goat_door_final = -1
    car_door_final = -1

    def __init__(self):

        # create three doors
        for i in range(0,3):
            self.doors.append(Door())

        self.car_door_final = rd.randint(0,2)
        self.doors[self.car_door_final].set_car()

        goat_door = self.car_door_final
        while (goat_door == self.car_door_final):
            goat_door = rd.randint(0,2)

        self.goat_door_final = goat_door
        self.doors[goat_door].set_goat()

    def run_game_stay(self):
        # make choice
        choice = rd.randint(0,3)

        if choice == self.car_door_final:
            return 1
        else:
            return -1

    def run_game_change(self):
        choice = rd.randint(0,3)

        while (choice == self.goat_door_final):
            choice = rd.randint(0,3)

        new_choice = rd.randint(0,3)
        while (new_choice == self.goat_door_final or new_choice == choice):
            new_choice = rd.randint(0,3)

        if new_choice == self.car_door_final:
            return 1
        else:
            return -1
