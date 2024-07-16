
from strings import get_hamming_distance, get_dna_complement

def print_menu():
    print("1 - Hamming Distance")
    print("2 - DNA Complement")
    print("3 - Exit")

def get_user_choice():
    while True:
        try:
            choice = int(input("Pick a choice from the menu "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid input.")
        except ValueError:
            print("Invalid input.")

def main():
    while True:
        print_menu()
        choice = get_user_choice()

        if choice == 1:
            dna1 = input("What is the first DNA sequence?")
            dna2 = input("What is the second DNA sequence? ")
            try:
                distance = get_hamming_distance(dna1, dna2)
                print(f"Hamming Distance between {dna1} and {dna2} is: {distance}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == 2:
            dna = input("Enter the DNA sequence: ")
            complement = get_dna_complement(dna)
            print(f"The DNA complement of {dna} is: {complement}")

        elif choice == 3:
            print("")
            break

if __name__ == '__main__':
    main()
