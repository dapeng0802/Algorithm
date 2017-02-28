/**
 * �������ξ���˳ʱ��ת�� 90 ��
 * ����Ŀ��
 *   ����һ�� N * N �ľ��� matrix����������������˳ʱ��ת�� 90 �Ⱥ����ʽ��
 *   ���磺
 *   1  2  3  4
 *   5  6  7  8
 *   9  10 11 12
 *   13 14 15 16
 *   ˳ʱ��ת�� 90 �Ⱥ�Ϊ��
 *   13 9  5  1
 *   14 10 6  2
 *   15 11 7  3
 *   16 12 8  4
 * ��Ҫ��
 *   ����ռ临�Ӷ�Ϊ O(1)��
 */
public void rotate(int[][] matrix) {
	int tR = 0;
	int tC = 0;
	int dR = matrix.length - 1;
	int dC = matrix[0].length - 1;
	while (tR < dR) {
		rotateEdge(matrix, tR++, tC++, dR--, dC--);
	}
}

public void rotateEdge(int[][] m, int tR, int tC, int dR, int dC) {
	int tmp = 0;
	for (int i = tC; i < dC; i++) {
		tmp = m[tR][i];
		m[tR][i] = m[dR-i+tR][tC];
		m[dR-i+tR][tC] = m[dR][dC-i+tC];
		m[dR][dC-i+tC] = m[i][dC];
		m[i][dC] = tmp;
	}
}