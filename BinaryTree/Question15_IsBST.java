/**
 * 判断一棵二叉树是否为搜索二叉树和完全二叉树
 * 【题目】
 *   给定一个二叉树的头节点 head，已知其中没有重复值的节点，实现两个函数分别判断这棵二叉树是
 * 搜索二叉树和完全二叉树。
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