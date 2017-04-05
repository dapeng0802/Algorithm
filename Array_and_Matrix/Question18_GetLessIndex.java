/**
 * ���������ҵ�һ���ֲ���С��λ��
 * ����Ŀ��
 *   ����ֲ���С�ĸ��arr ����Ϊ 1 ʱ��arr[0] �Ǿֲ���С��arr ����Ϊ N(N>1) ʱ,
 * ��� arr[0]<arr[1]����ô arr[0] �Ǿֲ���С����� arr[N-1]<arr[N-2]����ô arr[N-1]
 * �Ǿֲ���С����� 0<i<N-1������ arr[i]<arr[i-1]������ arr[i]<arr[i+1]����ô arr[i]
 * �Ǿֲ���С��
 *   ������������ arr����֪ arr �������������ڵ���������ȡ�дһ��������ֻ�践�� arr ��
 * ����һ���ֲ���С���ֵ�λ�ü��ɡ�
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