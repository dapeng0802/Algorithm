/**
 * �����������ۼӺ�����
 * ����Ŀ��
 *   ����һ������ arr�����������������ۼӺ͡�
 *   ���磬arr=[1,-2,3,5,-2,6,-1]�����е��������У�[3,5,-2,6] �����ۼӳ����ĺ� 12�����Է��� 12��
 * ��Ҫ��
 *   ��� arr ����Ϊ N��Ҫ��ʱ�临�Ӷ�Ϊ O(N)������ռ临�Ӷ�Ϊ O(1)��
 */
public int getMaxSum(int[] arr) {
	if (arr == null || arr.length == 0)
		return 0;
	int maxSum = Integer.MIN_VALUE;
	int curSum = 0;
	for (int i = 0; i < arr.length; i++) {
		curSum += arr[i];
		maxSum = Math.max(maxSum, curSum);
		if (curSum < 0) {
			curSum = 0;
		}
	}
	return maxSum;
}