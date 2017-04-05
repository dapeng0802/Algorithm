/**
 * 在数组中找到一个局部最小的位置
 * 【题目】
 *   定义局部最小的概念。arr 长度为 1 时，arr[0] 是局部最小。arr 长度为 N(N>1) 时,
 * 如果 arr[0]<arr[1]，那么 arr[0] 是局部最小；如果 arr[N-1]<arr[N-2]，那么 arr[N-1]
 * 是局部最小；如果 0<i<N-1，既有 arr[i]<arr[i-1]，又有 arr[i]<arr[i+1]，那么 arr[i]
 * 是局部最小。
 *   给定无序数组 arr，已知 arr 中任意两个相邻的数都不相等。写一个函数，只需返回 arr 中
 * 任意一个局部最小出现的位置即可。
 */
public int getLessIndex(int[] arr) {
	if (arr == null || arr.length == 0) {
		return -1;
	}
	if (arr.length == 1 || arr[0] < arr[1]) {
		return 0;
	}
	if (arr[arr.length - 1] < arr[arr.length - 2]) {
		return arr.length - 1;
	}
	int left = 1;
	int right = arr.length - 2;
	int mid = 0;
	while (left < right) {
		mid = (left + right) / 2;
		if (arr[mid] > arr[mid - 1]) {
			right = mid - 1;
		} else if (arr[mid] > arr[mid + 1]) {
			left = mid + 1;
		} else {
			return mid;
		}
	}
	return left;
}