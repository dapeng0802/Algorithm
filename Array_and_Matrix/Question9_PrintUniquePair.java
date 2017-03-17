/**
 * ���ظ���ӡ������������Ӻ�Ϊ����ֵ�����ж�Ԫ�����Ԫ��
 * ����Ŀ��
 *   ������������ arr ������ k�����ظ���ӡ arr ��������Ӻ�Ϊ k �Ĳ������Ԫ�顣
 *   ���磬arr=[-8,-4,-3,0,1,2,4,5,8,9]��k=10����ӡ���Ϊ��
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

/**
 * ��������Ŀ��
 *   ������������ arr ������ k�����ظ���ӡ arr ��������Ӻ�Ϊ k �Ĳ�������Ԫ�顣
 *   ���磬arr=[-8,-4,-3,0,1,2,4,5,8,9]��k=10����ӡ���Ϊ��
 *   -4,5,9
 *   -3,4,9
 *   -3,5,8
 *   0,1,9
 *   0,2,8
 *   1,4,5
 */
public void printUniqueTriad(int[] arr, int k) {
	if (arr == null || arr.length < 3) {
		return;
	}
	for (int i = 0; i < arr.length - 2; i++) {
		if (i == 0 || arr[i] != arr[i - 1]) {
			printReset(arr, i, i + 1, arr.length - 1, k - arr[i]);
		}
	}
}

public void printReset(int[] arr, int f, int l, int r, int k) {
	while (l < r) {
		if (arr[l] + arr[r] < k) {
			l++;
		} else if (arr[l] + arr[r] > k) {
			r--;
		} else {
			if (l == f + 1 || arr[l - 1] != arr[l]) {
				System.out.println(arr[f] + "," + arr[l] + "," + arr[r]);
			}
			l++;
			r--;
		}
	}
}