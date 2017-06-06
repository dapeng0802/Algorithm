/**
 * �ڶ��������ҵ�һ���ڵ�ĺ�̽ڵ�
 * ����Ŀ��
 *   ������һ���µĶ������ڵ��������£�
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
 *   �ýṹ����ͨ���������ṹ����һ��ָ�򸸽ڵ�� parent ָ�롣������һ�� Node ���͵Ľڵ�
 * ��ɵĶ�����������ÿ���ڵ�� parent ָ�붼ָ���Լ��ĸ��ڵ㣬ͷ�ڵ�� parent ָ�� null��
 * ֻ��һ���ڶ������е�ĳ���ڵ� node����ʵ�ַ��� node �ĺ�̽ڵ�ĺ������ڶ��������������
 * �������У�node ����һ���ڵ���� node �ĺ�̽ڵ㡣
 *   ���磬��ͼ��ʾ�Ķ�������
 *                                    6
 *                                /       \
 *                               3         9
 *                              / \       / \
 *                             1   4     8   10
 *                              \   \   /
 *                               2   5 7
 *   ��������Ľ��Ϊ��1��2��3��4��5��6��7��8��9��10
 *   ���Խڵ� 1 �ĺ��Ϊ�ڵ� 2���ڵ� 2 �ĺ��Ϊ�ڵ� 3���������ڵ� 10 �ĺ��Ϊ null��
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