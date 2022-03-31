import random

from src.die import Die
from src.hand import Hand


def main():
    dice = [Die(random.randint) for _ in range(5)]
    hand = Hand(dice)
    hand.throw_all()
    while True:
        print(hand)
        dice_to_reroll = input("Reroll? ")
        hand.throw(dice_to_reroll)


if __name__ == "__main__":
    main()
