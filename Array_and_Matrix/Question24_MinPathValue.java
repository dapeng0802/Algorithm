/**
 * �����ͨ·ֵ
 * ����Ŀ��
 *   ��һ�����;��� matrix ��ʾһ�����磬1 ������·��0 ������·��ÿһ��λ��ֻҪ��Խ�磬������������ 4 ������
 * ��������Ͻǵ������½ǵ����ͨ·ֵ��
 *   ���磬matrix Ϊ��
 *   1 0 1 1 1
 *   1 0 1 0 1
 *   1 1 1 0 1
 *   0 0 0 0 1
 *   ͨ·ֻ��һ������ 12 �� 1 ���ɣ����Է��� 12��
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