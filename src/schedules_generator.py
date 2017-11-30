from random import randint


class SchedulesGenerator:

    def __init__(self, pois):
        self.pois = pois

    def generate(self):
        schedule_length = randint(1, 10)
        return [self.pois[randint(0, len(self.pois)-1)] for _ in range(schedule_length)]