class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])


        p = [-1 for i in range(m * n)]

        for i in range(m):
            for j in range(n):
                if '1' == grid[i][j]:
                    p[i * n + j] = i * n + j

        for i in range(m):
            for j in range(n):
                if '1' == grid[i][j]:
                    grid[i][j] = "0"
                    for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        if -1 < i + x < m and -1 < j + y < n and grid[i + x][j + y] == '1':
                            self.union(p, i * n + j, (i + x) * n + (j + y))

        return len(set([self.parent(p, i) for i in range(m*n)]) - set([-1]))

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
