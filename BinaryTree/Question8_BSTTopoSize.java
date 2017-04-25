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
 *   
 * 【方法一】
 *   二叉树的节点数为 N，时间复杂度为 O(N)。
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
class Node {
	public Node left;
	public Node right;
	public int value;
	Node(int data) {
		value = data;
	}
}

/**
 * 【方法二】
 *   二叉树的节点数为 N，时间复杂度最好为 O(N)、最差为 O(N^2)。
 */
public int bstTopoSize2(Node head) {
	Map<Node, Record> map = new HashMap<Node, Record>();
	return posOrder(head, map);
}
public int posOrder(Node h, Map<Node, Record> map) {
	if (h == null)
		return 0;
	int ls = posOrder(h.left, map);
	int rs = posOrder(h.right, map);
	modifyMap(h.left, h.value, map, true);
	modifyMap(h.right, h.value, map, false);
	Record lr = map.get(h.left);
	Record rr = map.get(h.right);
	int lbst = lr == null ? 0 : lr.l + lr.r + 1;
	int rbst = rr == null ? 0 : rr.l + rr.r + 1;
	map.put(h, new Record(lbst, rbst));
	return Math.max(lbst + rbst + 1, Math.max(ls, rs));
}
public int modifyMap(Node n, int v, Map<Node, Record> m, boolean s) {
	if (n == null || (!m.containsKey(n)))
		return 0;
	Record r = m.get(n);
	if ((s && n.value > v) || ((!s) && n.value < v)) {
		m.remove(n);
		return r.l + r.r + 1;
	} else {
		int minus = modifyMap(s ? n.right : n.left, v, m, s);
		if (s) {
			r.r = r.r - minus;
		} else {
			r.l = r.l - minus;
		}
		m.put(n, r);
		return minus;
	}
}
class Record {
	public int l;
	public int r;
	
	public Record(int left, int right) {
		this.l = left;
		this.r = right;
	}
}