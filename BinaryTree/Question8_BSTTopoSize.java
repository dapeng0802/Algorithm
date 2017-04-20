/**
 * �ҵ��������з�������������������������˽ṹ
 * ����Ŀ��
 *   ����һ�ö�������ͷ�ڵ� head����֪���нڵ��ֵ����һ�����������������ҷ���
 * ����������������������˽ṹ�Ĵ�С��
 *   ���磬����������ͼ��ʾ��
 *                              6
 *                             / \
 *                            /   \
 *                           /     \
 *                          1       12
 *                         / \    /   \
 *                        0   3  10    13
 *                              /  \   / \
 *                             4   14 20  16
 *                            / \  / \
 *                           2  5 11 15
 *                           
 *   ���������ҷ�������������������������˽ṹ����ͼ��ʾ��
 *                               6
 *                              / \
 *                             /   \
 *                            1    12
 *                           / \  /  \
 *                          0  3 10  13
 *                                     \
 *                                     16
 *                     
 *   ������˽ṹ�ڵ���Ϊ 8�����Է��� 8��
 */
public int bstTopoSize1(Node head) {
	if (head == null) {
		return 0;
	}
	int max = maxTopo(head, head);
	max = Math.max(bstTopoSize1(head.left), max);
	max = Math.max(bstTopoSize1(head.right), max);
	return max;
}

public int maxTopo(Node h, Node n) {
	if (h != null && n != null && isBSTNode(h, n, n.value)) {
		return maxTopo(h, n.left) + maxTopo(h, n.right) + 1;
	}
	return 0;
}

public boolean isBSTNode(Node h, Node n, int value) {
	if (h == null) {
		return false;
	}
	if (h == n) {
		return true;
	}
	return isBSTNode(h.value > value ? h.left : h.right, n, value);
}