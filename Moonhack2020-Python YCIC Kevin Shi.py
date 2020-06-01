import random
import math

events = [
  ("You find a basket of food. Will you eat it?", "Eating the food replenished some of your energy! Energy +7%", 7, 0, 0),
  ("You find a basket of food. Will you eat it?", "The food was bad. Energy -3%, Water -1L", -3, -1, 0),
  ("You find a basket of food. Will you eat it?", "The food was packed with energy, but made you drink some water. Energy +30%, Water -2L", 30, -2, 0),
  ("You see a lump in the sand. Do you investigate?", "After some effort, you clear out the sand and find... nothing.  Energy -6%, Water -1L", -6, -1, 0),
  ("You see a lump in the sand. Do you investigate?", "You clear out the sand, but nothing was there. Energy -2%, Water -1L", -2, -1, 0),
  ("You see a lump in the sand. Do you investigate?", "With some diffculty, you pull out some materials. Energy -5%, Water -1L, Materials +3", -5, -1, 3),
  ("You see an oasis. Do you explore?", "It was farther than it looked, but you get a lot of water. Energy -10%, Water +25L", -10, 25, 0),
  ("You see an oasis. Do you explore?", "It was a mirage! What a waste of resources. However, you do manage to find some materials. Energy -8%, Water -5L, Materials +2", -8, -3, 2),
  ("You see a pile of materials in the distance, but it's really far away and you might not make it. Do you go?", "You head over and bring back the pile of materials. Energy -60%, Water -15L, Materials +35", -60, -15, 35)
  ]#format: info, text for yes, energy change, water change, materials change


while True:
  water = 250
  day = 0
  materials = 0
  energy = 100
  eventCheck = 0
  pluralSwap = "materials."
  print("You are stuck on Mars and need to gather materials to fix your ship. However, be sure to watch your water levels!")
  print("Each day, you use 4 liters of water. An expedition for materials takes 5% of your energy and a day of rest replenishes 25%")
  
  while water > 0 and materials < 150:
    day += 1
    if energy > 100:
      energy = 100  

    while True:
      if materials == 149:
        pluralSwap = "material."
      print("\nDay: "+str(day)+"; Water: "+str(water)+"L; Energy: "+str(energy)+"%")
      print("You need",str(150-materials),"more " + pluralSwap)
      choice = input("Would you like to explore and look for materials or rest for a day? (explore/rest) ").lower()
      if choice == "rest":
        water -= 4
        energy += 25
        break

      elif choice == "explore":
        energy -= 5
        water -= 4
        if random.random() > 0.35:
          eventCheck = 1
          event = random.choice(events)
          print("Answer yes or no.")

          while True:
            response = input(event[0]).lower()
            if response == "yes":
              print(event[1])
              energy += event[2]
              water += event[3]
              materials += event[4]
              break
            elif response == "no":
              print("You ignore it and move on.")
              break
            else:
              print("Please respond with yes or no!")

        else: eventCheck = 0
        randMatNum = math.floor(random.randint(0,2))
        if randMatNum == 2:
          print("You manage to find 2 more materials.")
        elif randMatNum == 1:
          print("You manage to find 1 more material.")
        elif eventCheck == 0: print("You didn't find anything today.")
        materials += randMatNum

        if energy <= 0:
          print("You ran out of energy! You made it back safely, but used up a huge amount of water. Water -100")
          energy = 50
          water -= 100
        break

      else: print("Please select one of the given options.")

  if water <= 0:
    playagain = input("\nYou ran out of water! You lasted " + str(day) + " days. Would you like to play again? Answer yes if you would.").lower()
  elif materials >= 150:
    playagain = input("\nYou found all of the materials and escaped! It took you " + str(day) + " days. Would you like to play again? Answer yes if you would.").lower()
  else:
    print("How did you get here?")
    playagain = "no"

  if playagain != "yes":
    break
  else: print("\n\n\n\n")