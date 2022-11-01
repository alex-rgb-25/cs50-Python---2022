def main():
    txt = input("input: ")
    print(shorten(txt))

def shorten(word):
    lis = []
    for l in range(len(word)):
        if word[l] not in ['a','e','i','o','u']:
            lis.append(word[l])
    txt = ''.join(lis)
    return txt

if __name__ == "__main__":
    main()
