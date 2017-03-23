/**
 * ��Ȼ�����������
 * ����Ŀ��
 *   ����һ������Ϊ N ���������� arr�������� N ��������ȵ���Ȼ�� 1~N����ʵ�� arr
 * �����򣬵��ǲ�Ҫ���±� 0~N-1 λ���ϵ���ͨ��ֱ�Ӹ�ֵ�ķ�ʽ�滻�� 1~N��
 * ��Ҫ��
 *   ʱ�临�Ӷ�Ϊ O(N)������ռ临�Ӷ�Ϊ O(1)��
 */
public void sort(int[] arr) {
	int temp = 0;
	for (int i = 0; i < arr.length;) {
		if (arr[i]-1 == i) {
			i++;
			continue;
		}
		temp = arr[arr[i]-1];
		arr[arr[i]-1] = arr[i];
		arr[i] = temp;
	}
}

public void sort2(int[] arr) {
	int temp = 0;
	int next = 0;
	for (int i = 0; i < arr.length; i++) {
		temp = arr[i];
		while (arr[i] != i + 1) {
			next = arr[temp - 1];
			arr[temp - 1] = temp;
			temp = next;
		}
	}
}