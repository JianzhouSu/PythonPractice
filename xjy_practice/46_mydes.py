import time


class Record:
    def __init__(self, initval=None, name=None):
        self.val = initval
        self.name = name
        self.filename = 'record.txt'

    def __get__(self, instance, owner):
        with open(self.filename, 'a', encoding='urf-8') as f:
            f.write('{}{}{}{}{}'.format(self.name, time.ctime(), self.name, 'read as ', str(self.val)))

        return self.val

    def __set__(self, instance, value):
        filename = '%s_record.txt' % self.name
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write('{}{}{}{}{}'.format(self.name, time.ctime(), self.name, 'set as ', str(value)))

        self.val = value
