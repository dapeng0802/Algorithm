/**
 * ������������������������Ľڵ�
 * ����Ŀ��
 *   һ�ö�����ԭ�������������������������������ڵ������λ�ã�ʹ����ö�����������
 * ���������������һ�����������ڵ㲢���ء���֪�����������нڵ��ֵ����һ����������
 * ������ͷ�ڵ� head������һ������Ϊ 2 �Ķ������ڵ����͵����� errs��errs[0] ��ʾһ��
 * ����ڵ㣬errs[1] ��ʾ��һ������ڵ㡣
 */
public Node[] getTwoErrNodes(Node head) {
	Node[] errs = new Node[2];
	if (head == null) {
		return errs;
	}
	Stack<Node> stack = new Stack<Node>();
	Node pre = null;
	while (!stack.isEmpty() || head != null) {
		if (head != null) {
			stack.push(head);
			head = head.left;
		} else {
			head = stack.pop();
			if (pre != null && pre.value > head.value) {
				errs[0] = errs[0] == null ? pre : errs[0];
				errs[1] = head;
			}
			pre = head;
			head = head.right;
		}
	}
	return errs;
}
