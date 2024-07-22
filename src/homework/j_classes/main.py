from class_a import die

def main():
    die_instance = die()
    
    while True:
        die_instance.roll()
        print(die_instance)
        
        user_input = input("Would you lile to roll again? (type (y/n)): ").strip().lower()
        if user_input != 'y':
            break

if __name__ == "__main__":
    main()
