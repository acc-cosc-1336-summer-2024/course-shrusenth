import repetition

def menu():
    while True:
        print("Homework 3 Menu")
        print("1 - Factorial")
        print("2 - Sum odd numbers")
        print("3 - Exit")
        menuoptions()

def menuoptions():
    choice = input("Choose option: ")
    if choice == "1":
        handle_factorials()
    elif choice == "2":
        handle_sum_odd_numbers()
    else:
      handle_exit()
