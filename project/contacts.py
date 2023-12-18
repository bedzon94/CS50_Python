import pyfiglet

# Define a dictionary to store contacts with names as keys and details as values
contacts = {}

# Function to add a contact
def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    
    contacts[name] = {
        "Phone": phone,
        "Email": email
    }
    print(f"{name} has been added to your contacts!")

# Function to display all contacts
def list_contacts():
    print("Contacts List:")
    for name, details in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {details['Phone']}")
        print(f"Email: {details['Email']}")
        print()

# Function to search for a contact
def search_contact():
    name = input("Enter the name to search: ")
    if name in contacts:
        details = contacts[name]
        print(f"Name: {name}")
        print(f"Phone: {details['Phone']}")
        print(f"Email: {details['Email']}")
    else:
        print(f"{name} not found in your contacts.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"{name} has been deleted from your contacts.")
    else:
        print(f"{name} not found in your contacts.")

# Main program loop
while True:
    contact_list = pyfiglet.figlet_format("Simple Contacts Program", font="bulbhead")
    print(contact_list)
    print("1. Add a contact")
    print("2. List all contacts")
    print("3. Search for a contact")
    print("4. Delete a contact")
    print("5. Quit")
    
    choice = input("Enter your choice (1/2/3/4/5): ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        list_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4/5).")

