package java_sub.sort;

import java_sub.utils.Utils;;

public class QuickSort {
    public void sort(int[] arr, int low, int high) {
        if (low < high) {
            int pi = dualeSortPartition(arr, low, high);
            sort(arr, low, pi - 1);
            sort(arr, pi + 1, high);
        }
    }

    // 双路快排
    public int dualeSortPartition(int[] arr, int low, int high) {

        int i = low, j = high + 1, pivot = arr[low];
        while (i < j) {
            while (--j > i && arr[j] >= pivot)
                ;
            while (++i < j && arr[i] <= pivot)
                ;
            if (i < j) {
                Utils.swap(arr, i, j);
            }
        }
        Utils.swap(arr, low, j);
        return j;

    }

    // 单路快排
    public int singleSortPartition(int[] arr, int low, int high) {

        int i = low - 1, pivot = arr[high];
        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                Utils.swap(arr, i, j);
            }
        }
        i++;
        Utils.swap(arr, i, high);
        return i;

    }

}
