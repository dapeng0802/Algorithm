/**
 * 子矩阵的最大累加和问题
 * 【题目】
 *   给定一个矩阵 matrix，其中的值有正、有负、有 0，返回子矩阵的最大累加和。
 *   例如，矩阵 matrix 为：
 *   -90  48  78
 *    64 -40  64
 *   -81  -7  66
 *   其中，最大累加和的子矩阵为：
 *    48  78
 *   -40  64
 *    -7  66
 *   所以返回累加和 209。
 *   例如，matrix 为：
 *   -1  -1  -1
 *   -1   2   2
 *   -1  -1  -1
 *   其中，最大累加和的子矩阵为：
 *   2  2
 *   所以返回累加和4。
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