contacts = {} #lsit

while True: #cant close until user dont want 
    print("\n CONTACT BOOK APP")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6.Count Contacts")
    print("7.Exit")   

    Choice = int(input("Enter Your Choice ="))   #variable 

    if Choice == 1:                     
        name = input("Enter Your Name =")
        if name in contacts:   #membership operator                 #if name is i contact then print 
            print(f"Contact Name {name} Already Exists! ")
        else:
            age = int(input("Enter Age ="))               # if contact is not avi then ask for information 
            email = input("Enter Email =")
            phone_no = input("Enter Phone Number =")   
            contacts[name] = {"age":int(age), "email":email, "phone_no":phone_no} #update it into Contact[] -empty list created at top
            print(f"Contact name {name} has been updated Succesfully")
    
    elif Choice == 2:
        name = input("Enter the Contact to view =")
        if name in contacts:  #check 1st contact is avi or not
            contact = contacts[name]   # if contact is avilable
            print (f"Name:{name}, Age:{age}, phone_no:{phone_no}")  #show contact
        else:
            print("Contact not Found!!")

    elif Choice == 3 :  #update contact
        name = input("Enter the Contact to Update =")
        if name in contacts:
            age = (input("Update Age ="))
            email = input("Update email =")
            phone_no = (input("Update phone_no="))
            contacts[name] = {"age":int(age), "email":email, "phone_no":phone_no}
            # contactme jo key present hai usme values koupdate kardo means age, email and phone_no is value and name is key = key-value pair

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
        found = False #if any count is matched or not and to retirve
        for name, contact in contacts.item(): #key value pair ka sequence milta hai tuple k andar i.e name and contact
             # name hamara key hai aur contact value aur contacts h key value pair ki list .item se hm wo sb 
            if search_name.lower() in name.lower(): #if this condition is true then contact enter by user is avilable   
                #check krta hai ki jo value inter ki hia user ne lower case me uska koi hissa hamare contantcs me hai ya nhi 
                print(f" Contact is Found- Name {name}, Age:{age}, email:{email},phone_no:{phone_no}")
                found = True # ye make sure karega ki atleast ke contact toh mila
            if not found:
                print("Contact Not Found")
    elif Choice == 6:
        print(f"Total Contact in your Book is = {len(contacts)}")  #count ka bhi use kr skte hai len se sare contact mil jayega lets see


    elif Choice == 7:
        print("Thank You 😊 Program is Closing.....")
        break 
    else:
        print("Invalid Choice")