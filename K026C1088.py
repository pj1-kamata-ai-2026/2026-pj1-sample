num = input("Enter a number: ")
if num .isdigit():
    num = int(num)
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")