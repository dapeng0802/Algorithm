/**
 * ������δ���ֵ���С������
 * ����Ŀ��
 *   ����һ�������������� arr���ҵ�������δ���ֵ���С��������
 *   ���磺
 *   arr=[-1,2,3,4]������ 1��
 *   arr=[1,2,3,4]������ 5��
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