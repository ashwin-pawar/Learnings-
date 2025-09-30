def task():
    tasks =[] # empty list
    print("----WELCOME TO TO-DO-LIST APPLICATION----")

    task_name = int(input("Enter How many Task you want : "))
    for i in range(1,task_name+1):
        task_name = input(f"Enter the task here : {i}  = ") #to add multiple tasks 
        tasks.append(task_name) # adding task to list

    print(f"Today's Task are\n - {tasks}") # display all tasks

    while True: 
        operations = int(input("Enter 1- Add\n Enter 2- Update\n Enter 3- Delete\n Enter 4- View\n Enter 5- Exit/Stop/"))
        if operations == 1:
            add = input("Enter the task you wants to Add =")
            tasks.append(add)
            print(f"task added Successfully 😌 \n - {tasks}")
        elif operations == 2:
            update = input("Enter the Task_No You wantes to Update =")
            if update in tasks:
                up= input("Enter the new Task =")
                ind= tasks.index(update) #we are find the tasks via index which we want to update
                tasks[ind] = up
                print(f"Task is Updated 🫥 \n - {up}")

        elif operations == 3:
            delete = input("Enter the task you wants to delete =")
            if delete in tasks:
                ind = tasks.index(delete)
                del tasks[ind] #for deleting task i used remove method but it wont work so use del
                print(f"Task {tasks} is Deleted Succcessfully... 😉 ")
        
        elif operations == 4:
            print(f"Todays Total Task = {tasks}" )
        
        elif operations == 5:
            print("Thank You. Closing the Program 🫡")
            break
        else:
            print("Invalid Input, Enter Correct Input ")

task() # calling function