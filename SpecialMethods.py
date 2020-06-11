class Student:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        new_str = ""
        new_str += self.name + "+" + other.name
        return Student(new_str)

    # def __repr__(self):
    #     return self.name

    def __str__(self):
        return self.name

    def __len__(self, string):
        return f"The lenght is: {len(string)}."

    def __cmp__(self, other):
        if self.name == other.name:
            return f"Names equal."
        else:
            return f"Names do not equal."

    def __mul__(self, number):
        return self.name * number

    def __pow__(self, power, modulo=None):
        return self.name * 2 ** power

    def __getitem__(self, item):
        return self.name, item.name

    def __contains__(self, item):
        if self.name in item.name:
            return "found"
        else:
            return "not found"



s1 = Student("Sandy") # name
s2 = Student("Spili") # name
s3 = Student("Waile") # name

print(s1+s2+s3)

s4 = Student("Waile") # name

print(s1.__len__("abcde"))
print(s3.__cmp__(s4))
print(s1.__mul__(3))
print(s1.__pow__(4))
print(s1.__getitem__(s2))
print(s3.__contains__(s4))

print(dir(s1))

import gc
for obj in gc.get_objects():
    if isinstance(obj, Student):
        print(obj)