# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# print(student_heights)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# [180 124 165 173 189 169 146]
# 156 178 165 171 187

total = 0
for height in student_heights:
    total += height
#print(f"The total height is {total}")

num_student = 0
for student in student_heights:
    num_student += 1
#print(f"The total student is {num_student}")

# avg_height = round(total / len(student_heights))
# print(f"The average height is {avg_height}")

avg_height = round(total / num_student)
#print(f"The average height is {avg_height}")
print(avg_height)