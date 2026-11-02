class Task:
    def __init__(self, name, description, deadline, state):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.state = state
    def get_info(self):
        return f"Task: {self.name}, {self.description}, {self.deadline}, {self.state}"

class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self, name, description, deadline, state):

     def show_tasks(self):
        for task in self.tasks:
            print(task.get_info())

Project1 = Task(name = "Project1", description = "team biology project", deadline = "05.11", state = "done")
CleanUp = Task(name = "CleanUp", description = "Clean my room and cook dinner", deadline = "tomorrow", state = "not done")

print(Project1.get_info())
print(CleanUp.get_info())