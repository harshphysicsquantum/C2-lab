import database
database.init_db()


print("==============================")
print("       C2-Lab Console")
print("==============================")
print("1. Add a task")
print("2. View pending tasks")
print("3. Process next task")
print("4. Exit")
print("==============================")
choice = input("Enter your choice: ")

if (choice == '1'):
    print("Adding a new task....")
    task = input("Enter task type: ")
    task_id = database.add_task(task)
    print(f"Task ID: {task_id}")

elif choice == '2':
    print("Viewing pending tasks....")
    pending_task = database.get_pending_tasks()

    if not pending_task:
        print("No pending tasks.")
    else:
        for task in pending_task:
            print(f"Task ID: {task[0]} | Type: {task[1]} | Status: {task[2]} | Created: {task[3]}")

elif choice == '3':
    print("Processing next data")
    next_pending_task = database.get_next_pending_task()
    if not next_pending_task:
        print("No pending tasks.")
    else:
        print(f"Task ID: {next_pending_task[0]} | Type: {next_pending_task[1]} | Status: {next_pending_task[2]} | Created: {next_pending_task[3]}")
        database.update_task_status(next_pending_task[0], "running")
            

else:
    print("Invalid choice")