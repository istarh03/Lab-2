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
        self.__wallet = 3
        self.__coin = Coin()
        
    def toss_coin(self): 
        self.__coin.toss()

    def get_coin_side(self):
        return self.__coin.get_sideup()

    def win_coin(self):
        self.__wallet = self.__wallet + 1

    def lose_coin(self):
        self.__wallet = self.__wallet - 1

    def get_wallet(self):
        return self.__wallet

    def get_name(self):
        return self.__name