from src.task.Clock import Clock
from src.task.TaskIdGenerator import TaskIdGenerator


class Task:

    def __init__(self, length: int, posting_time: int):
        self.id = TaskIdGenerator.generate()
        self.length = length
        self.posting_time = posting_time
        self.units_processed = 0
        self.end_time = -1

    def __str__(self):
        return 'Task(id={}, length={}, posting_time={}, units_processed={}, end_time={})'\
            .format(self.id, self.length, self.posting_time, self.units_processed, self.end_time)

    def __repr__(self):
        return self.__str__()

    def is_ready_to_start(self):
        return Clock.get_current_time() >= self.posting_time

    def is_finished(self):
        return self.end_time != -1

    def execute(self, processing_units: int):
        if processing_units >= self.length - self.units_processed:
            units_left = processing_units - (self.length - self.units_processed)
            units_used = processing_units - units_left
            self.units_processed = self.units_processed + units_used
            self.end_time = Clock.get_current_time()
            print('Processing finished: {}'.format(self))
            return units_left
        else:
            self.units_processed = self.units_processed + processing_units
            return 0
