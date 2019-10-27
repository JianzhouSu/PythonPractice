class Solution:

    def longestPalindrome(self, s: str) -> str:

        r_odd_max = 0
        r_even_max = 0
        cen_even_max = 0
        s_len = len(s)
        if s_len < 1:
            return ''

        # even
        cen = 0
        r = 0
        while cen - r >= 0 and cen + r + 1 < len(s):
            while cen - r >= 0 and cen + r + 1 < len(s) and s[cen - r] == s[cen + 1 + r]:
                r += 1
            if r > r_even_max:
                r_even_max = r
                cen_even_max = cen
            r = 0
            cen += 1

        # odd
        cen = 0
        r = 0
        while cen - r >= 0 and cen + r < len(s):
            while cen - r >= 0 and cen + r < len(s) and s[cen - r] == s[cen + r]:
                r += 1
            if r > r_odd_max:
                r_odd_max = r
                cen_odd_max = cen
            r = 1
            cen += 1

        if r_even_max >= r_odd_max:
            return s[(cen_even_max + 1 - r_even_max):(cen_even_max + r_even_max + 1)]
        else:
            return s[(cen_odd_max + 1 - r_odd_max):(cen_odd_max + r_odd_max)]


a = Solution()
print(a.longestPalindrome('adbbabbbb'))
