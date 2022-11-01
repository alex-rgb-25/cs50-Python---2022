def main():
    
    inp = input('fraction: ')
    percentage = convert(inp)
    print(gauge(percentage))

def convert(fraction):
    while True:
        try:
            x, y = fraction.split('/')
            g = f'{int(x)/int(y)*100:.0f}'
            if int(x) > int(y):
                raise ValueError
            return int(g)
        except ValueError:
            fraction = input("fraction: ")
            continue
        except ZeroDivisionError:
            fraction = input("fraction: ")
            continue

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return (f'{percentage}%')

if __name__ == "__main__":
    main()
