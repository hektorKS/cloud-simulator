import math

from src.bimodal.Generator import Generator
from src.task.Task import Task


class TasksGenerator:

    def __init__(self, length_generator: Generator, posting_time_generator: Generator):
        self.length_generator = length_generator
        self.posting_time_generator = posting_time_generator

    def generate_tasks(self):
        tasks = []
        lengths = self.length_generator.generate().tolist()
        posting_times = self.posting_time_generator.generate().tolist()

        lengths = list(map(lambda item: int(math.fabs(item)), lengths))
        posting_times = list(map(lambda item: int(math.fabs(item)), posting_times))

        tasks_count = len(lengths)
        for index in range(tasks_count):
            tasks.append(Task(lengths[index], posting_times[index]))
        return tasks
