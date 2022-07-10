#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

print('''
********************************      
   _______
  /\ o o o\
 /o \ o o o\_______
<    >------>   o /|
 \ o/  o   /_____/o|
  \/______/     |oo|
        |   o   |o/
        |_______|/
********************************
      ''')

import random

#version 1
'''
user_input = int(input("Pick a random number from 0 - 10 inclusive. "))
#random generator
ran_cal = user_input / 13
rand_output = round((ran_cal),1)
if rand_output > 0 and rand_output < 0.5:
    print("Heads")
else:
    print("Tails")
'''
#version 2
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number (1 - 10): "))
random = random.randint(0, 1)
 # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
#Write the rest of your code below this line 👇
if random == 1:
    print("Heads")
else:
    print("Tails")
