# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#***********************************
''' version 1
position_x = int(position[0])
position_y = int(position[1])


selected_row = map[position_y - 1]
selected_row[position_x -1] = "X"
#***********************************
'''
#***********************************
'''
#version 2
position_x = int(position[0])
position_y = int(position[1])

locate_x = map[position_x - 1]
locate_x[position_y - 1] = "$"
#***********************************
'''
#***********************************

#version 3

position_x = int(position[0])
position_y = int(position[1])

map[position_x - 1][position_y - 1] = "$"


#***********************************

#Write your code above this row 👆

# 🚨 Don't change the code below 👇

print(f"{row1}\n{row2}\n{row3}")
