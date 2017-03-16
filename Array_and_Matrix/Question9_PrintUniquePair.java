/**
 * 不重复打印排序数组中相加和为给定值的所有二元组和三元组
 * 【题目】
 *   给定排序数组 arr 和整数 k，不重复打印 arr 中所有相加和为 k 的不降序二元组。
 *   例如，arr=[-8,-4,-3,0,1,2,4,5,8,9]，k=10，打印结果为：
 *   1,9
 *   2,8
 */
public void printUniquePair(int[] arr, int k) {
	if (arr == null || arr.length < 2) {
		return;
	}
	int left = 0;
	int right = arr.length - 1;
	while (left < right) {
		if (arr[left] + arr[right] < k) {
			left++;
		} else if (arr[left] + arr[right] > k) {
			right--;
		} else {
			if (left == 0 || arr[left - 1] != arr[left]) {
				System.out.println(arr[left] + "," + arr[right]);
			}
			left++;
			right--;
		}
	}
}