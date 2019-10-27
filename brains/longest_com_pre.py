class Solution:
    def longestCommonPrefix(self, strs) -> str:
        out_i = 0
        try:
            while True:
                com_c = strs[0][out_i]
                for i in range(1, len(strs)):
                    if not strs[i][out_i] == com_c:
                        if out_i == 0:
                            return ''
                        else:
                            return strs[0][0:out_i]
                else:
                    out_i += 1
        except IndexError:
            if out_i == 0:
                return ''
            else:
                return strs[0][0:out_i]


testcase = ["flower", "flow", "flight"]
a = Solution()
print(a.longestCommonPrefix(testcase))
