import json
import os

class PersistentTaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.next_id = 1
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    self.tasks = data.get("tasks", [])
                    self.next_id = data.get("next_id", 1)
                print(f"Loaded {len(self.tasks)} tasks from {self.filename}.")
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading tasks: {e}. Starting with empty list.")
        else:
            print("No saved tasks found. Starting fresh.")

    def save_tasks(self):
        try:
            data = {
                "tasks": self.tasks,
                "next_id": self.next_id
            }
            with open(self.filename, 'w') as f:
                json.dump(data, f, indent=4)
            print("Tasks saved successfully.")
        except IOError as e:
            print(f"Error saving tasks: {e}")

    def create_task(self, title, description):
        task = {
            "id": self.next_id,
            "title": title,
            "description": description,
            "status": "Pending"
        }
        self.tasks.append(task)
        self.next_id += 1
        print(f"Task '{title}' created successfully.")
        self.save_tasks()

    def read_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        
        print("\n--- Task List ---")
        for task in self.tasks:
            print(f"ID: {task['id']} | Title: {task['title']} | Status: {task['status']}")
            print(f"Description: {task['description']}")
            print("-" * 20)

    def update_task(self, task_id, new_status):
        for task in self.tasks:
            if task['id'] == task_id:
                task['status'] = new_status
                print(f"Task {task_id} updated to '{new_status}'.")
                self.save_tasks()
                return
        print(f"Task with ID {task_id} not found.")

    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                del self.tasks[i]
                print(f"Task {task_id} deleted successfully.")
                self.save_tasks()
                return
        print(f"Task with ID {task_id} not found.")

def main():
    manager = PersistentTaskManager()
    
    while True:
        print("\n--- Persistent Task Manager Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task Status")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter task title: ")
            desc = input("Enter task description: ")
            manager.create_task(title, desc)
        elif choice == '2':
            manager.read_tasks()
        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to update: "))
                status = input("Enter new status (e.g., Completed, In Progress): ")
                manager.update_task(task_id, status)
            except ValueError:
                print("Invalid input. ID must be a number.")
        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to delete: "))
                manager.delete_task(task_id)
            except ValueError:
                print("Invalid input. ID must be a number.")
        elif choice == '5':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
