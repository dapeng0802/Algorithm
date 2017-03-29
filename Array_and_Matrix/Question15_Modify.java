/**
 * 奇数下标都是奇数或者偶数下标都是偶数
 * 【题目】
 *   给定一个长度不小于 2 的数组 arr，实现一个函数调整 arr，要么让所有的偶数下标都是偶数，
 * 要么让所有的奇数下标都是奇数。
 * 【要求】
 *   如果 arr 的长度为 N，函数要求时间复杂度为 O(N)，额外空间复杂度为 O(1)。
 */
public void modify(int[] arr) {
	if (arr == null || arr.length < 2) {
		return;
	}
	int even = 0;
	int odd = 1;
	int end = arr.length - 1;
	while (even <= end && odd <= end) {
		if ((arr[end] & 1) == 0) {
			swap(arr, end, even);
			even += 2;
		} else {
			swap(arr, end, odd);
			odd += 2;
		}
	}
}