/**
 * �ڶ��������ҵ������ڵ�������������
 * ����Ŀ��
 *   ����һ�ö�������ͷ�ڵ� head���Լ�������е������ڵ� o1 �� o2���뷵�� o1 �� o2 �����
 * �������Ƚڵ㡣
 *   ���磬��ͼ��ʾ�Ķ�������
 *   
 *                      1
 *                    /   \
 *                   2     3
 *                  / \   / \
 *                 4   5 6   7
 *                          /
 *                         8
 *                         
 *   �ڵ� 4 �ͽڵ� 5 ������������Ƚڵ�Ϊ�ڵ� 2���ڵ� 5 �ͽڵ� 2 ������������Ƚڵ�Ϊ�ڵ� 2��
 * �ڵ� 6 �ͽڵ� 8 ������������Ƚڵ�Ϊ�ڵ� 3���ڵ� 5 �ͽڵ� 8 ������������Ƚڵ�Ϊ�ڵ� 1��
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

/**
 * ���ף������ѯ�����ڵ������������ȵĲ���ʮ��Ƶ�����뷨�õ�����ѯ�Ĳ�ѯʱ����١�
 */
class Record1 {
	private HashMap<Node, Node> map;
	
	public Record1(Node head) {
		map = new HashMap<Node, Node>();
		if (head != null) {
			map.put(head, null);
		}
		setMap(head);
	}
	
	private void setMap(Node head) {
		if (head == null) {
			return;
		}
		if (head.left != null) {
			map.put(head.left, head);
		}
		if (head.right != null) {
			map.put(head.right, head);
		}
		setMap(head.left);
		setMap(head.right);
	}
	
	public Node query(Node o1, Node o2) {
		HashSet<Node> path = new HashSet<Node>();
		while (map.containsKey(o1)) {
			path.add(o1);
			o1 = map.get(o1);
		}
		while (!path.contains(o2)) {
			o2 = map.get(o2);
		}
		return o2;
	}
}