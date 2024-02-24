logo = '''
╔════╗      ╔╗        ╔╗        ╔╗ 
║╔╗╔╗║      ║║        ║║       ╔╝╚╗
╚╝║║╚╝╔══╗╔═╝║╔══╗    ║║ ╔╗╔══╗╚╗╔╝
  ║║  ║╔╗║║╔╗║║╔╗║    ║║ ╠╣║ ═╣ ║║ 
 ╔╝╚╗ ║╚╝║║╚╝║║╚╝║    ║╚╗║║╠═ ║ ║╚╗
 ╚══╝ ╚══╝╚══╝╚══╝    ╚═╝╚╝╚══╝ ╚═╝
                                   
'''


tasks = []
unique_tasks = set()

def add_task(task):
    if task not in unique_tasks:
        tasks.append(task)
        unique_tasks.add(task)
        print("Task added successfully!")
    else:
        print("Task already exists!")
    display_tasks()

def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        completed_task = tasks.pop(task_index)
        unique_tasks.remove(completed_task)
        print("Task marked as completed!")
    else:
        print("Invalid task index.")
    display_tasks()

def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        deleted_task = tasks.pop(task_index)
        unique_tasks.remove(deleted_task)
        print("Task deleted successfully!")
    else:
        print("Invalid task index.")
    display_tasks()

def display_tasks():
    if tasks:
        print("\n\n\n\nTo-Do List:\n")
        for index, task in enumerate(tasks):
            print(f"{index}. {task}")
        print('\n\n\n')
    else:
        print("\n\nNo tasks found.\n\n")

if __name__ == "__main__":
    
    print(logo)
    while True:
        print("\n1. Add Task")
        print("2. Complete Task")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            add_task(task)
        elif choice == '2':
            task_index = int(input("Enter task index to mark as completed: "))
            complete_task(task_index)
        elif choice == '3':
            task_index = int(input("Enter task index to delete: "))
            delete_task(task_index)
        
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


    
