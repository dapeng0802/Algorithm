/**
 * �ж϶������Ƿ�Ϊƽ�������
 * ����Ŀ��
 *   ƽ�������������Ϊ��Ҫô��һ�ÿ�����Ҫô�κ�һ���ڵ�����������߶Ȳ�ľ���ֵ������ 1��
 * ����һ�ö�������ͷ�ڵ� head���ж���ö������Ƿ�Ϊƽ���������
 * ��Ҫ��
 *   ����������Ľڵ���Ϊ N��Ҫ��ʱ�临�Ӷ�Ϊ o(N)��
 */
public boolean isBalance(Node head) {
	boolean[] res = new boolean[1];
	res[0] = true;
	getHeight(head, 1, res);
	return res[0];
}

public int getHeight(Node head, int level, boolean[] res) {
	if (head == null)
		return level;
	int lH = getHeight(head.left, level + 1, res);
	if (!res[0])
		return level;
	int rH = getHeight(head.right, level + 1, res);
	if (!res[0])
		return level;
	if (Math.abs(lH - rH) > 1) {
		res[0] = false;
	}
	return Math.max(lH, rH);
}