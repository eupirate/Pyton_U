import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

#player input
player_hand = int(input("Let's play, 1 is Rock, 2 is Paper, 3 is Scissors.\n" ))

#player assignment
if player_hand == 1:
 print("Player print" + rock)
elif player_hand == 2:
 print("Player print" + paper) 
else:
 print("Player print" + scissors) 

#Player logic
player_rock = 1
player_paper = 2
player_scissors = 3

#Machine input
machine_str = "Rock", "Paper", "Scissors" 
#machine assignment
#convert string to integer 
"Rock" == 1
"Paper" == 2
"Scissors" == 3
machine_num = 1, 2, 3
#machine random 
machine_ran = random.choice(machine_num)

if machine_ran == 1:
 print("machine print" + rock)
elif machine_ran == 2:
 print("machine print" + paper)
else:
 print("machine print" + scissors)


#draw logic
if player_hand == machine_ran:
 print("It's a draw")
#win logic 
elif player_hand == 1 and machine_ran == 3:
 print("You win!!")
elif player_hand == 2 and machine_ran == 1:
 print("You win!!")
elif player_hand == 3 and machine_ran == 2:
 print("You win!!")    
#lose logic
elif player_hand == 1 and machine_ran == 2:
 print("You lose!!")    
elif player_hand == 2 and machine_ran == 3:
 print("You lose!!") 
else:
 print("You lose!!")    