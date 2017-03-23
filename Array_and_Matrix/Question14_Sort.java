/**
 * 自然数数组的排序
 * 【题目】
 *   给定一个长度为 N 的整型数组 arr，其中有 N 个互不相等的自然数 1~N，请实现 arr
 * 的排序，但是不要把下标 0~N-1 位置上的数通过直接赋值的方式替换成 1~N。
 * 【要求】
 *   时间复杂度为 O(N)，额外空间复杂度为 O(1)。
 */
public void sort(int[] arr) {
	int temp = 0;
	for (int i = 0; i < arr.length;) {
		if (arr[i]-1 == i) {
			i++;
			continue;
		}
		temp = arr[arr[i]-1];
		arr[arr[i]-1] = arr[i];
		arr[i] = temp;
	}
}

public void sort2(int[] arr) {
	int temp = 0;
	int next = 0;
	for (int i = 0; i < arr.length; i++) {
		temp = arr[i];
		while (arr[i] != i + 1) {
			next = arr[temp - 1];
			arr[temp - 1] = temp;
			temp = next;
		}
	}
}