/**
 * �Ӿ��������ۼӺ�����
 * ����Ŀ��
 *   ����һ������ matrix�����е�ֵ�������и����� 0�������Ӿ��������ۼӺ͡�
 *   ���磬���� matrix Ϊ��
 *   -90  48  78
 *    64 -40  64
 *   -81  -7  66
 *   ���У�����ۼӺ͵��Ӿ���Ϊ��
 *    48  78
 *   -40  64
 *    -7  66
 *   ���Է����ۼӺ� 209��
 *   ���磬matrix Ϊ��
 *   -1  -1  -1
 *   -1   2   2
 *   -1  -1  -1
 *   ���У�����ۼӺ͵��Ӿ���Ϊ��
 *   2  2
 *   ���Է����ۼӺ�4��
 */
public int getMaxSumOfMatrix(int[][] matrix) {
	if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
		return 0;
	}
	int maxSum = Integer.MIN_VALUE;
	int cur = 0;
	int[] s = null;
	for (int i = 0; i != matrix.length; i++) {
		s = new int[matrix[0].length];
		for (int j = i; j != matrix.length; j++) {
			cur = 0;
			for (int k = 0; k != s.length; k++) {
				s[k] += matrix[j][k];
				cur += s[k];
				maxSum = Math.max(maxSum, cur);
				cur = cur < 0 ? 0 : cur;
			}
		}
	}
	
	return maxSum;
}