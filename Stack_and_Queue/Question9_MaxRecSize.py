#--coding=utf-8--

# 求最大子矩阵的大小
# 【题目】
#     给定一个整形矩阵 map，其中的值只有 0 和 1 两种，求其中全是 1 的所有矩形区域中，最大的矩形区域为 1 的数量。
#     例如：
#     1 1 1 0
#     其中，最大的矩形区域有 3 个 1，所以返回 3。
#     再如：
#     1 0 1 1
#     1 1 1 1
#     1 1 1 0
#     其中，最大的矩形区域有 6 个 1，所以返回 6。

def max_rec_size(map):
	if map == None or len(map) == 0 or len(map[0]) == 0:
		return 0
	max_area = 0
	height = [0 for i in range(len(map[0]))]
	for i in range(len(map)):
		for j in range(len(map[0])):
			height[j] = 0 if map[i][j] == 0 else height[j] + 1
		max_area = max(max_rec_from_bottom(height), max_area)
	return max_area

def max_rec_from_bottom(height):
	if height == None or len(height) == 0:
		return 0
	max_area = 0
	stack = []
	for i in range(len(height)):
		while len(stack) != 0 and height[i] <= height[stack[-1]]:
			j = stack.pop()
			k = -1 if len(stack) == 0 else stack[-1]
			cur_area = (i - k - 1) * height[j]
			max_area = max(max_area, cur_area)
		stack.append(i)
	while len(stack) != 0:
		j = stack.pop()
		k = -1 if len(stack) == 0 else stack[-1]
		cur_area = (i - k - 1) * height[j]
		max_area = max(max_area, cur_area)
	return max_area

def test():
	map = [[1,0,1,1],[1,1,1,1],[1,1,1,0]]
	print max_rec_size(map)
	

if __name__ == '__main__':
	test()
