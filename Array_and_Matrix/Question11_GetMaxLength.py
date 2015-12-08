#--coding=utf-8--

# 未排序数组中累加和为给定值的最长子数组系列问题
# 【题目】
#     给定一个无序数组 arr，其中元素可正、可负、可 0，给定一个整数 k。求 arr 所有的子数组中累加和为 k 的最长子数组长度。
# 【补充题目】
#     给定一个无序数组 arr，其中元素可正、可负、可 0。求 arr 所有的子数组中正数与负数个数相等的最长子数组长度。
# 【补充题目】
#     给定一个无序数组 arr，其中元素只是 1 或 0。求 arr 所有的子数组中 0 和 1 个数相等的最长子数组长度。

def max_length(arr, k):
	if not arr or len(arr) == 0:
		return 0
	dic = dict()
	dic[0] = -1
	length, summy = 0, 0
	for i in xrange(len(arr)):
		summy += arr[i]
		if dic.has_key(summy - k):
			length = max(i - dic.get(summy - k), length)
		if not dic.has_key(summy):
			dic[summy] = i
	return length

def max_length1(arr):
	if not arr or len(arr) == 0:
		return 0
	arr_tmp = []
	for i in xrange(len(arr)):
		arr_tmp.append(1 if arr[i] > 0 else (-1 if arr[i] < 0 else 0))
	return max_length(arr_tmp, 0)

def max_length2(arr):
	if not arr or len(arr) == 0:
		return 0
	arr_tmp = []
	for i in xrange(len(arr)):
		arr_tmp.append(-1 if arr[i] == 0 else arr[i])
	return max_length(arr_tmp, 0)


def test():
	arr = [1, 2, 3, 3, -1, 1, 1, 1, 1]
	k = 6
	print max_length(arr, k)
	arr = [1, 1, 2, 4, -3, -5, -6, 2, 5, 0, 1, 7]
	print max_length1(arr)
	arr = [1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1]
	print max_length2(arr)

if __name__ == '__main__':
	test()
