#!/bin/python3

import random

events = [
  ("You are beginning to smell.Would you like to take a shower?(type yes or no,then hit[ENTER]):",-200,0),
  ("You hear a hissing sound coming from a pipe.Would you like to investigate?(type yes or no,then hit[ENTER]):",-10,-500),
  ("A lump of ice has fallen from the sky nearby.Would you like to retrieve it?(type yes or no,then hit[ENTER]):",100,0),
  ("You watched a YouTube video about the best lawns in the solar system. Do you decide to try and grow a lawn in the desolate Martian soils?(type yes or no,then hit[ENTER]):", -300, -50),
  ("Your cousin Harold has mysteriously appeared. Do you invite nim to stay for one night?(type yes or no,then hit[ENTER]):", -200, -50),
  ("Today's food ration is very salty.Would you eat it?(type yes or no,then hit[ENTER]):", -5, 0),
  ("You spot an oasis off in the distance, do you investigate?(type yes or no,then hit[ENTER]):", -20, 0),
  ("Your knee hurts.Would you put some ice on it?(type yes or no,then hit[ENTER]):",-5,0)
         ]
print("[MARS WATER]\n---------------------------")
print("[CODED BY:RAY TANG]\n")
print("   This game is a text-based survival and sci-fi game,in which the player must make water-conscious decisions in order to survive for as long as possible without running out of water on Mars.In the beginning,you will start with 1000 liters of water.Thoughout the game,you will encounter various descicions that you will have to decide.To input your answer,type your answer and then press the [ENTER] key.Be careful,because if you don't choose wisely,you may end up using your water faster! \n GOOD LUCK,AND HAVE FUN!!! ;)") 
day=1
keepgoing=True
water = 1000
water_use=input("PLEASE ENTER HOW MANY LITERS OF WATER THAT YOU WILL DRINK IN A DAY:")
if water_use == "":
    print("PLEASE ENTER A NUMBER,NOTHING ELSE")
    water_use=input("PLEASE ENTER HOW MANY LITERS OF WATER THAT YOU WILL DRINK IN A DAY:")
while keepgoing:
    water=1000
    day=1
    while water > 0:
        water -= int(water_use)
        print("--------------------------------")
        print("[DAY",day,"]")
        print("--------------------------------")
        event=random.choice(events)
        while True:
          response=input(event[0]+"(yes/no):").lower()
          if response == "yes":
            water += event[1]
            break
          elif response == "no":
            water += event[2]
            break
          else:
            print("[PLEASE ANSWER WITH EITHER YES OR NO!]")
        day=day + 1
        print("[YOU HAVE",water,"LITERS OF WATER LEFT]")
    print("------------------------------------------------------------------")
    print("[GAME OVER]")
    print("[YOU RAN OUT OF WATER]")
    print("[YOU LASTED",day,"DAYS]")
    qwerty=input("TO PLAY AGAIN,PRESS[ENTER]KEY ANY OTHER KEY(PLUS ENTER)TO EXIT:")     
    keep_going=(qwerty == "")


