from src.task.Task import Task


class Node:

    def __init__(self, processing_power: int):
        self.processing_power = processing_power
        self.tasks_ready = []
        self.tasks_finished = []

    def register_ready_task(self, task: Task):
        self.tasks_ready.append(task)

    def process_one_tick(self):
        if not self.is_processing_left():
            return

        units_left = self.processing_power
        for task in self.tasks_ready[:]:
            if units_left < 1:
                break
            units_left = task.execute(units_left)
            if task.is_finished():
                self.__task_finished(task)

    def is_processing_left(self):
        return len(self.tasks_ready) > 0

    def __task_finished(self, task: Task):
        self.tasks_finished.append(task)
        self.tasks_ready.remove(task)
