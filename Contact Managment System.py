def add_contact(contacts):
    contact = input("Enter Contact Name: ")
    if contact in contacts:
        print(f"{contact} already exist!")
    else:
        try:
            phone_number = int(input("Enter Phone Number: "))
            email_address = input("Enter Email Address: ")
            contacts[contact] = (phone_number,email_address)
            print(f'Contact: {contact} has now been added you are most certainly welcome!')
        except ValueError:
            print(f'This is a invalid phone number. please enter a valid integer')

    
def edit_contact(contacts):
    contact = input("Enter Contact:")
    if contact not in contacts:
        print('Contact Not found')
    else:
        try:
            phone_number = int(input("Enter Phone Number"))
            email_address = input("Enter Email Address")
            contacts[contact] = (phone_number, email_address)
            print(f"Contact: {contact} has now been edited")
        except ValueError:
            print(f'This is a invalid phone number. please enter a valid integer')

def delete_contact(contacts):
    contact = input("Enter Contact: ")
    if contact not in contacts:
        print("This Contact Does Not Exist")
    else:
        del contacts[contact]
        print(f"Contact: {contact} was deleted from your contacts")

def search_for_contact(contacts):
    contact = input("Enter Contact: ")
    if contact in contacts:
        phone_number,email_address = contacts[contact]
        print("We Found Your Contact, Read Below!")
        print(f"Contact: {contact}\nPhone Number: {phone_number}\nEmail Address: {email_address}")
    else:
        print("Contact Was Not Found")

    
def display_contacts(contacts):
    for contact, details in contacts.items():
        print("Your Contact Was Found! Read Below!")
        print(f"Contact: {contact} Phone Number - {details[0]} Email Address - {details[1]}")

def export_contacts(filename,contacts):
    with open(filename, 'w') as file:
        for contact,details in contacts.items():
            file.write(f"Name: {contact},Phone Number: {details[0]},Email Address: {details[1]}\n")
    print(f"Contacts exported to {filename}")
def import_contacts(filename, contacts):
    try:
        with open(filename, 'r') as file:
            for line in file:
                contact,phone_number,email_address = line.strip().split(',')
                contacts[contact] = (int(phone_number),email_address)
        print(f'Contacts imported from {filename}')
        return contacts
    except FileNotFoundError:
        print(f"No contacts found at {filename}")
        


def user_interface(filename):
    contacts = {}
    import_contacts(filename,contacts)

    while True:
        
        print("Welcome To The Contact Management System!\nMenu: \n1. Add a new contact\n2. Edit an existing contact\n3. Delete a contact\n4. Search for a contact\n5. Display all contacts\n6. Export contacts to a text file\n7. Import contacts from a text file *BONUS*\n8. Quit")
        try:
            choice = int(input("Enter Choice From The Menu: "))


            if choice == 1:
                add_contact(contacts)
            elif choice == 2:
                edit_contact(contacts)
            elif choice == 3:
                delete_contact(contacts)
            elif choice == 4:
                search_for_contact(contacts)
            elif choice == 5:
                display_contacts(contacts)
            elif choice == 6:
                export_contacts(filename,contacts)
            elif choice == 7:
                import_contacts(filename,contacts)
            elif choice == 8:
                print("Exiting Now....")
                break
        except ValueError: 
            print("You entered a non integer")

          
    


if __name__ == "__main__":
    user_interface("contacts.txt")



