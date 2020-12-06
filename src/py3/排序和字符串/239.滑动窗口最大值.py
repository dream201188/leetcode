#
# @lc app=leetcode.cn id=239 lang=python
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution(object):
    """
    暴力办法超时
    """
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        if not length or not k:
            return []

        return [max(nums[i:i + k]) for i in range(n - k + 1)]

    """
    双端队列办法，队列维护一个最大的值的索引；
    添加一个值之前，比他小的都要被移除掉，然后再添加这个值
    """
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        if not n or not k:
            return []

        if k == 1:
            return nums

        from collections import deque
        def clean_queue(i):
            if deq and deq[0] <= i - k:
                deq.popleft()

            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

        ans = []
        deq = deque()
        for i in range(n):
            clean_queue(i)
            deq.append(i)
            if i >= k - 1:
                ans.append(nums[deq[0]])
        return ans

    """
    不需要双端队列的算法
    """
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        if not n or not k:
            return []

        if k == 1:
            return nums

        left, right = [float('-inf')] * n, [float('-inf')] * n
        left[0], right[n - 1] = nums[0], nums[n-1]

        for i in range(1, n):
            if i % k  == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])

            j = n - 1 - i
            if (j + 1) % k  == 0:
                right[j] = nums[j]
            else:
                right[j] = max(right[j + 1], nums[j])
        ans = []
        for i in range(n - k + 1):
            ans.append(max(right[i], left[i + k - 1]))

        return ans



# @lc code=end

