/**
 * 求最短通路值
 * 【题目】
 *   用一个整型矩阵 matrix 表示一个网络，1 代表有路，0 代表无路，每一个位置只要不越界，都有上下左右 4 个方向，
 * 求从最左上角到最右下角的最短通路值。
 *   例如，matrix 为：
 *   1 0 1 1 1
 *   1 0 1 0 1
 *   1 1 1 0 1
 *   0 0 0 0 1
 *   通路只有一条，由 12 个 1 构成，所以返回 12。
 */
public int minPathValue(int[][] matrix) {
	if (matrix == null || matrix.length == 0 || matrix[0].length == 0 || matrix[0][0] != 1 
			|| matrix[matrix.length - 1][matrix[0].length - 1] != 1) {
		return 0;
	}
	int res = 0;
	int[][] map = new int[matrix.length][matrix[0].length];
	map[0][0] = 1;
	Queue<Integer> rQ = new LinkedList<Integer>();
	Queue<Integer> cQ = new LinkedList<Integer>();
	rQ.add(0);
	cQ.add(0);
	int r = 0;
	int c = 0;
	while (!rQ.isEmpty()) {
		r = rQ.poll();
		c = cQ.poll();
		if (r == matrix.length - 1 && c == matrix[0].length - 1) {
			return map[r][c];
		}
		walkTo(map[r][c], r - 1, c, matrix, map, rQ, cQ);
		walkTo(map[r][c], r + 1, c, matrix, map, rQ, cQ);
		walkTo(map[r][c], r, c - 1, matrix, map, rQ, cQ);
		walkTo(map[r][c], r, c + 1, matrix, map, rQ, cQ);
	}
	return res;
}
public void walkTo(int pre, int toR, int toC, int[][] m, int[][] map, Queue<Integer> rQ, Queue<Integer> cQ) {
	if (toR < 0 || toR == m.length || toC < 0 || toC == m[0].length 
			|| m[toR][toC] != 1 || map[toR][toC] != 0) {
		return;
	}
	map[toR][toC] = pre + 1;
	rQ.add(toR);
	cQ.add(toC);
}