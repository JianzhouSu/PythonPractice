# alist = range(5)
# it = iter(alist)
#
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         break
#

# import datetime as dt
#
#
# class LeapYear:
#     def __init__(self):
#         self.now = dt.date.today().year
#
#     def is_leap_year(self, year):
#         if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#             return True
#         else:
#             return False
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while not self.is_leap_year(self.now):
#             self.now -= 1
#         temp = self.now
#         self.now -= 4
#         return temp


class MyRev:
    def __init__(self, strings):
        self.now_in = -1
        self.strings = strings

    def __iter__(self):
        return self

    def __next__(self):
        try:
            temp = self.strings[self.now_in]
            self.now_in -= 1
            return temp
        except IndexError:
            raise StopIteration
