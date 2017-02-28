/**
 * 将正方形矩阵顺时针转动 90 度
 * 【题目】
 *   给定一个 N * N 的矩阵 matrix，把这个矩阵调整成顺时针转动 90 度后的形式。
 *   例如：
 *   1  2  3  4
 *   5  6  7  8
 *   9  10 11 12
 *   13 14 15 16
 *   顺时针转动 90 度后为：
 *   13 9  5  1
 *   14 10 6  2
 *   15 11 7  3
 *   16 12 8  4
 * 【要求】
 *   额外空间复杂度为 O(1)。
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