class Solution:
    def isValid(self, s: str) -> bool:
        back = {')': '(', ']': '[', '}': '{'}
        stack = []
        for each in s:
            if each in '{([':
                stack.append(each)
            elif each in '})]':
                if stack[-1] == back[each]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False


testcase = '(){}[]'
a = Solution()
print(a.isValid(testcase))