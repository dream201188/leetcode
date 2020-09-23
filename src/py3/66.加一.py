#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start

from typing import List


class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:

        if (digits is None) or (len(digits) == 0):
            return []

        length = len(digits)
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


# @lc code=end
