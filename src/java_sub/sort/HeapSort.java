package java_sub.sort;

public class HeapSort {

    public void sort(int[] arr) {

        int n = arr.length;
        for (int i = n / 2 - 1; i > -1; i--) {
            heapify(arr, n, i);
        }

        for (int i = n - 1; i > 0; i--) {
            int swap = arr[0];
            arr[0] = arr[i];
            arr[i] = swap;
            heapify(arr, i, 0);
        }

    }

    public void heapify(int[] arr, int n, int i) {
        int largest = i;
        int l = 2 * i + 1;
        int r = 2 * i + 2;
        if (l < n && arr[largest] < arr[l])
            largest = l;
        if (r < n && arr[largest] < arr[r])
            largest = r;

        if (largest != i) {
            int swap = arr[largest];
            arr[largest] = arr[i];
            arr[i] = swap;
            heapify(arr, n, largest);
        }

    }
}