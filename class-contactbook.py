
import json
class ContactBook:
    def __init__(self):
        self.contacts = []
        self.load_contact()
    
    def add_contact(self, name, phone_number):
        contact = {"name": name, "phone_number": phone_number}
        self.contacts.append(contact)
        self.save_contact()
        print(f"{name} - {phone_number} added!")
    
    def view_contacts(self):
        if len(self.contacts) == 0:
            print("No contacts yet!")
        else:
            for contact in self.contacts:
                print(f"{contact['name']} - {contact['phone_number']}")

    def delete_contacts(self):
        choice = input("Enter Contact to delete ")
        if choice == "":
            print("Please Enter smth to delete")
            return
        for contacts in self.contacts:
            if choice.lower() == contacts["name"].lower():
                confirm = int(input(f"Do you really want to delete {contacts['name']} \n 1.Yes \n 2.No \n"))
                if confirm == 1:
                    self.contacts.remove(contacts)
                    print("Contact Deleted")
                    return
                elif confirm == 2:
                    return
                else:
                    print("Invalid Option")
                    return
            
        print("No such Contact")
            
    def search_contact(self):
        search_list = input("Enter a Contact to be searched ")
        if search_list.lower() == "":
            print("Please Enter smth to delete")
            return
        for contacts in self.contacts:
            if search_list.lower() == contacts["name"].lower():
                print(F" {contacts['name']} is the contact you are searching for")
                return
            
        print("There is no contacts matching that name")

    def save_contact(self):
        with open("contact_file.json", "w") as file:
            json.dump(self.contacts, file)
            print("Contacts saved!")

    def load_contact(self):
        try:
            with open("contact_file.json", "r") as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            pass


            
                


            



# create the object from the blueprint

def main():
    my_book = ContactBook()
    while True:
        print("Welcome to My_Book platform \n \n")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Delete Contacts")
        print("5. Quit")

        choice = int(input("Enter Your Choice "))
        if choice == 1:
            name = input("Enter name of Contact ")
            phone_number = input("Enter the Phone Number of the Contact ")
            my_book.add_contact(name, phone_number)
        elif choice == 2:
            my_book.view_contacts()
        elif choice == 3:
            my_book.search_contact()
        elif choice == 4:
            my_book.delete_contacts()
        elif choice == 5:
            break
        else:
            print("Invalid option")
     
main()

