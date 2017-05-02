/**
 * 调整搜索二叉树中两个错误的节点
 * 【题目】
 *   一棵二叉树原本是搜索二叉树，但是其中有两个节点调换了位置，使得这棵二叉树不再是
 * 搜索二叉树，请找回这两个错误节点并返回。已知二叉树中所有节点的值都不一样，给定二
 * 叉树的头节点 head，返回一个长度为 2 的二叉树节点类型的数组 errs，errs[0] 表示一个
 * 错误节点，errs[1] 表示另一个错误节点。
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
