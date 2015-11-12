#--coding=utf-8--

# 生成窗口最大值数组
# 【题目】
#     有一个整型数组 arr 和一个大小为 w 的窗口从数组的最左边滑到最右边，窗口每次向右边滑一个位置。
#     例如，数组为[4,3,5,4,3,3,6,7]，窗口大小为3时：
#     [4 3 5] 4 3 3 6 7    窗口中最大值为5
#     4 [3 5 4] 3 3 6 7    窗口中最大值为5
#     4 3 [5 4 3] 3 6 7    窗口中最大值为5
#     4 3 5 [4 3 3] 6 7    窗口中最大值为4
#     4 3 5 4 [3 3 6] 7    窗口中最大值为6
#     4 3 5 4 3 [3 6 7]    窗口中最大值为7
#     如果数组长度为 n，窗口大小为 w，则一共产生 n-w+1 个窗口的最大值。
#     请实现一个函数。
#     输入：整型数组 arr，窗口大小为 w。
#     输出：一个长度为 n-w+1 的数组 res，res[i] 表示每一种窗口状态下的最大值。
#     以本题为例，结果应该返回{5,5,5,4,6,7}。

def get_max_window(arr, w):
	result = []
	for i in range(len(arr) - w + 1):
		max_value = arr[i]
		for j in range(w):
			if arr[i + j] > max_value:
				max_value = arr[i + j]
		result.append(max_value)
	return result

# 以上为我第一时间想到的解法，但时间复杂度比较高，为 O(n*w)
# 以下的解法为书中的思路，时间复杂度为 O(n)

def get_max_window2(arr, w):
	result = []
	from collections import deque
	qmax = deque()
	for i in range(len(arr)):
		while len(qmax) != 0 and arr[qmax[-1]] <= arr[i]:
			qmax.pop()
		qmax.append(i)
		if qmax[0] == i - w:
			qmax.popleft()
		if i >= w - 1:
			result.append(arr[qmax[0]])
	return result

def test():
	arr = [7,3,5,4,8,3,6,5]
	print get_max_window(arr, 3)
	print get_max_window2(arr, 3)

if __name__ == '__main__':
	test()
