#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)

    def myAtoi(self, s: str) -> int:
        matches = re.match('([\+\-]?\d+)', s.lstrip())
        if not matches:
            return 0
        ans = int(matches.group(1))
        ans = max(min(ans, 2**31 - 1), -2**31)
        return ans

    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        i, n = 0, len(s)

        while i < n and ' ' == s[i]:
            i += 1

        sign = 1
        if i < n and '+' == s[i]:
            i += 1

        elif i < n and '-' == s[i]:
            i += 1
            sign = -1

        ans = 0
        while i < n and ord('0') <= ord(s[i]) <= ord('9'):
            ans = 10 * ans + int(s[i])
            i += 1

        ans *= sign
        return max(min(ans, 2 ** 31 - 1), -2 ** 31)


if __name__ == "__main__":
    s = Solution()
    s.myAtoi(" ")





# @lc code=end

