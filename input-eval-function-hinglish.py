'''
input(): user se input lene keliye hota hai
         Lekin ye hamesha string return karta hai
'''

x = input("Enter a number: ")
print(x) # output: Enter a number: 3
print(type(x)) # output: <class 'str'>
# Note: Number bhi text ban jata hai

# Common mistake:
a = input("Enter first number: ") # output: Enter first number: 2
b = input("Enter second number: ") # output: Enter second number: 3
print(a + b) # output: 23
# Note: String add nahi hoti, join hoti hain (concatenation)

# Sahi Tareeka:
a = int(input("Enter first number: ")) # output: Enter first number: 2
b = int(input("Enter second number: ")) # output: Enter second number: 3
print(a + b) # output: 5
# Note: int() string ko number me convert karta hai

# Tricky concept(overwrite)
x = input("Enter a number: ") # output: Enter a number: 2
x = int(input("Enter a number: ")) # output: Enter a number: 3
print(x) # output: 3
print(type(x)) # output: <class 'int'>
# Note: Last value previous value ko replace kar deti hai

'''
eval(): input ko code ki tarah run karta hai 
        System commands run ho sakte hain
        Ye security risk hai
'''

x = eval(input("Enter something: "))
__import__('os').system('echo Hacked')


# Galat Tareeka eval() ko likhne ka
# Ye valid Python expression nahi hai
x = eval("Enter something: ") 
# output: Enter something: 5
#         Hacked

'''
Final Summary:
input() -> always string
int() -> convert to number
eval() -> executes code
'''