class Task:
    def __init__(self, title, description="", status="incomplete"):
        # Constructor to initialize the task with title, description, and status
        self.title = title
        self.description = description
        self.status = status

    def mark_complete(self):
        # Method to mark a task as complete
        self.status = "complete"

    def display_task(self):
        # Method to display task details in a user-friendly format
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Status: {self.status}")

    def __str__(self):
        # Method to customize the string representation of the object
        return f"Title: {self.title}, Description: {self.description}, Status: {self.status}"


class TaskList:
    def __init__(self):
        # Constructor to initialize the TaskList with an empty list of tasks
        self.tasks = []

    def add_task(self, title, description="", status="incomplete"):
        # Method to add tasks to the TaskList (method overloading)
        new_task = Task(title, description, status)
        self.tasks.append(new_task)

    def remove_task(self, title):
        # Method to remove tasks from the TaskList
        self.tasks = [task for task in self.tasks if task.title != title]

    def list_all_tasks(self):
        # Method to list all tasks in the TaskList
        for task in self.tasks:
            print(task)

    def find_task_by_title(self, title):
        # Method to find a task by title in the TaskList
        for task in self.tasks:
            if task.title == title:
                return task
        return None


class PriorityTask(Task):
    def __init__(self, title, description="", status="incomplete", priority="low"):
        # Constructor to initialize a PriorityTask, inheriting from Task
        super().__init__(title, description, status)
        self.priority = priority

    def display_task(self):
        # Method overriding to customize the display of PriorityTask
        super().display_task()
        print(f"Priority: {self.priority}")

    def __str__(self):
        # Method overriding to customize the string representation of PriorityTask
        return f"{super().__str__()}, Priority: {self.priority}"


# Example Usage
if __name__ == "__main__":
    task_list = TaskList()

    # Adding tasks using different ways (method overloading)
    task_list.add_task("Complete Assignment")
    task_list.add_task("Read Book", "Read 'The Great Gatsby'")
    task_list.add_task("Exercise", status="in progress")

    # Display all tasks
    print("All Tasks:")
    task_list.list_all_tasks()

    # Find and mark a task as complete
    found_task = task_list.find_task_by_title("Read Book")
    if found_task:
        found_task.mark_complete()

    # Remove a task
    task_list.remove_task("Exercise")

    # Create a PriorityTask
    priority_task = PriorityTask("Finish Project", "Finish by Friday", priority="high")

    # Display PriorityTask details
    print("\nPriority Task Details:")
    priority_task.display_task()
