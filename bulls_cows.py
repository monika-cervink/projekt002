import random
import time
generator = random.sample((range(0, 10)), 4)
generator = [str(i) for i in generator]

print("Hi there! Let's play Bulls & Cows game!")
print("I've generated a random number for you (4 digit).")
start = time.time()
counter = 0
while counter >= 0:
    guess = input("Enter a number: ")
    while len(guess) != 4 or not guess.isdigit():
        print("Enter a 4 digit number!")
        guess = input("Enter a number: ")
    bulls = 0
    cows = 0
    for seq, number in enumerate(guess):
        for seq2, number2 in enumerate(generator):
            if seq == seq2 and number == number2:
                bulls += 1
            elif seq != seq2 and number == number2:
                cows += 1
    if cows != 1 and bulls == 1:
        print(f"{bulls} bull, {cows} cows")
    elif cows == 1 and bulls != 1:
        print(f"{bulls} bulls, {cows} cow")
    elif cows == 1 and bulls == 1:
        print(f"{bulls} bull, {cows} cow")
    else:
        print(f"{bulls} bulls, {cows} cows")
    counter += 1
    if bulls == 4:
        break
end = time.time()
timer = end - start
minutes = round(timer // 60)
seconds = round(timer % 60)

if counter <= 10:
    level = "amazing!"
elif 10 < counter <= 20:
    level = "average."
else:
    level = "not so good..."

print(f"Great, you've guessed the right number in {counter} guesses! "
      f"That's {level} \nYou did it in {minutes} min {seconds} sec.")
with open("number_of_guesses.txt", "a+") as file:
    file.write(f"{counter}\n")
