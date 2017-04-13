/**
 * 数组的 partition 调整
 * 【题目】
 *   给定一个有序数组 arr，调整 arr 使得这个数组的左半部分没有重复元素且升序，
 * 而不用保证右部分是否有序。
 *   例如，arr=[1,2,2,2,3,3,4,5,6,6,7,7,8,8,8,9]，调整之后 arr=[1,2,3,4,5,6,7,8,9,...]。
 * 【要求】
 *   1. 所有题目实现的时间复杂度为 O(N)。
 *   2. 所有题目实现的额外空间复杂度为 O(1)。
 */
public void partition(int[] arr) {
	if (arr == null || arr.length == 0) {
		return;
	}
	int u = 0;
	int i = 1;
	while (i != arr.length) {
		if (arr[i++] != arr[u]) {
			swap(arr, ++u, i - 1);
		}
	}
}
/**
 * 【补充题目】
 *   给定一个数组 arr，其中只可能含有 0、1、2 三个值，请实现 arr 的排序。
 *   另一种问法为：有一个数组，其中只有红球、蓝球和黄球，请实现红球全放在数组的
 * 左边，蓝球放在中间，黄球放在右边。
 *   另一种问法为：有一个数组，给定一个值 k，请实现比 k 小的数都放在数组的左边，
 * 等于 k 的数都放在数组的中间，比 k 大的数都放在数组的右边。
 * 【要求】
 *   1. 所有题目实现的时间复杂度为 O(N)。
 *   2. 所有题目实现的额外空间复杂度为 O(1)。
 */
public void sort(int[] arr) {
	if (arr == null || arr.length == 0) {
		return;
	}
	int left = -1;
	int index = 0;
	int right = arr.length;
	while (index < right) {
		if (arr[index] == 0) {
			swap(arr, ++left, index++);
		} else if (arr[index] == 1) {
			index++;
		} else {
			swap(arr, --right, index);
		}
	}
}