# type casting: It is use to convert a value from one data type to another

# Basic Type Casting

# int to string
x = str(3)
print(x) # print the value after type casting
print('Data type of x', type(x)) # to show data type is changed

# string to int
y = int("24")
print(y) # print the value after type casting
print('Data type of y',type(y)) # to show data type is changed

# float to int
z = int(30.5)
print(z) # print the value after type casting
print(type(z)) # to show data type is changed

# int to float
a = float(2)
print(a) # print the value after type casting
print(type(a)) # to show data type is changed


# Ques: addd string and int
x = "2" # str
y = int(x) # int
print(y + 3)

# there are 2 types of Type casting
# Implicit Casting: python automatically converts data types when needed. For example int to float (Automatic Conversion)
# Explicit Casting: When we manually convert using functions like int(), float(), str() it is called explicit casting 
a = 5
b = 2.5
print(a+b)


# Advanced Type Casting

# list to tuple
f = tuple([1, 2, 3])
print(f)
print(type(f))

# tuple to list
e = list((1, 2, 3))
print(e)
print(type(e))

# list to set (remove duplicate values)
g = set([1, 1, 1, 2, 3, 3, 3])
print(g)


# Dictionary Casting

my_dict = {"name": 'Sundus', "marks": 78}

d = list(my_dict) # it will fetch the keys from the dictionary as an output
print(d)

t = list(my_dict.values()) # it will fetch the values from the dictionary as an output
print(t)

p = list(my_dict.items())
print(p) # it will fetch the key, value pairs from the dictionary as an output

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

# Tuple Immutable Trick

# tuple -> list -> tuple

my_tuple = (1, 2, 3) # create a tuple and assign values into it.
temp = list(my_tuple) # converting tuple into list (type casting)
temp[0] = 100 # modifying the values that is present inside the list (modification)
my_tuple = tuple(temp) # converting list into tuple (type casting)
print(my_tuple) # print the tuple as an output
print(type(my_tuple)) # check the data type of an output

# put comma after the single value inside tuple.
t = (40,)
print(t)
print(type(t))

# common error
print(int("hello"))

















