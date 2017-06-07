/**
 * 在二叉树中找到两个节点的最近公共祖先
 * 【题目】
 *   给定一棵二叉树的头节点 head，以及这棵树中的两个节点 o1 和 o2，请返回 o1 和 o2 的最近
 * 公共祖先节点。
 *   例如，下图所示的二叉树。
 *   
 *                      1
 *                    /   \
 *                   2     3
 *                  / \   / \
 *                 4   5 6   7
 *                          /
 *                         8
 *                         
 *   节点 4 和节点 5 的最近公共祖先节点为节点 2，节点 5 和节点 2 的最近公共祖先节点为节点 2，
 * 节点 6 和节点 8 的最近公共祖先节点为节点 3，节点 5 和节点 8 的最近公共祖先节点为节点 1。
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