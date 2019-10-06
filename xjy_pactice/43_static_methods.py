class Count:
    def __init__(self, *args):
        li = args
        print(len(li))


class Word(str):
    def __new__(cls, word):
        if ' ' in word:
            print('Containing spaces, truncating to first word')
            word = word[:word.index(' ')]
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __le__(self, other):
        return len(self) <= len(other)


if __name__ == '__main__':
    c = Count(1, 2, 3)
    aw = Word('abcd')
    bw = Word('efg hij')
    print(aw > bw)