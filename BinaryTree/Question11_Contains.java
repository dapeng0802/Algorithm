/**
 * 判断 t1 树是否包含 t2 树全部的拓扑结构
 * 【题目】
 *   给定彼此独立的两棵树头节点分别为 t1 和 t2，判断 t1 树是否包含 t2 树全部的拓扑结构。
 *   例如，下图所示的 t1 树和 t2 树。
 *   
 *                          1
 *                        /   \
 *                       2     3                     2
 *                     /  \   / \                   / \
 *                    4    5 6   7                 4   5
 *                   / \  /                       /
 *                  8  9 10                      8
 *                  
 *   t1 树包含 t2 树全部的拓扑结构，所以返回 true。
 */
public boolean contains(Node t1, Node t2) {
	return check(t1, t2) || contains(t1.left, t2) || contains(t1.right, t2);
}

public boolean check(Node h, Node t2) {
	if (t2 == null) {
		return true;
	}
	if (h == null || h.value != t2.value) {
		return false;
	}
	return check(h.left, t2.left) && check(h.right, t2.right);
}