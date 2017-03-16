/**
 * ���ظ���ӡ������������Ӻ�Ϊ����ֵ�����ж�Ԫ�����Ԫ��
 * ����Ŀ��
 *   ������������ arr ������ k�����ظ���ӡ arr ��������Ӻ�Ϊ k �Ĳ������Ԫ�顣
 *   ���磬arr=[-8,-4,-3,0,1,2,4,5,8,9]��k=10����ӡ���Ϊ��
 *   1,9
 *   2,8
 */
public void printUniquePair(int[] arr, int k) {
	if (arr == null || arr.length < 2) {
		return;
	}
	int left = 0;
	int right = arr.length - 1;
	while (left < right) {
		if (arr[left] + arr[right] < k) {
			left++;
		} else if (arr[left] + arr[right] > k) {
			right--;
		} else {
			if (left == 0 || arr[left - 1] != arr[left]) {
				System.out.println(arr[left] + "," + arr[right]);
			}
			left++;
			right--;
		}
	}
}