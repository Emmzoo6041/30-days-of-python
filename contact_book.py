import json
import os

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(name, phone, email):
    contacts = load_contacts()
    contacts[name] = {
        'phone': phone,
        'email': email
    }
    save_contacts(contacts)
    print(f"Contact {name} added successfully!")

def get_contact(name):
    contacts = load_contacts()
    if name in contacts:
        return contacts[name]
    else:
        print(f"Contact {name} not found.")
        return None

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Get Contact")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            add_contact(name, phone, email)
        elif choice == '2':
            name = input("Enter name to search: ")
            contact = get_contact(name)
            if contact:
                print(f"Name: {name}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")
        elif choice == '3':
            print("Exiting the Contact Management System.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()