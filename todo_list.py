print("Welcome to my To-Do List")
tasks =[]

while True:
    print("\n===== YOUR TO-DO LIST =====")
    print("1. Add Task")
    print("2. view Tasks")
    print("3. Delete Task")
    print("4. Update Task")
    print("5. Mark Task as Completed")
    print("6. Exit")

    choice = input("Enter your choice:")

    # ADD TASK
    if choice == "1":
        task = input("Enter your task:")
        tasks.append(task)
        print("Task added successfully!")

    # VIEW TASKS
    elif choice =="2":
        print("\n===== YOUR TO-DO LIST =====")

        if len(tasks) == 0:
            print("No tasks availabale!")

        else:
            for number, task in enumerate(tasks, start=1):
             print(number, task)

    # DELETE TASK
    elif choice == "3":

        if len(tasks) ==0:
            print("No tasks available to delete!")

        else:
          for number, task in enumerate(tasks, start=1):
            print(number,task)

        task_number = int(input("Enter the task number to delete:"))

        if 1 <= task_number <=len(tasks):

            deleted_task = tasks.pop(task_number - 1)

            print(deleted_task, "deleted successfully!")

        else:
           print("Invalid task number!")    

    # UPDATE TASK
    elif choice == "4":

        if len(tasks) ==0:
                   print("No tasks available to update!")
       
        else:
            for number, task in enumerate(tasks, start=1):
                   print(number,task)
       
            task_number = int(input("Enter the task number to update:"))
       
            if 1 <= task_number <=len(tasks):
       
                   new_task = input("Enter the new task: ")
                   tasks[task_number - 1] = new_task
       
                   print("Task updated successfully!")
       
            else:
                  print("Invalid task number!") 

                     
     # Mark Task as Completed
    elif choice == "5":

       if len(tasks) == 0:
         print("No tasks available!")

       else:
        for number, task in enumerate(tasks, start=1):
            print(number, task)

        task_number = int(
            input("Enter the task number to mark as completed: ")
        )

        if 1 <= task_number <= len(tasks):

            tasks[task_number - 1] = (
                tasks[task_number - 1] + " [Completed]"
            )

            print("Task marked as completed!")

        else:
            print("Invalid task number!")
        
    # EXIT
     # EXIT
    elif choice == "6":
        print("Thank you for using the To-Do List!")
    break


# INVALID CHOICE
else:
    print("Invalid choice. Please try again") 


       
        
