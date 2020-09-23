package java_sub;

import java.util.ArrayDeque;
import java.util.Deque;

public class SlideWindow {
    public SlideWindow() {

    }

    public int[] maxSlidingWindow(int[] nums, int k) {
        if (null == nums || nums.length == 0)
            return new int[0];
        int n = nums.length;
        int[] result = new int[n - k + 1];
        for (int i = 0; i < n - k + 1; i++) {
            int max = nums[i];
            for (int j = i; j < i + k; j++) {
                max = Math.max(max, nums[j]);
            }
            result[i] = max;
        }
        return result;
    }

    public int[] maxSlidingWindow_deque(int[] nums, int k) {
        if (null == nums || k < 1)
            return new int[0];
        int n = nums.length;
        int[] result = new int[n - k + 1];
        int index22 = 0;
        Deque<Integer> queue = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            if (!queue.isEmpty() && queue.peekFirst() <= i - k) {
                queue.pollFirst();
            }
            while (!queue.isEmpty() && nums[queue.peekLast()] < nums[i]) {
                queue.pollLast();
            }
            queue.addLast(i);
            if (i >= k - 1) {
                result[index22++] = nums[queue.peekFirst()];
            }
        }
        return result;
    }
}
