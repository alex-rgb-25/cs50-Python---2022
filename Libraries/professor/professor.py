import random

def main():
    level = get_level()
    score = 0
    problems = 0
    while(problems < 10):
        tries = 0
        a = generate_integer(level)
        b = generate_integer(level)

        while True:
            try:
                guess = int(input(f"{a} + {b} = "))
                break
            except ValueError:
                if tries < 2:
                    print("EEE")
                    tries += 1
                    continue
                else:
                    break

        answ = a + b
        while tries < 2:
            if guess == answ:
                score += 1
                break
            else:
                tries +=1
                print("EEE")
                guess = input(f"{a} + {b} = ")
        if tries == 2:
            print(f"{a} + {b} = {answ}")
        problems += 1
    print("Score:", score)

def get_level():

    while True:
        level = input("Level: ")
        if level in ["1","2","3"]:
            return level

def generate_integer(level):
    match int(level):
        case 1:
            return random.randint(0,9)
        case 2:
            return random.randint(10,99)
        case 3:
            return random.randint(100,999)
        case _:
            raise ValueError

if __name__ == "__main__":
    main()
