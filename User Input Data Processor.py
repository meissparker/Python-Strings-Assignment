def first_last(first, last):

    print(f"Your first name is {len(first)} characters long")
    print(f"Your last name is {len(last)} characters long")

while True:
    first = input("Enter your first name: ")
    second = input("Enter your last name: ")
    if len(first) < 2 or len(second) < 2:
        print("You must enter at least 2 letters.")
    else:
        first_last(first, second)





