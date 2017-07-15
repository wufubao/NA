# -*- coding: utf-8 -*-

#!/usr/bin/env python

__author__ = 'wufubao'

def get_acc(n):
	if not isinstance(n, int):
		raise TypeError('bad operand type, the N must be int type')
	else:
		return 0.5*(1.5 - 1/n - 1/(n+1))
def get_l2s(n):
	sum = 0.0
	if not isinstance(n, int):
		raise TypeError('bad operand type, the N must be int type')
	else:
		while(n > 1):
			sum = float(sum + 1/(n*n-1))
			n = n - 1
		return sum

def get_s2l(n):
	sum = 0.0
	i = 2
	if not isinstance(n, int):
		raise TypeError('bad operand type, the N must be int type')
	else:
		while(i <= n):
			sum = float(sum + 1/(i*i-1))
			i = i + 1
		return sum


if __name__ == '__main__':
	n = input('please input the number of the N\n')
	acc = get_acc(int(n))

	sum_l2s = get_l2s(int(n))

	sum_s2l = get_s2l(int(n))
	print('the acc result is : ', acc , ' when N is: ', n, '\n')
	print('the l2s result is : ', sum_l2s, ' when N is: ', n, '\n')
	print('the s2l result is : ', sum_s2l, ' when N is: ', n, '\n')

