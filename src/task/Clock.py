class Clock:
    __current_time = 0

    @staticmethod
    def tick(value: int):
        Clock.__current_time = Clock.__current_time + value

    @staticmethod
    def get_current_time():
        return Clock.__current_time

    @staticmethod
    def reset():
        Clock.__current_time = 0
