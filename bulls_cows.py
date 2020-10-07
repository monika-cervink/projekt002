import random
generator = random.sample((range(0, 10)), 4)    # náhodná volba pc, list cisel
generator = [str(i) for i in generator]         # prevedeni na list stringu
print(f"generator: {generator}")                # pomocný print


def cows_number(sequence):
    cows = 0
    for i in sequence:
        if i in generator:
            cows += 1
    return print(f"cows: {cows}")


def bulls_number(sequence):         # nepricita bulls
    for i in sequence:
        bulls = 0
        index = 0
        if i[index] == generator[index]:
            bulls += 1
            index += 1
        else:
            index += 1
        return print(f"bulls: {bulls}")


print("Hi there! Let's play Bulls & Cows game!")
print("I've generated a random number for you (4 digit).")
try:
    guess = list(input("Enter a number: "))   # list stringů
    while not len(guess) == 4:         # co když zada pismeno
        print("Enter a 4 digit number!")
        guess = list(input("Enter a number: "))   # volba hráče (list stringu)
    cows_number(guess)
    bulls_number(guess)
except:           # dodelat errory
    print("Enter a 4 digit number!")
