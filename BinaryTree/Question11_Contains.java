/**
 * �ж� t1 ���Ƿ���� t2 ��ȫ�������˽ṹ
 * ����Ŀ��
 *   �����˴˶�����������ͷ�ڵ�ֱ�Ϊ t1 �� t2���ж� t1 ���Ƿ���� t2 ��ȫ�������˽ṹ��
 *   ���磬��ͼ��ʾ�� t1 ���� t2 ����
 *   
 *                          1
 *                        /   \
 *                       2     3                     2
 *                     /  \   / \                   / \
 *                    4    5 6   7                 4   5
 *                   / \  /                       /
 *                  8  9 10                      8
 *                  
 *   t1 ������ t2 ��ȫ�������˽ṹ�����Է��� true��
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