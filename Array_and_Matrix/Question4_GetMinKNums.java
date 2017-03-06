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

/**
 * 【解法二】
 *   O(N) 的解法。需要用到一个经典的算法——BFPRT 算法。
 */
public int[] getMinKNumsByBFPRT(int[] arr, int k) {
	if (k < 1 || k > arr.length) {
		return arr;
	}
	int minKth = getMinKthByBFPRT(arr, k);
	int[] res = new int[k];
	int index = 0;
	for (int i = 0; i != arr.length; i++) {
		if (arr[i] < minKth) {
			res[index++] = arr[i];
		}
	}
	for (; index != res.length; index++) {
		res[index] = minKth;
	}
	return res;
}

public int getMinKthByBFPRT(int[] arr, int k) {
	int[] copyArr = copyArray(arr);
	return select(copyArr, 0, copyArr.length - 1, k - 1);
}

public int[] copyArray(int[] arr) {
	int[] res = new int[arr.length];
	for (int i = 0; i != res.length; i++) {
		res[i] = arr[i];
	}
	return res;
}

public int select(int[] arr, int begin, int end, int i) {
	if (begin == end) {
		return arr[begin];
	}
	int pivot = medianOfMedians(arr, begin, end);
	int[] pivotRange = partition(arr, begin, end, pivot);
	if (i >= pivotRange[0] && i <= pivotRange[1]) {
		return arr[i];
	} else if (i < pivotRange[0]) {
		return select(arr, begin, pivotRange[0] - 1, i);
	} else {
		return select(arr, pivotRange[1] + 1, end, i);
	}
}

public int medianOfMedians(int[] arr, int begin, int end) {
	int num = end - begin + 1;
	int offset = num % 5 == 0 ? 0 : 1;
	int[] mArr = new int[num / 5 + offset];
	for (int i = 0; i != mArr.length; i++) {
		int beginI = begin + i * 5;
		int endI = beginI + 4;
		mArr[i] = getMedian(arr, beginI, Math.min(end, endI));
	}
	return select(mArr, 0, mArr.length - 1, mArr.length / 2);
}

public int[] partition(int[] arr, int begin, int end, int pivotValue) {
	int small = begin - 1;
	int cur = begin;
	int big = end + 1;
	while (cur != big) {
		if (arr[cur] < pivotValue) {
			swap(arr, ++small, cur++);
		} else if (arr[cur] > pivotValue) {
			swap(arr, cur, --big);
		} else {
			cur++;
		}
	}
	int[] range = new int[2];
	range[0] = small + 1;
	range[1] = big - 1;
	return range;
}

public int getMedian(int[] arr, int begin, int end) {
	insertionSort(arr, begin, end);
	int sum = end + begin;
	int mid = (sum / 2) + (sum % 2);
	return arr[mid];
}

public void insertionSort(int[] arr, int begin, int end) {
	for (int i = begin + 1; i != end + 1; i++) {
		for (int j = i; j != begin; j--) {
			if (arr[j - 1] > arr[j]) {
				swap(arr, j - 1, j);
			} else {
				break;
			}
		}
	}
}