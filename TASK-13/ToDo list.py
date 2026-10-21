# ==========================================
#          TO-DO LIST APPLICATION
# ==========================================

tasks = []

print("-" * 45)
print("           MY TO-DO LIST")
print("-" * 45)

while True:

    print("\n========== MAIN MENU ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Clear All Tasks")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ")


    # ======================================
    # 1. ADD TASK
    # ======================================

    if choice == "1":

        print("\n--- ADD NEW TASK ---")

        task_name = input("Enter task name: ")

        if task_name == "":
            print(" Task cannot be empty!")

        else:
            task = {
                "name": task_name,
                "completed": False
            }

            tasks.append(task)

            print(" Task added successfully!")


    # ======================================
    # 2. VIEW TASKS
    # ======================================

    elif choice == "2":

        print("\n--- YOUR TASKS ---")

        if len(tasks) == 0:

            print("📭 No tasks available.")

        else:

            for i, task in enumerate(tasks, start=1):

                if task["completed"]:
                    status = " Completed"
                else:
                    status = " Pending"

                print(i, ".", task["name"], "-", status)


    # ======================================
    # 3. MARK TASK AS COMPLETED
    # ======================================

    elif choice == "3":

        if len(tasks) == 0:

            print("\n No tasks available.")

        else:

            print("\n--- MARK TASK AS COMPLETED ---")

            for i, task in enumerate(tasks, start=1):

                print(i, ".", task["name"])

            try:

                task_number = int(
                    input("\nEnter task number to complete: ")
                )

                if 1 <= task_number <= len(tasks):

                    tasks[task_number - 1]["completed"] = True

                    print(" Task marked as completed!")

                else:

                    print(" Invalid task number.")

            except ValueError:

                print(" Please enter a number.")


    # ======================================
    # 4. DELETE TASK
    # ======================================

    elif choice == "4":

        if len(tasks) == 0:

            print("\n📭 No tasks to delete.")

        else:

            print("\n--- DELETE TASK ---")

            for i, task in enumerate(tasks, start=1):

                print(i, ".", task["name"])

            try:

                task_number = int(
                    input("\nEnter task number to delete: ")
                )

                if 1 <= task_number <= len(tasks):

                    deleted_task = tasks.pop(task_number - 1)

                    print(
                        "deleted",
                        deleted_task["name"],
                        "deleted successfully!"
                    )

                else:

                    print(" Invalid task number.")

            except ValueError:

                print(" Please enter a number.")


    # ======================================
    # 5. SEARCH TASK
    # ======================================

    elif choice == "5":

        print("\n--- SEARCH TASK ---")

        search = input("Enter task name to search: ").lower()

        found = False

        for task in tasks:

            if search in task["name"].lower():

                if task["completed"]:
                    status = " Completed"
                else:
                    status = " Pending"

                print(task["name"], "-", status)

                found = True

        if found == False:

            print(" Task not found.")


    # ======================================
    # 6. CLEAR ALL TASKS
    # ======================================

    elif choice == "6":

        if len(tasks) == 0:

            print("\n Task list is already empty.")

        else:

            confirm = input(
                "Are you sure you want to delete all tasks? (yes/no): "
            ).lower()

            if confirm == "yes":

                tasks.clear()

                print(" All tasks deleted!")

            else:

                print("Clear cancelled.")


    # ======================================
    # 7. EXIT
    # ======================================

    elif choice == "7":

        print("\n===================================")
        print("Thank you for using My To-Do List! ")
        print("===================================")

        break


    # ======================================
    # INVALID OPTION
    # ======================================

    else:

        print(" Invalid choice!")
        print("Please select a number from 1 to 7.")