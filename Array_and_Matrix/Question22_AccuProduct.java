/**
 * ��������λ��ֵ���۳�����
 * ����Ŀ��
 *   ����һ���������� arr�����ز�������λ��ֵ���۳����顣
 *   ���磬arr=[2,3,1,4]������ [12,8,24,6]�������Լ��⣬����λ���ϵ��۳ˡ�
 * ��Ҫ��
 *   1. ʱ�临�Ӷ�Ϊ O(N)��
 *   2. ����Ҫ���صĽ�������⣬����ռ临�Ӷ�Ϊ O(1)��
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