/**
 * �ж�һ�ö������Ƿ�Ϊ��������������ȫ������
 * ����Ŀ��
 *   ����һ����������ͷ�ڵ� head����֪����û���ظ�ֵ�Ľڵ㣬ʵ�����������ֱ��ж���ö�������
 * ��������������ȫ��������
 */
public boolean isBST(Node head) {
	if (head == null)
		return true;
	boolean res = true;
	Node pre = null;
	Node cur1 = head;
	Node cur2 = null;
	while (cur1 != null) {
		cur2 = cur1.left;
		if (cur2 != null) {
			while (cur2.right != null && cur2.right != cur1) {
				cur2 = cur2.right;
			}
			if (cur2.right == null) {
				cur2.right = cur1;
				cur1 = cur1.left;
				continue;
			} else {
				cur2.right = null;
			}
		}
		if (pre != null && pre.value > cur1.value) {
			res = false;
		}
		pre = cur1;
		cur1 = cur1.right;
	}
	return res;
}