#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start

from typing import List


class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        if length == 0:
            digits = []
        if length >= 1:
            digits[length - 1] = digits[length - 1] + 1
            for i in range(length - 1, -1, -1):
                if digits[i] == 10:
                    if i == 0:
                        temp = [0] * (length + 1)
                        temp[0] = 1
                        digits = temp
                    else:
                        digits[i] = 0
                        digits[i - 1] = digits[i - 1] + 1
                else:
                    break

        return digits


if __name__ == "__main__":
    solution = Solution()
    print(solution.plusOne([9, 8, 9]))

# @lc code=end
