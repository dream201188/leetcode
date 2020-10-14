package java_sub;

import java.util.LinkedList;
import java.util.Queue;

/*
连成一片的也叫岛屿，连成一片就是用图的办法可以访问到，也就是说可以遍历，可以遍历几次就是有几片也即是有几个岛屿；
本方法使用迭代遍历的方法
*/public class Island_bfs_200 {
    public int numIslands(char[][] grid) {
        if (null == grid || 0 == grid.length) // 每次先判断空的情况
            return 0;

        int nr = grid.length;
        int nc = grid[0].length;
        int count = 0;
        Queue<Integer> queue = new LinkedList<>(); // 广度遍历维护一个queue
        for (int i = 0; i < nr; i++) {
            for (int j = 0; j < nc; j++) {
                if ('1' == grid[i][j]) {
                    count++;
                    grid[i][j] = '0';
                    int index = i * nc + j; // 二维数组换算成一维数组的index
                    queue.offer(index);
                    while (!queue.isEmpty()) {
                        int index_tmp = queue.poll();
                        int row = index_tmp / nc; // 再将一维数组换算成行与列的数值
                        int col = index_tmp % nc;
                        if (row - 1 >= 0 && grid[row - 1][col] == '1') { // 上面的一个
                            grid[row - 1][col] = '0';
                            queue.offer((row - 1) * nc + col);
                        }
                        if (row + 1 < nr && grid[row + 1][col] == '1') { // 下面的一个
                            grid[row + 1][col] = '0';
                            queue.offer((row + 1) * nc + col);
                        }
                        if (col + 1 < nc && grid[row][col + 1] == '1') { // 右面的一个
                            grid[row][col + 1] = '0';
                            queue.offer(row * nc + col + 1);
                        }
                        if (col - 1 >= 0 && grid[row][col - 1] == '1') { // 左面的一个
                            grid[row][col - 1] = '0';
                            queue.offer(row * nc + col - 1);
                        }
                    }
                }
            }
        }
        return count;
    }
}
