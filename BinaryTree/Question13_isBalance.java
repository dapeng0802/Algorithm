/**
 * 判断二叉树是否为平衡二叉树
 * 【题目】
 *   平衡二叉树的性质为：要么是一棵空树，要么任何一个节点的左右子树高度差的绝对值不超过 1。
 * 给定一棵二叉树的头节点 head，判断这棵二叉树是否为平衡二叉树。
 * 【要求】
 *   如果二叉树的节点数为 N，要求时间复杂度为 o(N)。
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