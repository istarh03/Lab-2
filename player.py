"""
Program Name: Match Game
Author: Istar Hagi
Purpose: Player class with a name, a wallet, and a coin.
Starter Code: None
Date: October 7, 2026
"""

from coin import Coin


class Player:
    def __init__(self, name):
        self.__name = name
        self.__wallet = 20
        self.__coin = Coin()

   