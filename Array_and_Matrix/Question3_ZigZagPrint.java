/**
 * ��֮�����δ�ӡ����
 * ����Ŀ��
 *   ����һ������ matrix�����ա�֮�����εķ�ʽ��ӡ����������磺
 *   1  2  3  4
 *   5  6  7  8
 *   9  10 11 12
 *   ��֮�����δ�ӡ�Ľ��Ϊ��1��2��5��9��6��3��4��7��10��11��8��12
 * ��Ҫ��
 *   ����ռ临�Ӷ�Ϊ O(1)��
 */
public void zigzagPrint(int[][] matrix) {
	int tR = 0;
	int tC = 0;
	int dR = 0;
	int dC = 0;
	int endR = matrix.length - 1;
	int endC = matrix[0].length - 1;
	boolean fromUp = false;
	while (tR != endR + 1) {
		printLevel(matrix, tR, tC, dR, dC, fromUp);
		tR = tC == endC ? tR + 1 : tR;
		tC = tC == endC ? tC : tC + 1;
		dC = dR == endR ? dC + 1 : dC;
		dR = dR == endR ? dR : dR + 1;
		fromUp = !fromUp;
	}
	System.out.println();
}

public void printLevel(int[][] m, int tR, int tC, int dR, int dC, boolean f) {
	if (f) {
		while (tR != dR + 1) {
			System.out.print(m[tR++][tC--] + " ");
		}
	} else {
		while (dR != tR - 1) {
			System.out.print(m[dR--][dC++] + " ");
		}
	}
}