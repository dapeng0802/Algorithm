/**
 * 在数组中找到出现次数大于 N/K 的数
 * 【题目】
 *   给定一个整型数组 arr，打印其中出现次数大于一半的数，如果没有这样的数，打印提示信息。
 * 【要求】
 *   要求时间复杂度为 O(N)，额外空间复杂度为 O(1)。
 */
public void printHalfMajor(int[] arr) {
	int cand = 0;
	int times = 0;
	for (int i = 0; i != arr.length; i++) {
		if (times == 0) {
			cand = arr[i];
			times = 1;
		} else if (arr[i] == cand) {
			times++;
		} else {
			times--;
		}
	}
	times = 0;
	for (int i = 0; i != arr.length; i++) {
		if (arr[i] == cand) {
			times++;
		}
	}
	if (times > arr.length / 2) {
		System.out.println(cand);
	} else {
		System.out.println("no such number.");
	}
}