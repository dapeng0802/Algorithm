#--coding=utf-8--

# 用栈来求解汉诺塔问题
# 【题目】
#     汉诺塔问题比较经典，这里修改一下游戏规则：现在限制不能从最左侧的塔直接移动到最右侧，
# 也不能从最右侧的直接移动到最左侧，而是必须经过中间。求当塔有 N 层的时候，打印最优移动过程
# 和最优移动总步数。
#     例如，当塔数为两层时，最上层的塔记为1，最下层的塔记为2，则打印：
#         Move 1 from left to mid
#         Move 1 from mid to right
#         Move 2 from left to mid
#         Move 1 from right to mid
#         Move 1 from mid to left
#         Move 2 from mid to right
#         Move 1 from left to mid
#         Move 1 from mid to right
#         It will move 8 steps.

# 解法1. 递归
def Hanoi(floors, left, mid, right):
	if floors < 1:
		return 0
	return process(floors, left, mid, right, left, right)

def process(floors, left, mid, right, src, des):
	if floors == 1:
		if src == mid or des == mid:
			print 'Move 1 from', src, 'to', des
			return 1
		else:
			print 'Move 1 from', src, 'to', mid
			print 'Move 1 from', mid, 'to', des
			return 2
	if src == mid or des == mid:
		another = right if src == left or des == left else left
		part1 = process(floors - 1, left, mid, right, src, another)
		part2 = 1
		print 'Move', floors, 'from', src, 'to', des
		part3 = process(floors - 1, left, mid, right, another, des)
		return part1 + part2 + part3
	else:
		part1 = process(floors - 1, left, mid, right, src, des)
		part2 = 2
		print 'Move', floors, 'from', src, 'to', mid
		part3 = process(floors - 1, left, mid, right, des, src)
		part4 = 1
		print 'Move', floors, 'from', mid, 'to', des
		part5 = process(floors - 1, left, mid, right, src, des)
		return part1 + part2 + part3 + part4 + part5

# 解法2. 栈
from enum import Enum
Action = Enum('Action', 'No, LToM, MToL, MToR, RToM')

def HanoiByStack(floors, left, mid, right):
	lS, mS, rS = [], [], []
	import sys
	lS.append(sys.maxint)
	mS.append(sys.maxint)
	rS.append(sys.maxint)
	i = floors
	while i > 0:
		lS.append(i)
		i = i - 1
	record = [Action.No]
	step = 0
	while len(rS) != floors + 1:
		step += sStackTodStack(record, Action.MToL, Action.LToM, lS, mS, left, mid)
		step += sStackTodStack(record, Action.LToM, Action.MToL, mS, lS, mid, left)
		step += sStackTodStack(record, Action.RToM, Action.MToR, mS, rS, mid, right)
		step += sStackTodStack(record, Action.MToR, Action.RToM, rS, mS, right, mid)
	return step

def sStackTodStack(record, preNoAct, nowAct, sStack, dStack, src, des):
	if record[0] != preNoAct and sStack[-1] < dStack[-1]:
		dStack.append(sStack.pop())
		print 'Move', dStack[-1], 'from', src, 'to', des
		record[0] = nowAct
		return 1
	return 0

def test():
	Hanoi(3, 'left', 'mid', 'right')
	print '*****************************'
	HanoiByStack(3, 'left', 'mid', 'right')

if __name__ == '__main__':
	test()