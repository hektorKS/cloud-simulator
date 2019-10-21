class TaskIdGenerator:
    __value = 0

    @staticmethod
    def generate():
        generated = TaskIdGenerator.__value
        TaskIdGenerator.__value = TaskIdGenerator.__value + 1
        return generated
