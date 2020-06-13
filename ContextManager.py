
import contextlib

@contextlib.contextmanager
def mycontext (p):
    print ("Create Context")
    yield "c-Object"
    print ("Clear Context")

with mycontext("") as c:
    print (c)
    print ("after the context", c)
print("-------------------------------")

class myContext:
    def __init__ (self, p):
        self.p = p

    def __enter__(self):
        print ("Create Context")
        return "c-object"

    def __exit__(self, exception, value, trace):
        print ("Clear Context")

with myContext("") as c:
    print (c)
    print ("after the context", c)
print("-------------------------------")

# Implement this_file_reader
# • Define a context manager (based on a class) that can read the current python script.
# • Use __file__ attribute to get the name of the current file


class this_file_reader:

    def __enter__(self):
        self.file = open(__file__)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.file.close()

with this_file_reader() as fm:
    print(fm.read())
#file is closed when execution reaches this line
print(fm.closed)


print("-------------------------------")


import contextlib
import os

@contextlib.contextmanager
def this_file_reader():
    #x= open(os.path.basename(__file__))
    x = open(__file__)
    yield x
    x.close()

with this_file_reader() as fm:
		print (fm.read())

#file is closed when execution reaches this line
print (fm.closed)

print("-------------------------------")