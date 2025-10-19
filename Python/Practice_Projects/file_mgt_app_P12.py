# file  managment APP 

import os

def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"File Name {filename} Created Successfully 🫡")
    
    except FileExistsError:
        print(f"File Name {filename} Alredy Exists! 🫥")
    
    except Exception as e:
        print(f"An Error Occured ! 🤔")

def view_all_files():
    files = os.listdir()
    if not files:
        print("File not exits! 🫤")
    else:
        print("Files in the Directory: ")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"file name {filename} is deleted successfully! 🫡")

    except FileNotFoundError:
        print("File not found!")
    
    except Exception as e:
        print("An Error Occured!!")

def read_file(filename):
    try:     
        with open('sample.txt','r') as f:
            content = f.read()
            print(f"Content Of '{filename}': \n{content}")
    
    except FileNotFoundError:
        print(f"{filename} is Not Found!")

    except Exception as e:
        print("An Error Occured!!")

def edit_file(filename):
    try:
        with open('sample.txt','a') as f:
            content = input("Add your data here: ")
            f.write(content + "\n")
            print(f" Content Updated Successfully to {filename}")     
        
    except FileNotFoundError:
        print(f"{filename} is Not Found!")

    except Exception as e:
        print("An Error Occured!!")
       
def main():
    while True:
        print("------ FILE MANAGEMENT APP ------")
        print("1. Create File")
        print("2. Update File")
        print("3. Delete File")
        print("4. Read File")
        print("5. View All File")
        print("6. Exit/Close")
        
        choice = input("Enter Your Choice (1-6) 🤧 = ")

        if choice == '1':
            filename = input("Enter the file-name you have to Create 😌= ")
            create_file(filename)

        elif choice == '2':
            filename = input("Enter file-name to Edit File 😊= ")
            edit_file(filename)

        elif choice == '3':
            filename = input("Enter file_name tp Delete 🫠= ")
            delete_file(filename)

        elif choice == '4':
            filename = input("Enter the file_name to Read 👨‍🎓= ")
            read_file(filename)
        
        elif choice == '5':
            view_all_files()

        elif choice == '6':
            print("Thank You, Closing the Program !! 😉")
            break
        else:
            print("Invalid Choice !! Enter Correct Choice")

if __name__ == "__main__":       
    main()



