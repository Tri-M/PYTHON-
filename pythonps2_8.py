def encode():
    s = input("Enter your text: ")
    n = int(input("Enter shift bit:"))
    es=""
    for i in s:
        es += chr(int(ord(i)) + n)

    return es


def decode():
    s = input("Enter your text: ")
    n = int(input("Enter shift bit:"))
    es=""
    for i in s:
        es += chr(int(ord(i)) - n)

    return es


while(True):
    print("Menu:\n1. Encode\n2. Decode\n3. Exit\n")
    n = int(input("Enter your input: "))
    if (n == 1):
        s = encode()
        print(s)
    elif ( n == 2):
        s = decode()
        print(s)
    elif (n == 3):
        break
    else:
        print("Enter correct input.\n")
