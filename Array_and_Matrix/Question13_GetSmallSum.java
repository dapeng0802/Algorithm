/**
 * 计算数组的小和
 * 【题目】
 *   数组小和的定义如下：
 *   例如，数组 s=[1,3,5,2,4,6]，在 s[0] 的左边小于或等于 s[0] 的数的和为 0，
 * 在 s[1] 的左边小于或等于 s[1] 的数的和为 1，在 s[2] 的左边小于或等于 s[2] 
 * 的数的和为 1+3=4， 在 s[3] 的左边小于或等于 s[3] 的数的和为 1，在 s[4] 的
 * 左边小于或等于 s[4] 的数的和为 1+3+2=6，在 s[5] 的左边小于或等于 s[5] 的
 * 数的和为 1+3+5+2+4=15，所以 s 的小和为 0+1+4+1+6+15=27。
 *   给定一个数组 s，实现函数返回 s 的小和。
 */
public int getSmallSum(int[] arr) {
	if (arr == null || arr.length == 0) {
		return 0;
	}
	return func(arr, 0, arr.length - 1);
}

public int func(int[] s, int l, int r) {
	if (l == r) {
		return 0;
	}
	int mid = (l + r) / 2;
	return func(s, l, mid) + func(s, mid + 1, r) + merge(s, l, mid, r);
}

public int merge(int[] s, int left, int mid, int right) {
	int[] h = new int[right - left + 1];
	int hi = 0;
	int i = left;
	int j = mid + 1;
	int smallSum = 0;
	while (i <= mid && j <= right) {
		if (s[i] <= s[j]) {
			smallSum += s[i] * (right - j + 1);
			h[hi++] = s[i++];
		} else {
			h[hi++] = s[j++];
		}
	}
	for (; (j < right + 1) || (i < mid + 1); j++, i++) {
		h[hi++] = i > mid ? s[j] : s[i];
	}
	for (int k = 0; k != h.length; k++) {
		s[left++] = h[k];
	}
	return smallSum;
}