print (""" 
          _______________
          Task Management
          ***************        
       """)
pending = []
while True:
    print("""
    1. Add task
           
    2. View tasks list
          
    3. Change status to done
          
    4. Delete Task
          
    5. Exit
    """)
    option = input("Select an option:")
    if option == "5":
       print("""
             **** Thanks for use Task Management ****
             """)
       break
    
   
    elif option == "1":
        print("Option 1 selected")
        print()
        task = input("Input a task to do:")
        pending.append(task)
    
    elif option == "2":
        print("Option 2 Selected")
        print("Tasks list")
        for i, task in enumerate(pending, 1):
            print(f"{i}.{task}")
   
    elif option == "3":
        print("Option 3 selected")
        for i, task in enumerate(pending, 1):
            print(f"{i}. {task}")
        done = int(input ("Select a number of task done:"))
        if 1<= done <=len(pending):
            task_done = pending [done -1]
            del pending [done-1]
            print(f"The task changed to done: {task_done}")
        else:
            print("""
                      ***Task not found***
                  """)

    elif option == "4":
        print("Option 4 Selected")
        for i, task in enumerate(pending, 1):
            print(f"{i}. {task}")
        delete = int(input ("Select a number of task to delete:"))
        if 1<= delete <=len(pending):
            task_delete = pending [delete -1]
            del pending [delete-1]
            print(f"The task was deleted: {task_delete}")
    else:
        print("""
               ******   Invalid  ********
                Select a correct option
               **************************
               """)