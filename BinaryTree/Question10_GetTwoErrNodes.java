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
/**
 *   进阶：如果在原问题中得到了这两个错误节点，我们当然可以通过交换两个节点的节点值
 * 的方式让整棵二叉树重新成为搜索二叉树。但现在要求你不能这么做，而是在结构上完全交
 * 换两个节点的位置，请实现调整的函数。
 */
public Node[] getTwoErrParents(Node head, Node e1, Node e2) {
	Node[] parents = new Node[2];
	if (head == null)
		return parents;
	Stack<Node> stack = new Stack<Node>();
	while (!stack.isEmpty() || head != null) {
		if (head != null) {
			stack.push(head);
			head = head.left;
		} else {
			head = stack.pop();
			if (head.left == e1 || head.right == e1)
				parents[0] = head;
			if (head.left == e2 || head.right == e2)
				parents[1] = head;
			head = head.right;
		}
	}
	return parents;
}
public Node recoverTree(Node head) {
	Node[] errs = getTwoErrNodes(head);
	Node[] parents = getTwoErrParents(head, errs[0], errs[1]);
	Node e1 = errs[0];
	Node e1P = parents[0];
	Node e1L = e1.left;
	Node e1R = e1.right;
	Node e2 = errs[1];
	Node e2P = parents[1];
	Node e2L = e2.left;
	Node e2R = e2.right;
	if (e1 == head) {
		if (e1 == e2P) {
			e1.left = e2L;
			e1.right = e2R;
			e2.right = e1;
			e2.left = e1L;
		} else if (e2P.left == e2) {
			e2P.left = e1;
			e2.left = e1L;
			e2.right = e1R;
			e1.left = e2L;
			e1.right = e2R;
		} else {
			e2P.right = e1;
			e2.left = e1L;
			e2.right = e1R;
			e1.left = e2L;
			e1.right = e2R;
		}
		head = e2;
	} else if (e2 == head) {
		if (e2 == e1P) {
			e2.left = e1L;
			e2.right = e1R;
			e1.left = e2;
			e1.right = e2R;
		} else if (e1P.left == e1) {
			e1P.left = e2;
			e1.left = e2L;
			e1.right = e2R;
			e2.left = e1L;
			e2.right = e1R;
		} else {
			e1P.right = e2;
			e1.left = e2L;
			e1.right = e2R;
			e2.left = e1L;
			e2.right = e1R;
		}
		head = e1;
	} else {
		if (e1 == e2P) {
			if (e1P.left == e1) {
				e1P.left = e2;
				e1.left = e2L;
				e1.right = e2R;
				e2.left = e1L;
				e2.right = e1;
			} else {
				e1P.right = e2;
				e1.left = e2L;
				e1.right = e2R;
				e2.left = e1L;
				e2.right = e1;
			}
		} else if (e2 == e1P) {
			if (e2P.left == e2) {
				e2P.left = e1;
				e2.left = e1L;
				e2.right = e1R;
				e1.left = e2;
				e1.right = e2R;
			} else {
				e2P.right = e1;
				e2.left = e1L;
				e2.right = e1R;
				e1.left = e2;
				e1.right = e2R;
			}
		} else {
			if (e1P.left == e1) {
				if (e2P.left == e2) {
					e1.left = e2L;
					e1.right = e2R;
					e2.left = e1L;
					e2.right = e1R;
					e1P.left = e2;
					e2P.left = e1;
				} else {
					e1.left = e2L;
					e1.right = e2R;
					e2.left = e1L;
					e2.right = e1R;
					e1P.left = e2;
					e2P.right = e1;
				}
			} else {
				if (e2P.left == e2) {
					e1.left = e2L;
					e1.right = e2R;
					e2.left = e1L;
					e2.right = e1R;
					e1P.right = e2;
					e2P.left = e1;
				} else {
					e1.left = e2L;
					e1.right = e2R;
					e2.left = e1L;
					e2.right = e1R;
					e1P.right = e2;
					e2P.right = e1;
				}
			}
		}
	}
	return head;
}