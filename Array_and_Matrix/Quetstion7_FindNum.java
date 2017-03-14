/**
 * �����ж��ź���ľ���������
 * ����Ŀ��
 *   ����һ���� N*M �����;��� matrix ��һ������ K��
 * matrix ��ÿһ�к�ÿһ�ж����ź���ġ�ʵ��һ��������
 * �ж� K �Ƿ��� matrix �С�
 *   ���磺
 *   0  1  2  5
 *   2  3  4  7
 *   4  4  4  8
 *   5  7  7  9
 *   ��� K Ϊ 7������ true����� K Ϊ 6������ false��
 * ��Ҫ��
 *   ʱ�临�Ӷ�Ϊ O(N+M)������ռ临�Ӷ�Ϊ O(1)��
 */
public boolean findNum(int[][] matrix, int K) {
	int row = 0;
	int col = matrix[0].length - 1;
	while (row < matrix.length && col > -1) {
		if (matrix[row][col] == K) {
			return true;
		} else if (matrix[row][col] > K) {
			col--;
		} else {
			row++;
		}
	}
	return false;
}