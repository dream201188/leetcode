class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False

        return n & (n - 1) == 0

    def isPowerOfTwo(self, n):
        if n == 0:
            return False

        return n & -n == n


