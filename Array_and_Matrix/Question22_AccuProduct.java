/**
 * 不包含本位置值的累乘数组
 * 【题目】
 *   给定一个整型数组 arr，返回不包含本位置值的累乘数组。
 *   例如，arr=[2,3,1,4]，返回 [12,8,24,6]，即除自己外，其他位置上的累乘。
 * 【要求】
 *   1. 时间复杂度为 O(N)。
 *   2. 除需要返回的结果数组外，额外空间复杂度为 O(1)。
 */
public int[] accuProduct(int[] arr) {
	if (arr == null || arr.length < 2) {
		return null;
	}
	int count = 0;
	int all = 1;
	int[] result = new int[arr.length];
	for (int i = 0; i < arr.length; i++) {
		if (arr[i] != 0) {
			all *= arr[i];
		} else {
			count++;
		}
	}
	if (count == 0) {
		for (int i = 0; i < arr.length; i++) {
			result[i] = all / arr[i];
		}
	}
	if (count == 1) {
		for (int i = 0; i != arr.length; i++) {
			if (arr[i] == 0) {
				result[i] = all;
			}
		}
	}
	return result;
}

/**
 * 【进阶题目】
 *   对时间和空间复杂度的要求不变，而且不可以使用除法。
 */
public int[] accuProduct2(int[] arr) {
	if (arr == null || arr.length < 2) {
		return null;
	}
	int[] result = new int[arr.length];
	result[0] = arr[0];
	for (int i = 1; i < arr.length; i++) {
		result[i] = result[i - 1] * arr[i];
	}
	int tmp = 1;
	for (int i = arr.length - 1; i > 0; i--) {
		result[i] = result[i - 1] * tmp;
		tmp *= arr[i];
	}
	result[0] = tmp;
	return result;
}