'''
For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


def three_sum(arr):
	result = []
	for i in range(arr):
		result.append(two_sum(arr, i) + [i])
	return result
