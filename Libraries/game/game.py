import random

guess = 0
while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            continue
        correct = random.randint(1, level)
        while guess != correct:
            try:
                guess = int(input("Guess: "))
                if guess < 1:
                    continue
                if guess < correct:
                    print("Too small!")
                elif guess > correct:
                    print("Too large!")
            except ValueError:
                continue
        print("Just right!")
        break
    except ValueError:
        continue
