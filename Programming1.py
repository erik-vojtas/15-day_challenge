s = 4
c = 1
for t in range(-1,3):
    print("Iteration:", c)
    print("\tt =", t)
    s = s-t**3+1
    print("\ts =",s)
    c+=1

print(s)
print("------------------------")


def f1(f,x):
    print(f(x**2))

print(f1(lambda c:c+2, 3))
print("------------------------")


def getTime(num):
    sec = num % 60
    min = int((num - sec)/60%60)
    h = int((num - sec - (60*min))/(60*60))
    print(f"{h}h:{min}m:{sec}s")

getTime(1234)
getTime(4567)
print("------------------------")



