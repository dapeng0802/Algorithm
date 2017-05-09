/**
 * 判断 t1 树中是否有与 t2 树拓扑结构完全相同的子树
 * 【题目】
 *   给定彼此独立的两棵树头节点分别为 t1 和 t2，判断 t1 中是否有与 t2 树拓扑结构完全相同的子树。
 *   例如：下图所示的 t1 树和 t2 树。
 *   
 *                         1
 *                      /    \
 *                     2      3                   2
 *                   /   \   / \                /   \
 *                  4     5 6   7              4     5
 *                   \   /                      \   /
 *                    8 9                        8 9 
 *   
 *   t1 树有与 t2 树拓扑结构完全相同的子树，所以返回 true。但如果 t1 树和 t2 树分别如下图所示，
 * 则 t1 树就没有与 t2 树拓扑结构完全相同的子树，所以返回 false。
 *
 *                         1
 *                      /    \
 *                     2      3                   2
 *                   /   \   / \                /   \
 *                  4     5 6   7              4     5
 *                   \   /                      \   
 *                    8 9                        8  
 */
public boolean isSubTree(Node t1, Node t2) {
	String t1Str = serialByPre(t1);
	String t2Str = serialByPre(t2);
	return getIndexOf(t1Str, t2Str) != -1;
}

public String serialByPre(Node head) {
	if (head == null) {
		return "#!";
	}
	String res = head.value + "!";
	res += serialByPre(head.left);
	res += serialByPre(head.right);
	return res;
}

// KMP
public int getIndexOf(String s, String m) {
	if (s == null || m == null || m.length() < 1 || s.length() < m.length()) {
		return -1;
	}
	char[] ss = s.toCharArray();
	char[] ms = m.toCharArray();
	int si = 0;
	int mi = 0;
	int[] next = getNextArray(ms);
	while (si < ss.length && mi < ms.length) {
		if (ss[si] == ms[mi]) {
			si++;
			mi++;
		} else if (next[mi] == -1) {
			si++;
		} else {
			mi = next[mi];
		}
	}
	return mi == ms.length ? si - mi : -1;
}

public int[] getNextArray(char[] ms) {
	if (ms.length == 1) {
		return new int[] { -1 };
	}
	int[] next = new int[ms.length];
	next[0] = -1;
	next[1] = 0;
	int pos = 2;
	int cn = 0;
	while (pos < next.length) {
		if (ms[pos - 1] == ms[cn]) {
			next[pos++] = ++cn;
		} else if (cn > 0) {
			cn = next[cn];
		} else {
			next[pos++] = 0;
		}
	}
	return next;
}