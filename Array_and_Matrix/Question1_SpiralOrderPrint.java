/**
 * 转圈打印矩阵
 * 【题目】
 *   给定一个整型矩阵 matrix，请按照转圈的方式打印它。
 *   例如：
 *   1  2  3  4
 *   5  6  7  8
 *   9  10 11 12
 *   13 14 15 16
 *   打印结果为：1，2，3，4，8，12，16，15，14，13，9，5，6，7，11，10
 * 【要求】
 *   额外空间复杂度为 O(1)。
 */
public void spiralOrderPrint(int[][] matrix) {
	int tR = 0;
	int tC = 0;
	int dR = matrix.length - 1;
	int dC = matrix[0].length - 1;
	while (tR <= dR && tC <= dC) {
		printEdge(matrix, tR++, tC++, dR--, dC--);
	}
}

public void printEdge(int[][] m, int tR, int tC, int dR, int dC) {
	if (tR == dR) {
		for (int i = tC; i <= dC; i++) {
			System.out.print(m[tR][i] + " ");
		}
	} else if (tC == dC) {
		for (int i = tR; i <= dR; i++) {
			System.out.print(m[i][tC] + " ");
		}
	} else {
		int curC = tC;
		int curR = tR;
		while (curC != dC) {
			System.out.print(m[tR][curC] + " ");
			curC++;
		}
		while (curR != dR) {
			System.out.print(m[curR][dC] + " ");
			curR++;
		}
		while (curC != tC) {
			System.out.print(m[dR][curC] + " ");
			curC--;
		}
		while (curR != tR) {
			System.out.print(m[curR][tC] + " ");
			curR--;
		}
	}
}