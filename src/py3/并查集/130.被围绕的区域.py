class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return 0

        m, n = len(board), len(board[0])

        p = [i for i in range(m * n + 1)]
        target_group = m * n

        def node(i, j):
            return i * n + j

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    if i in [0, m - 1] or j in [0, n - 1]:
                        self.union(p, node(i, j), target_group)
                    else:
                        for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                            if -1 < i + x < m and -1 < j + y < n and board[i + x][j + y] == 'O':
                                self.union(p, node(i, j), node(i + x, j + y))

        for i in range(m):
            for j in range(n):
                if self.parent(p, node(i, j)) != self.parent(p, target_group):
                    board[i][j] = 'X'
                else:
                    board[i][j] = 'O'


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
