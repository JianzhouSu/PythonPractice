import time


class Record:
    def __init__(self, initval=None, name=None):
        self.val = initval
        self.name = name
        self.filename = 'record.txt'

    def __get__(self, instance, owner):
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write('\n{} {} {} {} {}'.format(self.name, time.ctime(), self.name, 'read as ', str(self.val)))

        return self.val

    def __set__(self, instance, value):
        filename = '%s_record.txt' % self.name
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write('\n{} {} {} {} {}'.format(self.name, time.ctime(), self.name, 'set as ', str(value)))

        self.val = value


class Test:
    a = Record(1, 'rec')
    x = a


c = Test()
print(c.x)
print(c.a)
c.x = 1000
print(c.x)
