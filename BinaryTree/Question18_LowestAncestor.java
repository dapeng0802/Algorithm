/**
 * �ڶ��������ҵ������ڵ�������������
 * ����Ŀ��
 *   ����һ�ö�������ͷ�ڵ� head���Լ�������е������ڵ� o1 �� o2���뷵�� o1 �� o2 �����
 * �������Ƚڵ㡣
 *   ���磬��ͼ��ʾ�Ķ�������
 *   
 *                      1
 *                    /   \
 *                   2     3
 *                  / \   / \
 *                 4   5 6   7
 *                          /
 *                         8
 *                         
 *   �ڵ� 4 �ͽڵ� 5 ������������Ƚڵ�Ϊ�ڵ� 2���ڵ� 5 �ͽڵ� 2 ������������Ƚڵ�Ϊ�ڵ� 2��
 * �ڵ� 6 �ͽڵ� 8 ������������Ƚڵ�Ϊ�ڵ� 3���ڵ� 5 �ͽڵ� 8 ������������Ƚڵ�Ϊ�ڵ� 1��
 */
public Node lowestAncestor(Node head, Node o1, Node o2) {
	if (head == null || head == o1 || head == o2)
		return head;
	Node left = lowestAncestor(head.left, o1, o2);
	Node right = lowestAncestor(head.right, o1, o2);
	if (left != null && right != null)
		return head;
	return left != null ? left : right;
}