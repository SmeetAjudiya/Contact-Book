contacts = {}

def display_contacts():
    print("Name\t\t Contact Number")
    for key in contacts:
        print("{}\t\t{}".format(key,contacts.get(key)))

while True:
    print("1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")

    choice = int(input("Enter Your Choice:"))

    if choice == 1:
        name = input("Enter Name:")
        phone = input("Enter PhoneNumber:")
        contacts[name] = phone 

    elif choice == 2:
        if not contacts:
            print("Empty Contact Book")
        else:
            display_contacts()    

    
    elif choice == 3:
        search_name = input("Enter the contact name:")
        if search_name in contacts:
            print(search_name, "Contact Number is", contacts[search_name])
        else:
            print("Name not found in Contact Book")
    
    elif choice == 4:
        edit_contact = input("Enter contact to be edited:") 
        if edit_contact in contacts:
            phone = input("Enter Mobile Number:")
            contacts[edit_contact] = phone
            print("Contact Updated")
        else:
            print("Name not found in Contact Book")
    
    elif choice == 5:
        del_contact = input("Enter contact name to delete:")
        if del_contact in contacts:
            confirm = input("Do you want to delete the contact (yes/no):")
            if confirm.lower() == "yes":
                contacts.pop(del_contact)
            display_contacts()
        else:
            print("Name not found in the contact book")
        
    else:
        break