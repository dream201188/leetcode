#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []

        if (nums is None) or (n < 3):
            return res

        nums.sort()
        for i in range(n):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i - 1] == nums[i]:
                i += 1
                continue

            l = i + 1
            r = n - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif sum > 0:
                    r -= 1
                else:
                    l += 1

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([1, -1, -1, 0]))

# @lc code=end
