# Advanced Data Types
'''
 1. List: A list is a collection where we can store multiple values. 
          A list can have multiple data type (heterogeneous).
          List are Ordered and Mutable, meaning we can change values.
          List can be accesed by Indexing
'''
# Create a list and assign values into it.
my_list = [10, 20, 30, 40, 'Sundus', 20.1, True]
print(my_list)

# Change value present inside the list with the help of Indexing
my_list[0] = 1000
print(my_list)

# Use Indexing to access value present inside List
print(my_list[4])

'''
2. Tuple: A tuple is a collection where we can store multiple values.
          A tuple is Ordered. 
          A tuple can have multiple data type (heterogeneous).
          Tuple can be accesed by Indexing
          A single-element tuple needs a comma; otherwise, it’s not a tuple and is treated as a normal value (e.g., int, string, etc.). 
          We cannot change values in a tuple, it is immutable.
'''
# Create tuple and assign value to it
my_tuple = (10, 20, 30, 40, 'Sundus', 44.0, True)
print(my_tuple)

# Use indexing to access a value present inside tuple 
print(my_tuple[4])

# Use ',' at the end of the single value present inside tuple 
my_tuple = (40,)
print(my_tuple)
print(type(my_tuple))

# This will give an error because tuple is immutable.

'''
 3. Set: A set is a collection where we can store multiple values.
         It can have multiple data type (heterogenous)
         A set is unordered, meaning indexing is not supported.
         A set is mutable, so we can add or remove values.
         Set does not allow duplicate values.
'''

my_set = {10, 10, 10, 20, 30, 30, 40, 'Sundus', 44.2, True, True}
print(my_set)

# This will give an error because Set does not support Indexing
my_set[0] = 100
print(my_set)

# Using .add() to add a new value inside the set
my_set.add(100)
print(my_set)

# Using .remove() to remove value from the set
my_set.remove(20)
print(my_set)

'''
4. Dictionary: A dictionary is a collection of key-value pairs.
            Key must be unique.
            We can access values using keys
            Dictionary is ordered.
'''
my_dict = {"name": 'Sundus',"name": 'Priya', "marks": 89.1, "is_student": True}

print(my_dict)

print(my_dict['marks'])
print(my_dict['name'])


