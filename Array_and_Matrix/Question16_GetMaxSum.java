/**
 * 子数组的最大累加和问题
 * 【题目】
 *   给定一个数组 arr，返回子数组的最大累加和。
 *   例如，arr=[1,-2,3,5,-2,6,-1]，所有的子数组中，[3,5,-2,6] 可以累加出最大的和 12，所以返回 12。
 * 【要求】
 *   如果 arr 长度为 N，要求时间复杂度为 O(N)，额外空间复杂度为 O(1)。
 */
public int getMaxSum(int[] arr) {
	if (arr == null || arr.length == 0)
		return 0;
	int maxSum = Integer.MIN_VALUE;
	int curSum = 0;
	for (int i = 0; i < arr.length; i++) {
		curSum += arr[i];
		maxSum = Math.max(maxSum, curSum);
		if (curSum < 0) {
			curSum = 0;
		}
	}
	return maxSum;
}