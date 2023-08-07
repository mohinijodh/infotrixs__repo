import json
import os

def title():

    line_1 = "------------------------------------------"

    title  = "Contact Management System"

    line_2 = "------------------------------------------"


    print(line_1.center(130)) #center() function is used to give a text align to text

    print(title.center(130))

    print(line_2.center(130)) 

title()

class Contact:
    def __init__(self, name, email, phone):
        
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }

class ContactManager:
    def __init__(self, database_file="contacts.json"):
        self.contacts = []
        self.database_file = database_file

    def add_contact(self, name, email, phone):
        if not self._validate_name(name):
            print("Invalid name. Name cannot be empty.")
            return
        if not self._validate_email(email):
            print("Invalid email. Please provide a valid email address.")
            return
        if not self._validate_phone(phone):
            print("Invalid phone number. Please provide a valid phone number.")
            return

        contact = Contact(name, email, phone)
        self.contacts.append(contact)
        self._save_contacts()

    def _validate_name(self, name):
        return bool(name.strip())

    def _validate_email(self, email):
        # A basic email validation check for demonstration purposes
        return "@" in email

    def _validate_phone(self, phone):
        # A basic phone number validation check for demonstration purposes
        return phone.isdigit()

    def _save_contacts(self):
        with open(self.database_file, 'w') as file:
            json.dump([contact.to_dict() for contact in self.contacts], file)

    def load_contacts(self):
        if os.path.exists(self.database_file):
            with open(self.database_file, 'r') as file:
                contacts_data = json.load(file)
                for contact_data in contacts_data:
                    name = contact_data["name"]
                    email = contact_data["email"]
                    phone = contact_data["phone"]
                    contact = Contact(name, email, phone)
                    self.contacts.append(contact)

    def view_contacts(self):
        print("Contact List:")
        for contact in self.contacts:
            print(f"Name: {contact.name}, Email: {contact.email}, Phone: {contact.phone}")
        print("\n")

    def search_contact(self, name):
        found_contacts = []
        for contact in self.contacts:
            if name.lower() in contact.name.lower():
                found_contacts.append(contact)

        if found_contacts:
            print("Search Results:")
            for contact in found_contacts:
                print(f"Name: {contact.name}, Email: {contact.email}, Phone: {contact.phone}")
        else:
            print("No matching contacts found.\n")

    def delete_contact(self, name):
        updated_contacts = [contact for contact in self.contacts if contact.name.lower() != name.lower()]

        if len(updated_contacts) == len(self.contacts):
            print(f"No contact with the name '{name}' found.\n")
        else:
            self.contacts = updated_contacts
            self._save_contacts()
            print(f"Contact '{name}' deleted successfully.\n")

    def update_contact(self, name, new_email, new_phone):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.email = new_email
                contact.phone = new_phone
                self._save_contacts()
                print(f"Contact '{name}' updated successfully.\n")
                return

        print(f"No contact with the name '{name}' found.\n")

# Example usage:
if __name__ == "__main__":
    contact_manager = ContactManager()
    contact_manager.load_contacts()

    while True:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            phone = input("Enter Phone: ")
            contact_manager.add_contact(name, email, phone)
            print("Contact added successfully.\n")
        elif choice == "2":
            contact_manager.view_contacts()
        elif choice == "3":
            name = input("Enter the name to search: ")
            contact_manager.search_contact(name)
        elif choice == "4":
            name = input("Enter the name to delete: ")
            contact_manager.delete_contact(name)
        elif choice == "5":
            name = input("Enter the name to update: ")
            new_email = input("Enter the new email: ")
            new_phone = input("Enter the new phone: ")
            contact_manager.update_contact(name, new_email, new_phone)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.\n")
