import math
import random

from src.bimodal.DistributionGenerator import DistributionGenerator
from src.task.Task import Task


class TasksGenerator:

    def __init__(self, length_generator: DistributionGenerator, tasks_number_generator: DistributionGenerator):
        self.length_generator = length_generator
        self.tasks_number_generator = tasks_number_generator

    def generate_tasks(self, expected_tasks_number: int = 10000, delta_time: int = 1000):
        tasks = []
        tasks_numbers = self.tasks_number_generator.generate().tolist()
        tasks_numbers = TasksGenerator.__make_positive(tasks_numbers)

        current_posting_time = 0
        while len(tasks) < expected_tasks_number:
            self.length_generator.set_number_of_elements(random.choice(tasks_numbers))
            lengths = self.__generate_lengths()

            for length in lengths:
                if len(tasks) == expected_tasks_number:
                    break
                tasks.append(Task(length, current_posting_time + random.randint(0, delta_time - 1)))
            current_posting_time = current_posting_time + delta_time

        return tasks

    def __generate_lengths(self, ):
        lengths = self.length_generator.generate().tolist()
        return TasksGenerator.__make_positive(lengths)

    @staticmethod
    def __make_positive(collection: list):
        return list(map(lambda item: int(math.fabs(item)), collection))
