import time as t


class MyTimer:
    def __init__(self):
        self.unit = ['year', 'month', 'day', 'Hour', 'minute', 'second']
        self.borrow = [0, 12, 31, 24, 60, 60]
        self.prompt = 'haven\'t start yet'
        self.lasted = []
        self.begin = 0
        self.stop = 0

    def __str__(self):
        return self.prompt

    __repr__ = __str__()

    def __add__(self, other):
        prompt = 'totally run for '
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])
        return prompt

    def start(self):
        self.begin = t.localtime()
        self.prompt = 'use stop before start'
        print('timer start')

    def stop(self):
        if not self.begin:
            print('use start before stop')
        else:
            self.end = t.localtime()
            self._calc()
            print('stop timer')

    def _calc(self):
        self.lasted = []
        self.prompt = 'totally run for '
        for index in range(6):
            temp = self.end[index] - self.begin[index]
