'''
ASCII Guessing Game
Andrew Conte
'''

import random

def print_treasure_map():
    '''  Print an ASCII treasure map.'''
    print(
        '''
         _____
        |    |
        |    |
        |  X |   ----> Treasure
        |    |
        |    |
        ------
        '''
    )

def play_game():
    print("Welcome to the ACSII Treasure Hunt!")
    print_treasure_map()
    print("The Treasure is hidden behind a number between 1 and 100")

    treasure_number= random.randint(1, 100)
    attempts = 7 # Limit the number of attempts

    while attempts > 0:
         print(f"\nYou have {attempts} attempts remaining.")
         attempts = 0

if __name__ == "__main__":
      play_game()