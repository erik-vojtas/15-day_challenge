# A generator is a function that returns an object (iterator) which we can iterate over (one value at a time).
# • As easy as defining a normal function with yield statement instead of a return statement.
# • When called, it returns an object (iterator) but does not start execution immediately.
# • Local variables and their states are remembered between successive calls.

def mygen():
    yield("C")
    yield("G")
    yield("A")
    yield("T")

gen = mygen()
print (next(gen))
print (next(gen))

# for c in gen:
#     print (c)

print(list(gen)) # use “list” function to collect all the values returned by the generator
print("-------------------------")



# Write a generator function “myrange” to replicate the behavior of the range function

def myRange(start, end, step):
    x = start
    while x <= end:
        yield x
        x += step

for c in myRange(0, 10, 3):
    print(c)
print("-------------------------")

# • Write a Python Generator called RandomEven, which generates a sequence of random even numbers between 1 and 100.
# • The number of items to be generated is given as input parameter
import random

def RandomEven(num_of_digits):
    c = 0
    while c < num_of_digits:
        n = random.randint(1, 100)
        if n % 2 == 0:
            c += 1
            yield (c,n)

for c in RandomEven(15): # generate 12 numbers
    print(c)
print("-------------------------")