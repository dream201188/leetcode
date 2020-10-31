class Solution(object):

    def fib(self, N):
        """
        :type N: int
        :rtype: int
        傻递归方式，无任何优化，复杂度指数级，2**N
        """
        if N < 2:
            return N
        return self.fib(N - 1) + self.fib(N - 2)

    def fib(self, N):
        """
        递归：采用缓存结果的方式优化，时间复杂度n，空间复杂度 n+1
        """
        m = [0] * (N + 1)
        n = N

        def fibr(n, m):
            if n < 2:
                return n
            if m[n] == 0:
                m[n] = fibr(n - 1, m) + fibr(n - 2, m)
            return m[n]

        return fibr(n, m)

    def fib(self, N):
        """
        动态规划：dp方式优化，时间复杂度n，空间复杂度 n+1
        """
        n = N
        if n <= 1:
            return n

        a = [0] * (n + 1)
        a[0], a[1] = 0, 1
        for i in range(2, n + 1, 1):
            a[i] = a[i - 1] + a[i - 2]
        return a[n]

    def fib(self, N):
        """
        动态规划：dp方式优化，时间复杂度n，空间复杂度 2
        """
        n = N
        if n <= 1:
            return n
        a, b = 0, 1
        for i in range(2, n + 1, 1):
            b, a = a + b, b
        return b
