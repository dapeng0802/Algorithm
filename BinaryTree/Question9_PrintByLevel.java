/**
 * 二叉树的按层打印与 ZigZag 打印
 * 【题目】
 *   给定一棵二叉树的头节点 head，分别实现按层打印和 ZigZag 打印二叉树的函数。
 *   例如，二叉树如下图所示。
 *                                    1
 *                                   / \
 *                                  2   3
 *                                 /   / \
 *                                4   5   6
 *                                   / \
 *                                  7   8
 *   按层打印时，输出格式必须如下：
 *   Level 1 : 1
 *   Level 2 : 2 3
 *   Level 3 : 4 5 6
 *   Level 4 : 7 8
 *   
 *   ZigZag 打印时，输出格式必须如下：
 *   Level 1 from left to right : 1
 *   Level 2 from right to left : 3 2
 *   Level 3 from left to right : 4 5 6
 *   Level 4 from right to left : 8 7
 */
public void printByLevel(Node head) {
	if (head == null)
		return;
	Queue<Node> queue = new LinkedList<Node>();
	int level = 1;
	Node last = head;
	Node nLast = null;
	queue.offer(head);
	System.out.print("Level " + (level++) + " : ");
	while (!queue.isEmpty()) {
		head = queue.poll();
		System.out.print(head.value + " ");
		if (head.left != null) {
			queue.offer(head.left);
			nLast = head.left;
		}
		if (head.right != null) {
			queue.offer(head.right);
			nLast = head.right;
		}
		if (head == last && !queue.isEmpty()) {
			System.out.print("\nLevel " + (level++) + " : ");
			last = nLast;
		}
	}
	System.out.println();
}