class SStr(str):
    def __sub__(self, other):
        flag_dismatch = 0
        nl_dis = []
        for i in range(len(self)):
            if self[i] == other[i]:
                pass
            else:
                nl_dis.append(i)


if __name__ == '__main__':
    str1 = SStr('abc')
