/**
 * 打印 N 个数组整体最大的 Top K
 * 【题目】
 *   有 N 个长度不一的数组，所有的数组都是有序的，请从大到小打印这 N 个数组整体最大的前 K 个数。
 *   例如，输入含有 N 行元素的二维数组可以代表 N 个一维数组。
 *   219,405,538,845,971
 *   148,558
 *   52,99,348,691
 *   再输入整数 k=5，则打印：
 *   Top 5: 971,845,691,558,538
 * 【要求】
 *   1. 如果所有数组的元素个数小于 K，则从大到小打印所有的数。
 *   2. 要求时间复杂度为 O(KlogN)。
 */
public void printTopK(int[][] matrix, int topK) {
	int heapSize = matrix.length;
	HeapNode[] heap = new HeapNode[heapSize];
	for (int i = 0; i != heapSize; i++) {
		int index = matrix[i].length - 1;
		heap[i] = new HeapNode(matrix[i][index], i, index);
		heapInsert(heap, i);
	}
	System.out.print("Top " + topK + " : ");
	for (int i = 0; i != topK; i++) {
		if (heapSize == 0) {
			break;
		}
		System.out.print(heap[0].value + " ");
		if (heap[0].index != 0) {
			heap[0].value = matrix[heap[0].arrNum][--heap[0].index];
		} else {
			swap(heap, 0, --heapSize);
		}
		heapify(heap, 0, heapSize);
	}
	
}

public void heapInsert(HeapNode[] heap, int index) {
	while (index != 0) {
		int parent = (index - 1) / 2;
		if (heap[parent].value < heap[index].value) {
			swap(heap, parent, index);
			index = parent;
		} else {
			break;
		}
	}
}

public void heapify(HeapNode[] heap, int index, int heapSize) {
	int left = index * 2 + 1;
	int right = index * 2 + 2;
	int largest = index;
	while (left < heapSize) {
		if (heap[left].value > heap[index].value) {
			largest = left;
		}
		if (right < heapSize && heap[right].value > heap[largest].value) {
			largest = right;
		}
		if (largest != index) {
			swap(heap, largest, index);
		} else {
			break;
		}
		index = largest;
		left = index * 2 + 1;
		right = index * 2 + 2;
	}
}

public void swap(HeapNode[] heap, int index1, int index2) {
	HeapNode tmp = heap[index1];
	heap[index1] = heap[index2];
	heap[index2] = tmp;
}
class HeapNode {
	public int value;
	public int arrNum;
	public int index;
	
	public HeapNode(int value, int arrNum, int index) {
		this.value = value;
		this.arrNum = arrNum;
		this.index = index;
	}
}