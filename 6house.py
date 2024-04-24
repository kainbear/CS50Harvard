name = input("What is your name? ")

match name:
    case "Harry":
        print("Welcome to Gryffindor!")
    case _:
        print("Get away!!!")