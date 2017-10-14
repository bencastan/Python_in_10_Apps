#import actors
import random

import time

from actors import Wizard, Creature, SmallAnimal, Dragon


def main():
    print_header()
    game_loop()


def print_header():
    print('----------------------')
    print(' WIZARD GAME APP')
    print('----------------------')
    print()


def game_loop() -> object:
    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 75, True),
        Wizard('Evil Wizard', 1000)
    ]
    hero = Wizard('Gandalf', 75)

    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared from a dark and foggy forrest...'
              .format(active_creature.name, active_creature.level))
        print()

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard runs and hides taking time to recover...")
                time.sleep(5)
                print("The wizard returns revitalised!!!")
        elif cmd == 'r':
            print('The wizard has become unsure of his power and flees!!!')
            time.sleep(6)
        elif cmd == 'l':
            print("The wizard {} takes in the suroundings and sees:"
                  .format(hero.name))
            for c in creatures:
                print(' * A {} of level {}'.format(c.name, c.level))
        else:
            print('OK, exiting game... bye!')
            break

        if not creatures:
            print("You defeated all the creatures!")
            break

if __name__ == '__main__':
    main()
