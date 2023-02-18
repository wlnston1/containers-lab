
#! exercise 1
students = ["Winston", "Mia", "Helen", "Flora", "Tian-Shen"]
# print(students[1])
# print(students[-1])

#! exercise 2
'''Create a tuple named foods containing the same number of foods (strings) as there are names in the studentslist.
Use a forloop to print out the string "food goes here is a good food".'''
food = ["picanha", "bone", "mapotofu", "fish", "红烧肉"]
# for i in range(len(students)):
#     print(f"{food[i]} is a good food.")

for i in range(len(students)):
    print(f"{food[i]} is {students[i]}'s favorite dish.")

# food2 = ["burger", "hotdog", "soda", "fries"]
# for i in range(len(food)):
#     print(f"{food2[i]} is a good food, too!")

# chipotle = ["beef", "chicken", "steak", "barbacoa"]
# for i in range(len(food)):
#     print(f"welcome to chipotle, what kind of meat? {chipotle[i]}")


#! exercise 3
'''Using a forloop, print just the last two food strings from foods.'''
# for i in range(-2, len(food)):
#     print(food[i])

#! exercise 4
'''Create a dictionary named home_town containing the keys of city, state and population.
Print a string with this format: "I was born in city, state - population of population"'''
hometown = {"city": "Tianjin", "country": "China", "population": "13866000"}
city = hometown["city"]
country = hometown["country"]
population = hometown["population"]

print(f"I was born in {city}, {country} - population of {population}")


#! exercise 5
'''Iterate over the key: value pairs in home_townand print a string for each item, for example:'''
for key, value in hometown.items():
    print(f"{key}: {value}")

#! exercise 6
'''
Create an empty list named cohort.
Using a forloop, add one dictionary to the cohort list for each student name. Each dictionary should have this shape:
Iterate over cohortprinting out each element.
'''

students = ["Winston", "Helen", "Flora", "Tian"]
cohort = []

for student in students:
    fav_food = input(f"What is {student}'s favorite food? ")
    student_dict = {"student": student, "fav_food": fav_food}
    cohort.append(student_dict)

for student_dict in cohort:
    print(student_dict)


#! exercise 7
'''
Using the list of studentsand list comprehension, assign to a variable named awesome_studentsa new list containing strings similar to this:
["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
Iterate over awesome_studentsprinting out each string.
'''
students = ["Tina", "Fred", "Wilma"]
awesome_students = [f"{student} is awesome!" for student in students]
print(awesome_students)


#! exercise 8
'''
Using the tuple foods and list comprehension within a forloop, print each food string that contains the letter a.
'''
foods = ("apple", "doughnut", "carrot", "avocado")
for food in foods:
    if "a" in food:
        print(food)