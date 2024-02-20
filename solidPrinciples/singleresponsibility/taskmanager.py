
"""
    Todo Task Manager has only one responsibility of adding and removing the task. So it follows SRP as it has only one reason to change the class
"""

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task):
        self.tasks.remove(task)


        