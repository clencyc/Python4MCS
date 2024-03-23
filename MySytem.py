class Node:
    """
    Represents a single task node in the linked list.
    """
    def __init__(self, data):
        self.data = data  # Task description
        self.due_date = None  # Optional due date (string)
        self.priority = None  # Optional priority level (e.g., "high", "medium", "low")
        self.next = None  # Pointer to the next node in the list

class ToDoList:
    """
    Implements a to-do list using a linked list.
    """
    def __init__(self):
        self.head = None  # Head of the linked list

    def is_empty(self):
        """
        Checks if the to-do list is empty.

        Returns:
            bool: True if the list is empty, False otherwise.
        """
        return self.head is None

    def add_task(self, task, due_date=None, priority=None):
        """
        Adds a new task to the end of the list.

        Args:
            task (str): The task description.
            due_date (optional): The due date for the task (string).
            priority (optional): The priority level of the task (e.g., "high", "medium", "low").
        """
        new_node = Node(task)
        new_node.due_date = due_date
        new_node.priority = priority

        if self.is_empty():
            self.head = new_node
        else:
            # Traverse to the last node
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def print_list(self):
        """
        Prints the tasks in the list along with their due dates and priorities (if set).
        """
        if self.is_empty():
            print("No tasks in the list.")
            return

        cur = self.head
        while cur:
            print(f"- {cur.data}")
            if cur.due_date:
                print(f"  Due date: {cur.due_date}")
            if cur.priority:
                print(f"  Priority: {cur.priority}")
            print()
            cur = cur.next

    def update_task(self, task_description, new_data, new_due_date=None, new_priority=None):
        """
        Updates an existing task in the list.

        Args:
            task_description (str): The description of the task to be updated.
            new_data (str): The new data for the task.
            new_due_date (optional): The new due date for the task (string).
            new_priority (optional): The new priority level of the task (e.g., "high", "medium", "low").

        Returns:
            bool: True if the task is updated successfully, False otherwise.
        """
        if self.is_empty():
            return False

        cur = self.head
        while cur:
            if cur.data == task_description:
                cur.data = new_data
                cur.due_date = new_due_date
                cur.priority = new_priority
                return True
            cur = cur.next
        return False

    def delete_task(self, task_description):
        """
        Deletes a task from the list.

        Args:
            task_description (str): The description of the task to be deleted.

        Returns:
            bool: True if the task is deleted successfully, False otherwise.
        """
        if self.is_empty():
            return False

        prev = None
        cur = self.head
        while cur:
            if cur.data == task_description:
                if not prev:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                return True
            prev = cur
            cur = cur.next
        return False


# Example usage
todo_list = ToDoList()

todo_list.add_task("Buy groceries")
todo_list.add_task("Finish project report", due_date="2024-03-31", priority="high")
todo_list.add_task("Clean the house", priority="medium")
print("To-do-list")

print("To-Do-List")
