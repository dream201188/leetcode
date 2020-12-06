class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 2:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            b, a = a + b, b
        return b % 1000000007


    def fib(self, n):
        if n <= 1:
            return n

        a, b = 0, 1
        for i in range(2, n + 1):
            b, a = a + b, b
        return b

if __name__ == "__main__":
    s = Solution()
    for i in range(9):
        print('fib %d: %d' %(i, s.fib(i)))
