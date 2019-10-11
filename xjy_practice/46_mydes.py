import time
import os
import pickle


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


class MyDes:
    saved = []

    def __init__(self, name=None):
        self.name = name
        self.filename = self.name + '.pkl'

    def __get__(self, instance, owner):
        if self.name not in MyDes.saved:
            raise AttributeError('no attribute {}'.format(self.name))

        with open(self.filename, 'rb') as f:
            value = pickle.load(f)

        return value

    def __set__(self, instance, value):
        with open(self.filename, 'wb') as f:
            pickle.dump(value, f)
            MyDes.saved.append(self.name)

    def __delete__(self, instance):
        os.remove(self.filename)
        MyDes.saved.remove(self.name)


class Test:
    a = Record(1, 'rec')
    x = a
    d = MyDes('d')
    e = MyDes('e')



if __name__ == '__main__':
    c = Test()
    print(c.x)
    print(c.a)
    c.x = 1000
    print(c.x)
