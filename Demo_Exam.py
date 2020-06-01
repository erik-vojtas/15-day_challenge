a = (1,)
print(a)



def fact(num):
    if num == 0:
        return 1
    else:
        return num*fact(num-1)
print(fact(3))



def censor(word):
    split_sentence = (word.split(" "))
    for w in split_sentence:
        if len(w) <= 5:
            print(w, end=' ')
        else:
            print("*"*len(w), end=' ')
    print("\n")


censor("dsfdsfdsfs")
censor("hello")

# Test Code
censor("The code is fourty") # ➞ "The code is ******" c
censor("Remember two plus three is five") # ➞ "******** two plus three is five" c
censor("aaaaa 1234 12345 seventy nine") #➞ "aaaaa 1234 12345 ******* nine"

# Write a guess number game. At the beginning, the program will generate a random lucky number from 1 to 100.
# After that, the program will ask the user for a guess number.
# If the guess number is greater than the lucky number, it will print out “Too high”;
# if the guess number is less than the lucky number, it will print out “Too low”.
# The program will continue to ask a new guess number until the user enters the lucky number.
# As a consequence, it will print out “You guess right! It costs you x guesses”,
# where x is the number of guesses the user tries.

import random
lucky_num = random.randint(1, 100)
counter = 0
def guess_game():
    global counter
    counter += 1
    user_guess = int(input("Guess a number from 1 to 100: "))
    if user_guess == lucky_num:
        print(f"You guess right! It costs you {counter} guesses.")
    elif user_guess > lucky_num:
        print("Too high")
        guess_game()
    else:
        print("Too low")
        guess_game()

guess_game()

for x in range (16,21):
    print(x)

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 8?
# Write a Python Program to determine the result and submit the result below.

for x in range(1, 5000):
    if x % 2 == 0 and x % 3 == 0 and x % 4 == 0 and x % 5 == 0 and x % 6 == 0 and x % 7 == 0 and x % 8 == 0:
        print(f'Smallest positive number that is evenly divisible by all of the numbers from 1 to 8 = {x}.')
        break

found = False
x = 1
while found != True:
    if x % 2 == 0 and x % 3 == 0 and x % 4 == 0 and x % 5 == 0 and x % 6 == 0 and x % 7 == 0 and x % 8 == 0:
        print(f'Smallest positive number that is evenly divisible by all of the numbers from 1 to 8 = {x}.')
        found = True
    x += 1



def harmonic_sum(n):
    result = 0
    for x in range(1, n+1):
        result += 1/x
    return result


print(round (harmonic_sum(300),5))
print(round (harmonic_sum(40),2))
print(round (harmonic_sum(76),2))
print(round (harmonic_sum(400),2))