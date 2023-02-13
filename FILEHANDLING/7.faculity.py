def add_faculty(file_path, data):
    with open(file_path, "a") as f:
        f.write(",".join(data) + "\n")

def delete_faculty(file_path, id):
    data = []
    with open(file_path, "r") as f:
        for line in f:
            temp = line.strip().split(",")
            if temp[0] != id:
                data.append(temp)
    with open(file_path, "w") as f:
        for d in data:
            f.write(",".join(d) + "\n")

def update_faculty(file_path, id, data):
    fac_data = []
    found = False
    with open(file_path, "r") as f:
        for line in f:
            temp = line.strip().split(",")
            if temp[0] == id:
                fac_data.append(",".join(data))
                found = True
            else:
                fac_data.append(",".join(temp))
    if found:
        with open(file_path, "w") as f:
            for d in fac_data:
                f.write(d + "\n")
    else:
        print("Faculty not found.")

def display_faculty(file_path, id=None):
    with open(file_path, "r") as f:
        if id:
            for line in f:
                temp = line.strip().split(",")
                if temp[0] == id:
                    print(",".join(temp))
                    break
            else:
                print("Faculty not found.")
        else:
            for line in f:
                print(line.strip())

def main():
    file_path = "faculty.txt"
    while True:
        print("1. Add Faculty")
        print("2. Delete Faculty")
        print("3. Update Faculty")
        print("4. Display Faculty")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            id = input("Enter id: ")
            name = input("Enter name: ")
            dept = input("Enter department: ")
            add_faculty(file_path, [id, name, dept])
        elif choice == "2":
            id = input("Enter id to delete: ")
            delete_faculty(file_path, id)
        elif choice == "3":
            id = input("Enter id to update: ")
            name = input("Enter name: ")
            dept = input("Enter department: ")
            update_faculty(file_path, id, [id, name, dept])
        elif choice == "4":
            id = input("Enter id to display (Press enter to display all): ")
            display_faculty(file_path, id)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
