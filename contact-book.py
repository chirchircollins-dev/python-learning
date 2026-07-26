contact_book = []

def add_contact(name, phone_number):
    contact = {"name": name,"phone_number": phone_number}
    contact_book.append(contact)
    save_contact()
    print(f"{name} - {phone_number} - added to contact book")

def view_contact_book():
    if len(contact_book) == 0:
        print("We have nothing in the contact book")
    else:
        print("Here is what is present in the contact book")
        for contacts in contact_book:
            print(f"{contacts['name']} - {contacts['phone_number']}")

def search_contact():
    search_term = input("Enter the Name|Phone_Number of contact to be searched")
    for contacts in contact_book:
        
        if contacts["name"] == search_term or contacts["phone_number"] == search_term:
            print(f"{contacts['name']} - {contacts['phone_number']}")


def del_contact():
    delete_contact = input("Enter the contact to delete")
    for contacts in contact_book:
        if delete_contact == contacts["name"] or delete_contact == contacts["phone_number"]:
            print(f"The contact to be deleted is - {contacts['name']}")
            choice = int(input("Do you want to proceed and delete \n 1.yes \n 2.No"))
            if choice == 1:
                contact_book.remove(contacts)
                print("Contact Deleted")
                return
            elif choice == 2:
                return
            else:
                print("Enter a valid Response")

        elif delete_contact != contacts["name" ] or delete_contact == contacts["phone_number"]:
            print("No contacts matches what are you are trying to delete")

        else:
            print("Enter Contact to Delete")
        
        


import json

def save_contact():
    with open("contact.json","w") as file:
        json.dump(contact_book, file)
        print("Contacts saved😊")

def load_contact():
    global contact_book
    try:
        with open("contact.json","r") as banana:
            contact_book = (json.load(banana))
    except FileNotFoundError:
        pass
    

def big_banana():
    load_contact()
    while True:
        print("\nWelcome to Your PhoneBook😊❤️")
        print("\n1.➕ Add Contact")
        print("\n2.👀 View Contacts")
        print("\n3.🔍 Search Contacts")
        print("\n4.🚮 Delete Contacts")
        print("\n5.🔚 Quit")

        choice = int(input("\n  >>>  "))

        if choice == 1:
            name = input("Enter the name of the person you wish to save😊: ")
            phone_number = input("Enter the phone number of the above person😊: ")
            add_contact(name, phone_number)
        elif choice == 2:
            view_contact_book()
        elif choice == 3:
            search_contact()
        elif choice == 4:
            del_contact()
        elif choice == 5:
            break
        else:
            print("Enter a Valid Option🙂")

big_banana()


    



