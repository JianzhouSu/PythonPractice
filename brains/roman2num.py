class Solution:
    @staticmethod
    def romanToInt(s: str) -> int:
        al2num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        output = 0
        leng = len(s)
        for i in range(leng):
            if i + 1 >= leng or al2num[s[i]] >= al2num[s[i + 1]]:
                output += al2num[s[i]]
            else:
                output -= al2num[s[i]]

        return output


testcase = 'D'

print(Solution.romanToInt(testcase))
