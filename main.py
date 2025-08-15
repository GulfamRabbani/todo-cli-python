# Simple To-Do CLI Application

todo_list = []

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        todo_list.append(task)
        print(f"✅ Task '{task}' added!")
    
    elif choice == "2":
        if not todo_list:
            print("📭 No tasks yet!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")
    
    elif choice == "3":
        if not todo_list:
            print("📭 No tasks to remove!")
        else:
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter task number to remove: "))
                removed = todo_list.pop(task_num - 1)
                print(f"🗑 Task '{removed}' removed!")
            except (ValueError, IndexError):
                print("❌ Invalid task number!")
    
    elif choice == "4":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice! Please try again.")
