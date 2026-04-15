# if Statement: Ek condition check karta hai. Agar condition True hoti hai, tabhi code run hota hai.
'''
Syntax:
if condition:
    # code chalega
'''

# Example: 
age = 18

if age >= 18:
    print('Aap vote de sakte hai')

# if-else statement: Agar condtion True ho to ek block chalega, aur agar condition False ho to doosra block chalega.

'''
Syntax:
if condition:
    # True wala code chalega
else:
    # False wala code chalega
'''

# Example:

age = 20

if age >= 18:
    print('Aap vote de sakte hai')
else:
    print('Aap vote nhi de sakte hai')

# User input example:

num = int(input("Ek number enter karo: "))

if num > 0:
    print("Positive number")
else:
    print("Negative number")

'''
 Important Points:
 1. Python me indentation bahut important hai
 2. Condition True ya False honi chahiye
 3. else tabhi chalega jab if False hoga
 '''