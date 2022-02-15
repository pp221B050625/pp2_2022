import random

print("Hello! What is your name?")
name = input()


def game(n):
    cnt = 0
    number = random.randint(1, 20)
    print(f'Well, {n}, I am thinking of a number between 1 and 20.')
    print("Take a guess.")
    while True:
        a = int(input())
        if a == number:
            cnt += 1
            print(f'Good job, {n}! You guessed my number in {cnt} guesses!')
            return
        if a > number:
            cnt += 1
            print("Your guess is too high")
            print("Take a guess.")
        if a < number:
            cnt += 1
            print("Your guess is too low")
            print("Take a guess.")


game(name)
