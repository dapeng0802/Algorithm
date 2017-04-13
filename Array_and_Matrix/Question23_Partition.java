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