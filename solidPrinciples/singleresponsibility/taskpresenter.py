''' using static method here because display method itself doesn't hold variable of tasks. it will just be given the task'''

class TaskPresenter:
    @staticmethod
    def display_tasks(tasks):
        for task in tasks:
            print(task)

