
#exercise 1
'''write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.'''


def sum_to(n):
    return sum(range(1, n+1))

result = sum_to(6)
print(result)  # Output: 15



#exercise 2
'''Write a function named largestthat takes a list of numbers as an argument and returns the largest number in that list.'''
#Write a function named largestthat takes a list of numbers as an argument and returns the largest number in that list.
def largest(numbers):
    if not numbers:
        return None
    else:
        return max(numbers)

numbers = [1, 2, 3, 400, 5]
result = largest(numbers)
print(result)


# exercise 3
''' Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string.
 For example, the call occurances("fleep floop", "e") should return 2.
 You may not use the count method in your solution.'''

def occurances(string1, string2):
    count = 0
    for i in range(len(string1)):
        if string1[i] == string2:
            count += 1
    return count

print(occurances("fleep floop", "e"))




# exercise 4
'''Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product.
(Hint: Review your notes on *args).'''

def product(*args):
    product = 1
    for i in args:
        product *= i
    return product

print(product(1, 2, 3, 4, 5))