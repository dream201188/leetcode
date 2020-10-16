package java_sub;

import java.util.Collections;
import java.util.PriorityQueue;

class MedianSlidingWindow2 {
    PriorityQueue<Integer> maxHeap = new PriorityQueue<>((Collections.reverseOrder())); // 大顶堆，小半部分
    PriorityQueue<Integer> minHeap = new PriorityQueue<>(); // 小顶堆，大半部分数字

    public double[] medianSlidingWindow(int[] nums, int k) {
        double[] result = new double[nums.length - k + 1];
        for (int i = 0; i < nums.length; i++) {
            if (maxHeap.size() == 0 || maxHeap.peek() >= nums[i]) {
                maxHeap.add(nums[i]);
            } else {
                minHeap.add(nums[i]);
            }
            balanceHeaps();

            if (i >= k - 1) { // i 从k - 1 开始变成一个完整滑动窗口
                if (maxHeap.size() == minHeap.size()) { // 偶数大顶堆最大值与小顶堆的平均值
                    result[i - k + 1] = maxHeap.peek() / 2.0 + minHeap.peek() / 2.0; // 少用一个index变量
                } else {
                    result[i - k + 1] = maxHeap.peek();
                }

                int elementToBeRemoved = nums[i - k + 1]; // 少用一个最左端变量表示左边窗口失去的值，
                                                          // i = k -1 开始，nums从0开始
                if (elementToBeRemoved <= maxHeap.peek()) {
                    maxHeap.remove(elementToBeRemoved);
                } else {
                    minHeap.remove(elementToBeRemoved);
                }
                balanceHeaps();
            }
        }
        return result;
    }

    // 每次增加或者后面减少后要进行balance，其实就是红黑树的算法；
    // 平衡的目的是让大顶推的个数要么跟小顶堆一样多要么就是多一个
    // 如果一共有奇数个，那么大顶堆多一个，要么是偶数个，则两边一样多
    private void balanceHeaps() {
        if (maxHeap.size() > minHeap.size() + 1) // 最多多一个
            minHeap.add(maxHeap.poll());
        else if (maxHeap.size() < minHeap.size()) // 最少不能要与他个数相当
            maxHeap.add(minHeap.poll());
    }
}