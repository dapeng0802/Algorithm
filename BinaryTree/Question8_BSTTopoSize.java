/**
 * 找到二叉树中符合搜索二叉树条件的最大拓扑结构
 * 【题目】
 *   给定一棵二叉树的头节点 head，已知所有节点的值都不一样，返回其中最大的且符合
 * 搜索二叉树条件的最大拓扑结构的大小。
 *   例如，二叉树如下图所示。
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
 *   其中最大的且符合搜索二叉树条件的最大拓扑结构如下图所示。
 *                               6
 *                              / \
 *                             /   \
 *                            1    12
 *                           / \  /  \
 *                          0  3 10  13
 *                                     \
 *                                     16
 *                     
 *   这个拓扑结构节点数为 8，所以返回 8。
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