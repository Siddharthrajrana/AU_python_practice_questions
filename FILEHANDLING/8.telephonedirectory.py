# Program to maintain a file directory
import os

def add_contact(directory, name, number):
    directory[name] = number
    print("Contact added successfully")

def search_contact(directory, name):
    if name in directory:
        return directory[name]
    else:
        return "Contact not found"

def update_number(directory, name, number):
    if name in directory:
        directory[name] = number
        print("Contact number updated successfully")
    else:
        print("Contact not found")

def update_name(directory, name, new_name):
    if name in directory:
        directory[new_name] = directory.pop(name) 
        print("Contact name updated successfully")
    else:
        print("Contact not found")

def delete_contact(directory, name):
    if name in directory:
        directory.pop(name)
        print("Contact deleted successfully")
    else:
        print("Contact not found")

def read_file(filename):
    directory = {}
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                name, number = line.strip().split(',')
                directory[name] = number
    return directory

def write_file(filename, directory):
    with open(filename, 'w') as file:
        for name, number in directory.items():
            file.write(f"{name},{number}\n")

def main_menu(filename):
    directory = read_file(filename)
    while True:
        print("\nMain Menu")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact Number")
        print("4. Update Contact Name")
        print("5. Delete Contact")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter name: ")
            number = input("Enter number: ")
            add_contact(directory, name, number)
        elif choice == 2:
            name = input("Enter name: ")
            print(search_contact(directory, name))
        elif choice == 3:
            name = input("Enter name: ")
            number = input("Enter new number: ")
            update_number(directory, name, number)
        elif choice == 4:
            name = input("Enter name: ")
            new_name = input("Enter new name: ")
            update_name(directory, name, new_name)
        elif choice == 5:
            name = input("Enter name: ")
            delete_contact(directory, name)
        elif choice == 6:
            break
        else:
            print("Invalid choice. Try again.")
        write_file(filename, directory)

if __name__ == '__main__':
    filename = "directory.txt"
    main_menu(filename)
