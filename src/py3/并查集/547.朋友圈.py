class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M:
            return 0
        m = len(M)
        p = [i for i in range(m)]
        for i in range(m):
            for j in range(i + 1, m):
                if M[i][j] == 1:
                    self.union(p, i, j)
        return len(set([self.parent(p, i) for i in range(m)]))

    def union(self, p, i, j):
        p1 = self.parent(p, i)
        p2 = self.parent(p, j)
        p[p2] = p1

    def parent(self, p, i):
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != i:
            x = i; i = p[i]; p[x] = root;
        return root

