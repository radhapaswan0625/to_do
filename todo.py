#Simple To_Do List App

tasks=[]

while True:
    print("\n....To_Do List App....")
    print("1. Add Tasks")
    print("2. View Tasks")
    print("3. Mark Task Completed")
    print("4. Delete Tasks")
    print("5. Exit")


    choice=input("Enter your choice (1-5)")

    if choice=="1":
        task=input("Enter task name:")
        tasks.append({"task":task, "completed": False})
        print("Task added successfully!")

    elif choice=="2":
        if not tasks:
            print("No tasks yet.")

        else:
            print("\n Your tasks:")
            for i, t in enumerate(tasks, 1):
                status="bold tick"if t["completed"]else "cross marks"
                print(f"{i}.{t['task']} [{status}]")

    elif choice=="3":
        task_no=int(input("Enter task number to mark completed:"))

        if 0<task_no<=len(tasks):
            tasks[task_no-1]["completed"]=True
            print("Task marked as completed!")

        else:
            print("Invalid task number!")

    elif choice=="4":
        task_no=int(input("Enter task number to delete:"))
        if 0<task_no<=len(tasks):
            removed =tasks.pop(task_no-1)
            print(f"Task '{removed ['task']}' deleted!")


    elif choice=="5":
        print("Exiting the To-Do List App. GoodBye!")

        break

    else:
        print("Invalidd choice! Enter a number 1-5.")
