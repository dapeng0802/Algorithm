/**
 * 在二叉树中找到一个节点的后继节点
 * 【题目】
 *   现在有一种新的二叉树节点类型如下：
 *     public class Node {
 *         public int value;
 *         public Node left;
 *         public Node right;
 *         public Node parent;
 *         
 *         public Node(int data) {
 *             this.value = data;
 *         }
 *     }
 *   该结构比普通二叉树结点结构多了一个指向父节点的 parent 指针。假设有一棵 Node 类型的节点
 * 组成的二叉树，树中每个节点的 parent 指针都指向自己的父节点，头节点的 parent 指向 null。
 * 只给一个在二叉树中的某个节点 node，请实现返回 node 的后继节点的函数。在二叉树的中序遍历
 * 的序列中，node 的下一个节点叫作 node 的后继节点。
 *   例如，下图所示的二叉树。
 *                                    6
 *                                /       \
 *                               3         9
 *                              / \       / \
 *                             1   4     8   10
 *                              \   \   /
 *                               2   5 7
 *   中序遍历的结果为：1，2，3，4，5，6，7，8，9，10
 *   所以节点 1 的后继为节点 2，节点 2 的后继为节点 3，……，节点 10 的后继为 null。
 */
public Node getNextNode(Node node) {
	if (node == null)
		return node;
	if (node.right != null)
		return getLeftMost(node.right);
	else {
		Node parent = node.parent;
		while (parent != null && parent.left != node) {
			node = parent;
			parent = node.parent;
		}
		return parent;
	}
}
public Node getLeftMost(Node node) {
	if (node == null)
		return node;
	while (node.left != null)
		node = node.left;
	return node;
}