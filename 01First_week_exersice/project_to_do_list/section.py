class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        filtered_task = [x for x in self.tasks if x == new_task]
        if filtered_task:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name):
        filtered_task = [x for x in self.tasks if x.name == task_name]
        if filtered_task:
            task_to_complete = filtered_task[0]
            task_to_complete.completed = True
            return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        removed_task = 0
        for task_to_remove in self.tasks:
            if task_to_remove.completed:
                self.tasks.remove(task_to_remove)
                removed_task += 1
        return f"Cleared {removed_task} tasks."

    def view_section(self):
        res = f"Section {self.name}:\n"
        for s in self.tasks:
            res += f"{s.details()}\n"
        return res


# task = Task("Make bed", "27/05/2020")
# print(task.change_name("Go to University"))
# print(task.change_due_date("28.05.2020"))
# task.add_comment("Don't forget laptop")
# print(task.edit_comment(0, "Don't forget laptop and notebook"))
# print(task.details())
# section = Section("Daily tasks")
# print(section.add_task(task))
# second_task = Task("Make bed", "27/05/2020")
# section.add_task(second_task)
# print(section.clean_section())
# print(section.view_section())
