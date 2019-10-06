class Demo:
    def __getattr__(self, item):
        self.item = 'fish'
        return self.item


class Counter:
    def __init__(self):
        super().__setattr__('counter', 0)

    def __setattr__(self, key, value):
        super().__setattr__('counter', self.counter + 1)
        super().__setattr__(key, value)

    def __delattr__(self, item):
        super().__setattr__('counter', self.counter - 1)
        super().__delattr__(item)


if __name__ == '__main__':
    d = Demo()
    d.x
    d.x = 'Xman'
    d.x
