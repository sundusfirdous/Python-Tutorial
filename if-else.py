# if statement: It is used to check a condition. If the condition is True, the code inside it will execute

'''
Syntax:

if condition:
    # code to execute
'''
# Example:

age = 18

if age >= 18:
    print("You are eligible to vote") # output: You are eligible to vote

# if-else statement: It is used when we want to execute one block if the condition is True, and another block if it is False.

'''
Syntax:

if condition:
    # True block
else:
    # False block
'''


# Example:

num = 4

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# Example with User input:

num = int(input("Enter a number: "))

if num > 0:
    print('Positive number')
else:
    print('Negative number')

'''
 Important Points:
1. Indentation is very important in python
2. Condition must return True or False
3. else block runs only when if condition is False
'''

