class CountList(list):
    def __init__(self, *args):
        super(CountList, self).__init__(args)
        self.count = []
        for i in args:
            self.count.append(0)

    def __len__(self):
        return len(self.count)

    def __getitem__(self, item):
        self.count[item] += 1
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        self.count[key] += 1
        return super(CountList, self).__setitem__(key, value)

    def __delitem__(self, key):
        del self.count[key]
        return super(CountList, self).__delitem__(key)

    def counter(self, key):
        return self.count[key]

    def append(self, args):
        self.count.append(0)
        super(CountList, self).append(args)

    def pop(self, key=-1):
        del self.count[key]
        return super(CountList, self).pop(key)

    def remove(self, *args):
        for i in args:
            key = super().index(i)
            del self.count[key]
        return super(CountList, self).remove(*args)

    def insert(self, *args, **kwargs):
        self.count.insert(args[0], 0)
        return super(CountList, self).insert(*args, **kwargs)

    def clear(self, *args, **kwargs):
        self.count.clear()
        return super(CountList, self).clear(*args, **kwargs)

    def reverse(self, *args, **kwargs):
        self.count.reverse()
        return super(CountList, self).reverse(*args, **kwargs)


if __name__ == '__main__':
    c1 = CountList(1, 3, 5, 7, 9)
    c2 = CountList(2, 4, 6, 8, 10)
