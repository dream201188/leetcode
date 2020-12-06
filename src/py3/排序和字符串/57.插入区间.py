#
# @lc app=leetcode.cn id=57 lang=python
#
# [57] 插入区间
#

# @lc code=start
class Solution(object):

    #我自己写的排序要更简单明了
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        left, right = newInterval
        ans = []

        for interval in intervals:
            li, ri = interval
            if ri < left or li > right:
                ans.append(interval)
            else:
                left = min(li, left)
                right = max(ri, right)
        ans.append([left, right])
        ans.sort(key=lambda x: x[0])

        return ans

    """
    不用最后排序，本身有有序，所以如果li right了，后面肯定都大
    """
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        left, right = newInterval
        ans = []
        placed = False
        for interval in intervals:
            li, ri = interval
            if ri < left:
                 ans.append(interval)

            elif li > right:
                if not placed:
                    ans.append([left, right])
                    placed = True
                ans.append(interval)
            else:
                left = min(li, left)
                right = max(ri, right)

        if not placed:
            ans.append([left, right])

        return ans

    """
    不用最后排序，本身有有序，所以如果li right了，后面肯定都大,不用继续循环了就
    """
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        left, right = newInterval
        ans = []
        placed = False
        for i, interval in enumerate(intervals):
            li, ri = interval
            if ri < left:
                 ans.append(interval)

            elif li > right:
                if not placed:
                    ans.append([left, right])
                    placed = True
                ans.extend(intervals[i:])
                break
            else:
                left = min(li, left)
                right = max(ri, right)

        if not placed:
            ans.append([left, right])

        return ans


# @lc code=end

