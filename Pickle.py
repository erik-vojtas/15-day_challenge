# • The pickle module implements binary protocols for serializing and de-serializing a Python object structure.
# • Pickling (and unpickling) is alternatively known as “serialization”, “marshalling,” or “flattening”

# Serialization : Serialization is a mechanism of converting the state of an object into a byte stream, JSON, YAML, XML.
# JSON and XML are two of the most commonly used serialization formats within web applications.
# Deserialization : It is the reverse process where the byte stream is used to recreate the actual object in memory.

import pickle

# take user input to take the amount of data
number_of_data = int(input('Enter the number of data : '))
data = []

# take input of the data
for i in range(number_of_data):
    raw = input('Enter data '+ str(i) + ' : ')
    data.append(raw)

# open a file, where you ant to store the data
file = open('important', 'wb')

# dump information to that file
pickle.dump(data, file)

# close the file
file.close()

print("--------------------------------")

# open a file, where you stored the pickled data
file = open('important', 'rb')

# dump information to that file
data = pickle.load(file)

# close the file
file.close()

print('Showing the pickled data:')

c = 0
for item in data:
    print('The data ', c, ' is : ', item)
    c += 1

print("-------------------------------")

class TestClass1:
    def __init__(self, c):
        self.c = c

class TestClass2:
    def __init__(self, c1):
        self.c1 = c1

t1 = TestClass1("test")
t2 = TestClass2(t1)

filename = 't2.dump'
outfile = open(filename,'wb')
pickle.dump(t2, outfile)
outfile.close()

infile = open(filename,'rb')
x = pickle.load(infile)
print (x)
print (x.c1.c)

infile.close()


print("-------------------------------")