'''
Operators: Operators are special symbols used to perform operations on variables and values

Types of Operators:
1. Arithmetic
2. Comparison
3. Logical
4. Assignment
5. Membership
6. Identity
'''

# Arithmetic Operators: Used for mathematical calculation

a = 10
b = 5
# a, b -> Operands
# +, - ,* % etc -> Operators

print(a + b) # addition
print(a - b) # subtraction
print(a * b) # multiplication
print(a / b) # division
print(a % b) # modulus (remainder)
print(a ** b) # exponent (power)
print(a // b) # floor division (quotient)

# 2. Comparison Operators: Used to compare values & return True or False
a = 10
b = 5

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# 3. Logical Operators: Used to combine conditions (and, or , not)

x = True
y = False
print(x and y)
print(x or y)
print(not y)

# 4. Assignment Operators: Used to assign & update values

a = 10
a += 5 # a = a + 5
a -= 2 # a = a - 2
a *= 2 # a = a * 2
a /= 2 # a = a * 2

# 5. Membership Operators: Used to check if a value exists in a sequence (in, not in)

# list 
list1 = [1, 2, 3]

print(2 in list1)
print(5 not in list1)

# Dictionary
student = {"name": 'Sundus', "marks": 77}
print("name" in student)
print("Sundus" in student)

print("Sundus" in student.values())
print(("name", "Sundus") in student.items())

# 'in' operator in dictionary always checks the key by default

# set
my_set = {10, 20, 30}
print(50 not in my_set)
print(20 in my_set)

# tuple
my_tuple = (10, 20, 30)
print(20 not in my_tuple)
print(20 in my_tuple)

# 6. Identity Operators: Used to compare memory locations (is, is not)

a = [1, 2, 3]
b = a

print(a is b)
print(a is not b)

'''
Important Tips

'==' compare values
'is' compares memory locations
'''




















