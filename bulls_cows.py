import random
generator = random.sample((range(0, 10)), 4)
generator = [str(i) for i in generator]
print(f"generator: {generator}")                # pomocný print


def cows_number(sequence):
    cows = 0
    for i in sequence:
        if i in generator:
            cows += 1
    return cows


def bulls_number(sequence):
    bulls = 0
    for seq, number in enumerate(sequence):
        for seq2, number2 in enumerate(generator):
            if seq == seq2 and number == number2:
                bulls += 1
    return bulls


print("Hi there! Let's play Bulls & Cows game!")
print("I've generated a random number for you (4 digit).")
counter = 0
while generator:
    guess = input("Enter a number: ")
    while not len(guess) == 4 or not guess.isdigit():
        print("Enter a 4 digit number!")
        guess = input("Enter a number: ")
    print(f"cows: {cows_number(guess)}, bulls: {bulls_number(guess)}")
    counter += 1
    if (bulls_number(guess)) == 4:
        break
if counter <= 5:
    level = "amazing!"
elif counter <= 10:
    level = "average."
else:
    level = "not so good..."
print(f"Great, you've guessed the right number in {counter} guesses! That's {level}")
