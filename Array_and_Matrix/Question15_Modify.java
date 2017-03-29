/**
 * �����±궼����������ż���±궼��ż��
 * ����Ŀ��
 *   ����һ�����Ȳ�С�� 2 ������ arr��ʵ��һ���������� arr��Ҫô�����е�ż���±궼��ż����
 * Ҫô�����е������±궼��������
 * ��Ҫ��
 *   ��� arr �ĳ���Ϊ N������Ҫ��ʱ�临�Ӷ�Ϊ O(N)������ռ临�Ӷ�Ϊ O(1)��
 */
public void modify(int[] arr) {
	if (arr == null || arr.length < 2) {
		return;
	}
	int even = 0;
	int odd = 1;
	int end = arr.length - 1;
	while (even <= end && odd <= end) {
		if ((arr[end] & 1) == 0) {
			swap(arr, end, even);
			even += 2;
		} else {
			swap(arr, end, odd);
			odd += 2;
		}
	}
}