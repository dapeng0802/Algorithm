/**
 * ���������ҵ����ִ������� N/K ����
 * ����Ŀ��
 *   ����һ���������� arr����ӡ���г��ִ�������һ����������û��������������ӡ��ʾ��Ϣ��
 * ��Ҫ��
 *   Ҫ��ʱ�临�Ӷ�Ϊ O(N)������ռ临�Ӷ�Ϊ O(1)��
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