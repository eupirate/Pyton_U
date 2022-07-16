import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#version 1

#end of names list
end_list = (len(names) - 1)

picked_num = random.randint(0, end_list)
person_pay = names[picked_num]
print(f"{person_pay} is going to pay for the meal.")


# print(end_list)

#version 2
# pay_person = random.choice(names)

# print(f"{pay_person} is going to pay for the meal today.")

