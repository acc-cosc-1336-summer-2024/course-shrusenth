# main.py
from homework.i_dictionaries_sets.dictionary import get_p_distance_matrix  

def main():
    while True:
        print("\nMenu:")
        print("1 - Get p-distance matrix")
        print("2 - Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            
            dna_sequences = []
            while True:
                sequence_str = input("Enter a DNA sequence (or 'done' to finish): ")
                if sequence_str.lower() == 'done':
                    break
                dna_sequences.append(list(sequence_str.upper()))

          
            seq_length = len(dna_sequences[0]) if dna_sequences else 0
            if not all(len(seq) == seq_length for seq in dna_sequences):
                print("Invalid input: Sequences must be same length.")
                continue

            
            matrix = get_p_distance_matrix(dna_sequences)
            for row in matrix:
                for val in row:
                    print(f"{val:.5f}", end=" ")
                print()
        elif choice == '2':
            print("Exit.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
