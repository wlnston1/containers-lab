# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
    #  Please enter a letter from the alphabet (a-z or A-Z):
char = input("Enter a letter from the alphabet, A-Z ").lower()

# # 2. Write the code that determines whether the letter entered is a vowel
# if char in "aeiou":
#     print(f'The character {char} is a vowel')
# else:
#     print(f'The character {char} is a consonant')
    
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant
# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

if char in "aeiou":
    print(f'The character {char} is a vowel')
else:
    print(f'The character {char} is a consonant')




















# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase:

str = input("Please enter a word or phrase:")

# 2. Print the following message:
#      - What you entered is xx characters long
print(len(str))


# 3. Return to step 1, unless the word 'quit' was entered. 
if str == "quit":
    print(f'You entered the word "quit". Program will now exit.')

else:
    str = input("Please enter a word or phrase:")
    print(len(str))


















# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
# #      Input a dog's age in human years:
# age = int(input("How old is your doggo? "))



# # # 2. Calculates the equivalent dog years, where:
# # #      - The first two years count as 10 years each
# # #      - Any remaining years count as 7 years each

# # '''
# # if larger or eual to 2, sutract 2
# # if smaller than 3, times 10
# # '''

# dog_year = 0

# if age <= 2:
#     dog_year = age * 10 
# elif age > 2:
#     dog_year = 20 + (age - 2)*7
# # print(dog_year)

# # # (20)+(7*1)=
# # # (10+10)+(7*3)=51

# # # 3. Prints the answer in the following format:
# # #      The dog's age in dog years is xx
# # # Hint:  Use the int() function to convert the string returned from input() into an integer

# print("Your doggo's age in dog years is " + str(dog_year))

age = int(input("How old is your doggo? "))
dog_year = 0

if age <= 2:
    dog_year = age * 10 
elif age > 2:
    dog_year = 20 + (age - 2)*7

print(f"Your doggo's age in dog years is {dog_year}")

print("Your dog year", dog_year)


















# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:

# tri_1 = input("Enter the length of triangle side 1 ")
# tri_2 = input("Enter the length of triangle side 2 ")
# tri_3 = input("Enter the length of triangle side 3 ")

# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length

# if tri_1 == tri_2 and tri_2 == tri_3:
#      print("This is an equalateral triangle")
# elif tri_1 != tri_2 and tri_2 != tri_3 and tri_1 != tri_3:
#      print("This is a scalene triangle")
# else:
#      print("This is an isosceles triangle")


# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

# print("A triangle with sides " + tri_1 + tri_2 + "and" + tri_3 + "is a " +  "triangle" )

# if tri_1 == tri_2 and tri_2 == tri_3:
#      print("A triangle with sides of", tri_1, ",", tri_2, "&", tri_3, "is an equalateral triangle. All three sides are equal in length")
# elif tri_1 != tri_2 and tri_2 != tri_3 and tri_1 != tri_3:
#      print("A triangle with sides of", tri_1, ",", tri_2, "&", tri_3, "is a scalene triangle. All three sides are unequal in length.")
# else:
#      print("A triangle with sides of", tri_1, ",", tri_2, "&", tri_3, "is an isosceles triangle. Two sides are the same length.")


















# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.

# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.
# Hint: The next number is found by adding the two numbers before it

'''def fibonnaci(n):
    if n<=0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)


for i in range(50):
    print(fibonnaci(i), end=', ')'''



def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(50):
    print("term", i, "/ number:", fibonacci(i))









# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):
# month = input("Enter the month of the season (note: just the first three letters)").lower()



# 2. Then promptshtt the user to enter the day of the month:
#      Enter the day of the month:
# day = int(input("Enter the day of the month (note: please use two digits, e.g. 31)"))



# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# if month is "Dec" or "Jan" or "Feb" or "Mar" and between 



# 4. Print the result as follows:
#      <Mmm> <dd> is in <season>

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month_to_num = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12
}

month = input("Enter the month of the season (Jan - Dec): ")
day = int(input("Enter the day of the month: "))

month_num = month_to_num[month]

if month_num == 12 and day >= 21 or month_num == 1 or month_num == 2 and day <= 19:
    season = "Winter"
elif (month_num == 3 and day >= 20) or (month_num >= 4 and month_num <= 6 and day <= 20):
    season = "Spring"
elif (month_num == 6 and day >= 21) or (month_num >= 7 and month_num <= 9 and day <= 21):
    season = "Summer"
else:
    season = "Fall"

print("{} {} is in {}".format(month, day, season))


