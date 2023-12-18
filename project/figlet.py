import pyfiglet
import sys

def main():
    my_contact_list = ContactList()

    while True:
        try:
            contact_list = pyfiglet.figlet_format("Simple Contacts Program", font="bulbhead")
            print(contact_list)
            print("1. Add a new Contact")
            print("2. Remove Contact")
            print("3. Display Contacts")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter contact name: ")
                phone_number = input("Enter phone number: ")
                contact = Contact(name, phone_number)
                my_contact_list.add_contact(contact)
                print("Contact added!")

            elif choice == "2":
                name = input("Enter the name of the contact to remove: ")
                my_contact_list.remove_contact(name)
                print("Contact removed!")

            elif choice == "3":
                print("Contacts:")
                my_contact_list.display_contacts()

            elif choice == "4":
                print("Exiting the program...")
                break

            else:
                print("Invalid choice. Please select a valid option.")
        except EOFError:
            print()
            sys.exit("Exiting the program...")
        except KeyboardInterrupt:
            print()
            sys.exit("Exiting the program...")

class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}"

class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return

    def display_contacts(self):
        for contact in self.contacts:
            print(contact)



if __name__ == "__main__":
    main()

