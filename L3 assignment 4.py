contacts = {}

while True:
    print("\n---- Contact List ----")
    print("1. Add contact")
    print("2. Remove contact")
    print("3. Show contacts")
    print("4. Exit")

    choice = input("Enter your choice (01-04): ")

    if choice == "01":
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        contacts[name] = number
        print(f"{name} added to contacts")
    elif choice == "02":
        name = input("Enter name to remove: ")
        if name in contacts:
            del contacts[name]
            print(f"{name} removed from contacts")
        else:
            print(f"{name} not found in contacts")
    elif choice == "03":
        print("\n---- Contacts ----")
        for name, number in contacts.items():
            print(f"{name}: {number}")
    elif choice == "04":
        print("Exiting contact list...")
        break
    else:
        print("Invalid choice. Try again.")
