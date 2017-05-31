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

public boolean isCBT(Node head) {
	if (head == null) {
		return true;
	}
	Queue<Node> queue = new LinkedList<Node>();
	boolean leaf = false;
	Node l = null;
	Node r = null;
	queue.offer(head);
	while (!queue.isEmpty()) {
		head = queue.poll();
		l = head.left;
		r = head.right;
		if ((leaf && (l != null || r != null)) || (l == null && r != null)) {
			return false;
		}
		if (l != null) {
			queue.offer(l);
		}
		if (r != null) {
			queue.offer(r);
		} else {
			leaf = true;
		}
	}
	return true;
}