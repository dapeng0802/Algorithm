/**
 * ��Ҫ�������������鳤��
 * ����Ŀ��
 *   ����һ���������� arr�������Ҫ�������������鳤�ȡ�
 *   ���磺arr = [1, 5, 3, 4, 2, 6, 7] ���� 4����Ϊֻ�� [5, 3, 4, 2] ��Ҫ����
 */
public int getMinLength(int[] arr) {
	if (arr == null || arr.length < 2) {
		return 0;
	}
	int min = arr[arr.length - 1];
	int noMinIndex = -1;
	for (int i = arr.length - 2; i != -1; i--) {
		if (min < arr[i]) {
			noMinIndex = i;
		} else {
			min = Math.min(min, arr[i]);
		}
	}
	if (noMinIndex == -1) {
		return 0;
	}
	int max = arr[0];
	int noMaxIndex = -1;
	for (int i = 1; i != arr.length; i++) {
		if (max > arr[i]) {
			noMaxIndex = i;
		} else {
			max = Math.max(max, arr[i]);
		}
	}
	return noMaxIndex - noMinIndex + 1;
}