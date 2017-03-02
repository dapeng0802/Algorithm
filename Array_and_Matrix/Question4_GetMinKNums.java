/**
 * 找到无序数组中最小的 k 个数
 * 【题目】
 *   给定一个无序的整型数组 arr，找到其中最小的 k 个数。
 * 【要求】
 *   如果数组 arr 的长度为 N，排序之后自然可以得到最小的 k 个数，
 * 此时时间复杂度与排序的时间复杂度相同，均为 O(NlogN)。
 * 本题要求实现时间复杂度为 O(Nlogk) 和 O(N) 的方法。
 * 【解法一】
 *   维护一个有 k 个数的大根堆，这个堆代表目前选出的 k 个最小的数，
 * 在堆里的 k 个元素中堆顶的元素是最小的 k 个数里最大的那个。
 */
public int[] getMinKNumsByHeap(int[] arr, int k) {
	if (k < 1 || k > arr.length) {
		return arr;
	}
	int[] kHeap = new int[k];
	for (int i = 0; i != k; i++) {
		heapInsert(kHeap, arr[i], i);
	}
	for (int i = k; i != arr.length; i++) {
		if (arr[i] < kHeap[0]) {
			kHeap[0] = arr[i];
			heapify(kHeap, 0, k);
		}
	}
	return kHeap;
}

public void heapInsert(int[] arr, int value, int index) {
	arr[index] = value;
	while (index != 0) {
		int parent = (index - 1) / 2;
		if (arr[parent] < arr[index]) {
			swap(arr, parent, index);
			index = parent;
		} else {
			break;
		}
	}
}

public void heapify(int[] arr, int index, int heapSize) {
	int left = index * 2 + 1;
	int right = index * 2 + 2;
	int largest = index;
	while (left < heapSize) {
		if (arr[left] > arr[index]) {
			largest = left;
		}
		if (right < heapSize && arr[right] > arr[largest]) {
			largest = right;
		}
		if (largest != index) {
			swap(arr, largest, index);
		} else {
			break;
		}
		index = largest;
		left = index * 2 + 1;
		right = index * 2 + 2;
	}
}

public void swap(int[] arr, int index1, int index2) {
	int tmp = arr[index1];
	arr[index1] = arr[index2];
	arr[index2] = tmp;
}