/**
 * 数组中未出现的最小正整数
 * 【题目】
 *   给定一个无序整型数组 arr，找到数组中未出现的最小正整数。
 *   例如：
 *   arr=[-1,2,3,4]。返回 1。
 *   arr=[1,2,3,4]。返回 5。
 */
public int missNum(int[] arr) {
	int l = 0;
	int r = arr.length;
	while (l < r) {
		if (arr[l] == l + 1) {
			l++;
		} else if (arr[l] <= 1 || arr[l] > r || arr[arr[l] - 1] == arr[l]) {
			arr[l] = arr[--r];
		} else {
			swap(arr, l, arr[l] - 1);
		}
	}
	return l + 1;
}