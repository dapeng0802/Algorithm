#--coding=utf-8--

# 最大值减去最小值小于或等于 num 的子数组数量
# 【题目】
#     给定数组 arr 和整数 num，共返回有多少个子数组满足如下情况：
#     max(arr[i..j]) - min(arr[i..j]) <= num
#     max(arr[i..j]) 表示子数组 arr[i..j] 中的最大值，min(arr[i..j]) 表示子数组 arr[i..j] 中的最小值。
# 【要求】
#     如果数组长度为 N，请实现时间复杂度为 O(N) 的解法。

from collections import deque

def get_num(arr, num):
	if arr == None or len(arr) == 0:
		return 0
	queue = deque()
	count = 0
	for i in range(len(arr)):
		while len(queue) > 0 and (arr[i] - min(queue) > num or max(queue) - arr[i] > num):
			count += len(queue)
			queue.popleft()
		queue.append(arr[i])
	while len(queue) > 0:
		count += len(queue)
		queue.popleft()
	return count

# 以上是我所想到的解法，思路和书中不谋而合，使用双向队列;
# 以下是书中的解法，但我个人认为我的解法较为简单，时间复杂度和空间复杂度都符合要求。

def get_num2(arr, num):
	if arr == None or len(arr) == 0:
		return 0
	qmin = deque()
	qmax = deque()
	i, j, res = 0, 0, 0
	while i < len(arr):
		while j < len(arr):
			while len(qmin) > 0 and arr[qmin[-1]] >= arr[j]:
				qmin.pop()
			qmin.append(j)
			while len(qmax) > 0 and arr[qmax[-1]] <= arr[j]:
				qmax.pop()
			qmax.append(j)
			if arr[qmax[0]] - arr[qmin[0]] > num:
				break
			j += 1
		if qmin[0] == i:
			qmin.popleft()
		if qmax[0] == i:
			qmax.popleft()
		res += j - i
		i += 1
	return res

def test():
	arr = [2,6,8,4,12,16,3,6,13,7,11,24,28,14,31]
	print get_num(arr, 5)
	print get_num2(arr, 5)
	

if __name__ == '__main__':
	test()
