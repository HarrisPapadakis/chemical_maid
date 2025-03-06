class Human:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'address': self.address
        }


humans = []

def input_human():
    name = input("Enter name: ")
    age = input("Enter age: ")
    address = input("Enter address: ")
    human = Human(name, age, address)
    humans.append(human)
    print(f"Human {name} added successfully.")

def edit_human():
    name = input("Enter the name of the human to edit: ")
    for human in humans:
        if human.name == name:
            new_name = input(f"Enter new name (current: {human.name}): ")
            new_age = input(f"Enter new age (current: {human.age}): ")
            new_address = input(f"Enter new address (current: {human.address}): ")
            human.name = new_name if new_name else human.name
            human.age = new_age if new_age else human.age
            human.address = new_address if new_address else human.address
            print(f"Human {name} updated successfully.")
            return
    print(f"Human with name {name} not found.")

def delete_human():
    name = input("Enter the name of the human to delete: ")
    for i, human in humans:
        if human.name == name:
            del humans[i]
            print(f"Human {name} deleted successfully.")
            return
    print(f"Human with name {name} not found.")

def save_humans():
    with open('humans.txt', 'w') as file:
        for human in humans:
            file.write(str(human.to_dict()) + '\n')
    print("Humans saved successfully.")

def display_humans():
    if not humans:
        print("No humans to display.")
    for human in humans:
        print(human.to_dict())

def main():
    while True:
        print("\nMenu:")
        print("1. Εισαγωγή Στοιχείων Ανθρώπου")
        print("2. Διόρθωση Στοιχείων Ανθρώπου")
        print("3. Διαγραφή Στοιχείων Ανθρώπου")
        print("4. Αποθήκευση Στοιχείων Ανθρώπου")
        print("5. Εμφάνιση Στοιχείων Ανθρώπου")
        print("6. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                input_human()
            case '2':
                edit_human()
            case '3':
                delete_human()
            case '4':
                save_humans()
            case '5':
                display_humans()
            case '6':
                print("Exiting the program.")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
