#
# @lc app=leetcode.cn id=155 lang=python
#
# [155] 最小栈
#

# @lc code=start
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.repo = list()
        self.min = float('inf')
        self.not_pop = True

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.repo.append(x)
        if self.not_pop and x < self.min:
            self.min = x



    def pop(self):
        """
        :rtype: None
        """
        self.repo.pop()
        self.not_pop = False



    def top(self):
        """
        :rtype: int
        """
        return self.repo[-1]



    def getMin(self):
        """
        :rtype: int
        """
        if self.not_pop:
            return self.min

        self.not_pop = True
        self.min  = float('inf')
        for num in self.repo:
            if num < self.min:
                self.min = num
        return self.min



class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.repo = list()


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.repo:
            min_x = x
        else:
            min_x = min(self.repo[-1][1], x)

        self.repo.append((x, min_x))



    def pop(self):
        """
        :rtype: None
        """
        self.repo.pop()



    def top(self):
        """
        :rtype: int
        """
        return self.repo[-1][0]



    def getMin(self):
        """
        :rtype: int
        """
        return self.repo[-1][1]




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

