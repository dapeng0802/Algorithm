/**
 * δ���������������ۼӺ�Ϊ����ֵ��������鳤��
 * ����Ŀ��
 *   ����һ������ arr�����������򣬵�ÿ��ֵ��Ϊ�������ٸ���һ������ k��
 * �� arr ������������������Ԫ����Ӻ�Ϊ k ��������鳤�ȡ�
 *   ���磬arr=[1,2,1,1,1]��k=3��
 *   �ۼӺ�Ϊ 3 ���������Ϊ [1,1,1]�����Խ������ 3��
 */
public int getMaxLength(int[] arr, int k) {
	if (arr == null || arr.length == 0 || k <= 0) {
		return 0;
	}
	int len = 0;
	int left = 0;
	int right = 0;
	int sum = arr[0];
	while (right < arr.length) {
		if (sum == k) {
			len = Math.max(len, right - left + 1);
			sum -= arr[left++];
		} else if (sum < k) {
			right++;
			if (right == arr.length) {
				break;
			}
			sum += arr[right];
		} else {
			sum -= arr[left++];
		}
	}
	return len;
}