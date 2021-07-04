import random

def guess(num):
    random_number = random.randint(1,num)
    guess = 0
    while guess != random_number :
        guess = int(input(f"Guess the number between 1 to {num} : "))
        if guess > random_number :
            print(f"Number you choose is too high")
        elif guess < random_number :
            print(f"Number you choose is too low")

    print(f"Yupss...!! You guess the correct number {random_number}....")

guess(10)