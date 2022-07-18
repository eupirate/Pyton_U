print('''*******************************
 _            _   
| |          | |  
| |_ ___  ___| |_ 
| __/ _ \/ __| __|
| ||  __/\__ \ |_ 
 \__\___||___/\__|
*******************************''')
  
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
navigation = input("Which direction would you take? Left or Right? \n").lower()

if navigation == "left":
 action = input("What action are you taking? Swim or Wait? \n").lower()
 if action == "wait":
    door = input("Which door would you pick? Red Blue or Yellow? \n").lower()
    if door == "yellow":
     print("Yellow door, you win!!!")
    elif door =="red":
     print("Red door, Game Over!!!")
    elif door == "blue":
     print("Blue door, Game Over!!!")
    else:
        print("No door like that, Game Over!!!")
 else: 
     print("Game Over!!")
else:
 print("Game Over!")     
    
    