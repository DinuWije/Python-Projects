"Author: Dinu Wijetunga"

import random
from time import sleep

def displayIntro():
  print('\nYou are the last hope for the human race.\n') 
  sleep(2)
  print("Prologue: \nDecades ago, the planet Earth became uninhabitable due to the spread of a deadly new virus.\nNations around the world scrambled for a cure, but it was too late.\nA private company, SpaceVentures decided that the only way to save hummanity was\nto send a spacecraft into the cosmos, searching for a new planet hummanity can call home. \nYou are the captain of that vessel.\n")
  print()
  name = input("What is your name?: ")
  print ("\nStardate: 03/25/2153\n")
  sleep(2)
  print("You wake up to alarms blaring around the ship. \n'%s Wake Up!' the familiar voice of your spaceships AI calls out. \n'We have a problem!' it says.\nThe ship is nearning a wormhole and I need you to tell me what action to take!" % (name)) 

def wormhole():
  print("'You need to decide whether to enter the wormhole or not! '")
  if difficulty == 'H':
    random_int1 = random.randint(1,6)
  else: 
    random_int1 = random.randint(1,12)
  wormhole = input("\nPress 1 to enter the wormhole or 2 to change course rapidly: ")
  if wormhole == "1":
    print("\nYou approach the wormhole...")
    sleep(2)
    if random_int1 <= 3:
      print("\nYour spaceship begins to shake violently.\nSuddenly, you hear a bang, then nothing.\nAll you feel is the cold emptiness of space as you run out of breath.")
    else:
      print('\nAfter what felt like an eternity, your spaceship makes it out of the wormhole')
      sleep(2)
      planets()
  else:
    print("\n'Thrusters at full blast, diverting around wormhole...'\n")
    sleep(2)
    if random_int1 <= 3:
      print("The ship overexters its thrusters, and they all shutdown.\nYou are left stranded in space forever.")
    else:
      print("You make it safely around the wormhole")
      sleep(2)
      planets()

def planets():
  print("\nStardate: 12/25/2155\n\n'Sensors have picked up a system of 3 habitable planets'")
  enter_system = input("'Do you want to invesitgate?'\nPress 'y' for YES or 'n' for NO: ")
  if enter_system == 'y' or enter_system == 'yes':
    print('\nYou approach three planets.')
    planet_choice = input("Which one would you like to land on? (enter 1, 2, or 3): ")
    chosen_planets(planet_choice)
  else:
    print("\nYou travel for another 100 years.\nYou find nothing more promising than the 3 planets you left behind.\nAs you die, the future of humannity dies with you.")

def chosen_planets(choice):
  if difficulty == 'H':
    random_int2 = random.randint(1,6)
  else: 
    random_int2 = random.randint(1,12)
  if choice == '1':
    print('Landing on Planet 1...\n')
    sleep(2)
    if random_int2 <= 6:
      print('As you land on the planet, you unknowingly land in a lake of lava.\nYour ship bursts into flames (with everyone on board)')
      print("Game Over")
    else:
      print("After decades of space travel you finally found a planet suitable for humans. \nYou now begin the long process of setting up a colony.")
      print("The End")
  elif choice == '2':
    print('Landing on Planet 2...\n')
    sleep(2)
    if random_int2 <= 3:
      print ('As you land on the planet, you are attacked by a primitive group of aliens, who catch you by suprise.\nYou are now dinner.')
      print("Game Over")
    else:
      print("After decades of space travel you finally found a planet suitable for humans. \nYou now begin the long process of setting up a colony.")
      print("The End")
  else:
    print('Landing on Planet 3...\n')
    sleep(2)
    if random_int2 <= 1:
      print ('As you land on the planet, you are attacked by a primitive group of aliens, who catch you by suprise.\nYou are now dinner.')
      print("Game Over")
    else:
      print("After decades of space travel you finally found a planet suitable for humans. \nYou now begin the long process of setting up a colony.")
      print("The End")


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
  difficulty = input("What difficulty would you like to play on? Press 'h' for hard, 'n' for normal: ")
  difficulty = difficulty.upper()
  displayIntro()
  wormhole()
  print('Do you want to play again? (yes or no)')
  playAgain = input()

