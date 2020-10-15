#
# @lc app=leetcode.cn id=7 lang=python
#
# [7] 整数反转
#


# @lc code=start
class Solution:

    def reverse(self, x):
        if x < 0:
            y = '-' + str(-x)[::-1]
        else:
            y = str(x)[::-1]
        res = int(y)
        if res > pow(2, 31) - 1 or res < pow(-2, 31):
            return 0
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse(123))

# @lc code=end
