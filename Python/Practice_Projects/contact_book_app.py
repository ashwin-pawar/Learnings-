contacts = {} 

while True: 
    print("\n CONTACT BOOK APP")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6.Count Contacts")
    print("7.Exit")   

    Choice = int(input("Enter Your Choice ="))   

    if Choice == 1:                     
        name = input("Enter Your Name =")
        if name in contacts:   #membership operator                
            print(f"Contact Name {name} Already Exists! ")
        else:
            age = int(input("Enter Age ="))              
            email = input("Enter Email =")
            phone_no = input("Enter Phone Number =")   
            contacts[name] = {"age":int(age), "email":email, "phone_no":phone_no} 
            print(f"Contact name {name} has been updated Succesfully")
    
    elif Choice == 2:
        name = input("Enter the Contact to view =")
        if name in contacts: 
            contact = contacts[name]   
            print (f"Name:{name}, Age:{age}, phone_no:{phone_no}") 
        else:
            print("Contact not Found!!")

    elif Choice == 3 :  
        name = input("Enter the Contact to Update =")
        if name in contacts:
            age = (input("Update Age ="))
            email = input("Update email =")
            phone_no = (input("Update phone_no="))
            contacts[name] = {"age":int(age), "email":email, "phone_no":phone_no}
            print("Contact not Found")

    elif Choice == 4:
        name = input("Enter the Contact to delete =")
        if name in contacts:
            del contacts[name]
            print(f"Contact Name {name}  has been Deleted Successfully ")
        else:
            print("Contact not Found")

    elif Choice == 5:
        search_name = input("Enter the Contact to Search =")
        found = False 
        for name, contact in contacts.item():

            if search_name.lower() in name.lower(): 
                print(f" Contact is Found- Name {name}, Age:{age}, email:{email},phone_no:{phone_no}")
                found = True 
            if not found:
                print("Contact Not Found")
    elif Choice == 6:
        print(f"Total Contact in your Book is = {len(contacts)}")


    elif Choice == 7:
        print("Thank You 😊 Program is Closing.....")
        break 
    else:

        print("Invalid Choice")



NOTE :- In this project i make use of membership operator (key-value pair) as well as other concepts like 
        Loops, Dictonary, Formatted String, if-elif-else  and methods like .lower() .item() .len().

        I am still leanring everyday and imporving my skiils in python. (> - <)
