/**
 * �ҵ�������������С�� k ����
 * ����Ŀ��
 *   ����һ��������������� arr���ҵ�������С�� k ������
 * ��Ҫ��
 *   ������� arr �ĳ���Ϊ N������֮����Ȼ���Եõ���С�� k ������
 * ��ʱʱ�临�Ӷ��������ʱ�临�Ӷ���ͬ����Ϊ O(NlogN)��
 * ����Ҫ��ʵ��ʱ�临�Ӷ�Ϊ O(Nlogk) �� O(N) �ķ�����
 * ���ⷨһ��
 *   ά��һ���� k �����Ĵ���ѣ�����Ѵ���Ŀǰѡ���� k ����С������
 * �ڶ���� k ��Ԫ���жѶ���Ԫ������С�� k �����������Ǹ���
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