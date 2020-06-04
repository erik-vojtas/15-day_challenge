
# Iterator which takes 3 attributes: start, stop and step
class Counter():
    def __init__(self, start, stop, step):
        self.n = start
        self.stop = stop
        self.step = step

    def __next__(self):
        self.n += self.step
        if self.n >= self.stop:
            raise StopIteration
        return self.n

    def __iter__(self):
        return self

for c in Counter(0,10,3):
    print (c)


# Iterator which takes a list of items and iterate through them
class Iterator():
    def __init__(self,list_of_nums):
        self.list_of_nums = list_of_nums
        self.i = -1

    def __next__(self): #get next element in our list of numbers
        self.i += 1
        if self.i >= len(self.list_of_nums): # if our index is greater or equal to the length of our list then stop the iteration
            raise StopIteration
        return self.list_of_nums[self.i]

    def __iter__(self): # return an object with the __next__ method
        return self

list_of_nums = [1,3,5,7,9]
myIterator = Iterator(list_of_nums)
for x in Iterator(list_of_nums):
    print(x)

# Iterator which generates Fibonacci sequence of numbers

class FibSequence:
    def __init__(self, number_of_digits):
        self.number_of_digits = number_of_digits
        self.n1 = 0
        self.n2 = 1
        self.count = 0

    def __next__(self):
        temp = self.n1 + self.n2
        self.n2 = self.n1
        self.n1 = temp
        self.count += 1
        if self.count > self.number_of_digits:
            raise StopIteration
        return temp

    def __iter__(self):
        return self


fib = FibSequence(10)
for x in FibSequence(9):
    print(x)
print (next (fib) )
print (next (fib) )
print (next (fib) )
