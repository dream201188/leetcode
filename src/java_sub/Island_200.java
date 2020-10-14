package java_sub;

/*
连成一片的也叫岛屿，连成一片就是用图的办法可以访问到，也就是说可以遍历，可以遍历几次就是有几片也即是有几个岛屿；
本方法使用深度遍历的方法
*/
public class Island_200 {
    public int numIslands(char[][] grid) {
        int count = 0;
        int nr = grid.length;
        if (grid == null || nr == 0) {
            return count;
        }
        int nc = grid[0].length;

        for (int i = 0; i < nr; i++) {
            for (int j = 0; j < nc; j++) {
                if (grid[i][j] == '1') {
                    count++;
                    dfs(grid, nr, nc, i, j);
                }
            }
        }

        return count;
    }

    private void dfs(char[][] grid, int nr, int nc, int r, int c) {
        if (r < 0 || c < 0 || r >= nr || c >= nc || grid[r][c] == '0') {
            return;
        }

        grid[r][c] = '0'; // 标识成0 也就是标识访问过了，模板使用set方法
        dfs(grid, nr, nc, r - 1, c);
        dfs(grid, nr, nc, r + 1, c);
        dfs(grid, nr, nc, r, c + 1);
        dfs(grid, nr, nc, r, c - 1);
    }
}
