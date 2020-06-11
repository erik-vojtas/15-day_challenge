print("Question 1:")
nope = False
zilch = 0
nada = []

print(bool(nada))
if (nope, zilch and nada):
    print("Stay positive!")
else:
    print("Do not be so negative!")

# The conditional evaluates a non-empty tuple which is "truthy"
# Although each item in the tuple is "falsely" (False, 0 and an empty list)
# the tuple itself evaluates to True.

print("----------------------------")
a, b = 0, 1

print("Question 2:")
def fibonacci(n):
    global a, b
    for _ in range(n):
        print(a)
        a, b = b, a + b
    return a

print(fibonacci(8))
# Answer:
# Error. This raises an UnboundLocalError – “a” & “b” are local variables,
# b is referenced before assignment (when a is assigned to b).
# Fix this using the “global” or initialise “a” & “b” inside the function scope.
print("----------------------------")

print("Question 3:")
values = [1,2,3,4,5]
even_num = [x for x in values if x % 2 == 0]
is_evens = [x % 2 == 0 for x in values]
print(even_num)
print(is_evens)
result = sum(is_evens)
print(result)
# Answer:
# 2. “bool” is a subtype of “int” (for quirky historical reasons - bit.ly/2Xy1ipI)
# so summing the list of bools is equivalent to summing a list of ints.

print("----------------------------")

print("Question 4:")
def add_to_list(*args, my_list=[]):
    my_list += args
    return my_list

x = add_to_list(1,2,3)
y = add_to_list(4,5,6)

print(x)
# Answer:
# [1,2,3,4,5,6] The default arg, “my_list”, is mutable,
# so it isn't instantiated with every function call
# Calling the fn twice adds the other args to the same list instance each time
# Don't use mutable types as default args!

print("----------------------------")

print("Question 5:")
seconds = 10

for i in range(seconds):
    --seconds

if seconds:
    print("Still waiting...")
else:
    print("You're done!")
# Answer
# “Still waiting…” Python does not have a decrement operator so line 4 has no effect. 
# It just gets parsed as two negative signs in a row, i.e. the equivalent of “-(-seconds).”

print("----------------------------")

print("Question 6:")
multipliers = [lambda x: (i+1)*x for i in range(5)]
def print_times_table(value):
    print([fn(value) for fn in multipliers])
    
print_times_table(2)
# Answer:
# [10,10,10,10,10] The L1 fns are closures: they have access to a variable from the enclosing scope
# that has completed its execution (the list comprehension). Py closures are late binding: their value
# is looked up at the time the closure is called. By the time the lambda fns are called the list comprehension
# has executed and i==4 so all the lamba fns return 10. Fix the code in question 6 by writing:
# multipliers = [lambda x, i=i: (i+1)*x for i in range(5)]. This forces the early binding of “i” as a default argument in the lambda fns.
# This works due to the behaviour we saw in Q4 - default args are created once, at the time the fn is created, rather than when it is called.

print("----------------------------")

print("Question 7:")
a = b = [1]
a += [2]
print(b)
a = a + [3]
print(b)
# Answer:
# [1,2] [1,2] The += operator on L3 uses the “__iadd__” method which modifies the list in place.
# L7 uses the “__add__” method which takes two parameters and returns their sum without modifying either.

print("----------------------------")

print("Question 8:")
a = b = "1"
a += "2"
print(a, b)
a = a + "3"
print(a, b)
# Answer:
#12 1 123 1. The += operator only uses the __iadd__ method if it exists.
# Strings are immutable so do not have __iadd__ therefore lines 3 and 7 are equivalent.

print("----------------------------")

print("Question 9:")
a = [[1,2,3], [4]]
# a = ([1,2,3], [4])
a[0] += [4]
print(a)
# Answer:
# Error. Tuples do not support item assignment so,
# while you can add an item to the list at position 0
# you cannot then assign that list to be item 0 in the tuple.
print("----------------------------")

print("Question 10:")
a = b = 500
print(a is b)

a -= 200
b -= 200
print(a is b)

a = a - 200
b = b - 200
print(a is b)
# Answer
# True False True. “a” & “b” start off referencing the same int object.
# After L4 & L5 they both reference different int objects with the same value,
# so no longer have reference equality. Python keeps an array of ints between -5 & 256
# When you create an int in that range you get a reference to a pre-existing object
# After L8&9, a& b reference the same object again!
print("----------------------------")