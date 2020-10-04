import random
generator = random.sample((range(0, 10)), 4)    # náhodná volba pc
print(f"generator: {generator}")                # pomocný print


def cows_number(sequence):
    cows = 0
    for number in sequence:
        if int(number) in generator:
            cows += 1
    return print(f"cows: {cows}")


print("Hi there! Let's play Bulls & Cows game!")
print("I've generated a random number for you (4 digit).")
try:
    guess = input("Enter a number: ")     # je to STRING!!
    while not len(guess) == 4 or not guess.isdigit():
        print("Enter a 4 digit number!")
        guess = input("Enter a number: ")   # volba hráče (STRING!)
    cows_number(guess)
except TypeError:
    print("Enter a 4 digit number!")
