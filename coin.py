"""
Program Name: Match Game
Author: Istar Hagi
Purpose: Coin class for a coin that can be tossed.
Starter Code: None
Date: October 7, 2026
"""

import random


class Coin:
    def __init__(self):
        self.__sideup = "Heads"

    def toss(self):
        number = random.randint(0, 1)
        if number == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        return self.__sideup
