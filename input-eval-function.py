'''
input(): It is used to take user input.
         But it always return data in string format
'''
x = input("Enter a number: ")
print(x)
print(type(x))
# Note: Numbers are treated as text

# Common Mistake:
a = input("Enter first number: ") # output: Enter first number: 2
b = input("Enter second number: ") # output: Enter second number: 3
print(a + b) # output: 23
#  Note: String don't add, they concatenate (join)

# Correct Approach:
a = int(input("Enter first number: ")) # output: Enter first number: 2
b = int(input("Enter second number: ")) # output: Enter second number: 3
print(a + b) # output: 5
# Note: int() coverts string -> integer

# Tricky concept (overwriting)
x = input("Enter a number: ") # output: Enter a number: 2
x = int(input("Enter a number: ")) # output: Enter a number: 3
print(x) # output: 3
print(type(x)) # output: <class 'int'>
# Note: Latest value overwrites previous value

'''
eval(): It execute input as python code.
        It can run system commands.
        It is a security risk
'''
x = eval(input("Enter something: "))
__import__('os').system("echo Hacked")
# output: Enter something: 5
#         Hacked

# Incorrect way to write eval()
x = eval("Enter something: ")
# Note: eval() need valid Python expression, not plain text

'''
Final Summary:
input() -> always string
int() -> convert to number
eval() -> executes code
'''

