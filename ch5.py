# -*- coding: utf-8 -*-
#!/usr/bin/env python
from __future__ import division
import traceback
import math
PI = math.pi
esp = 0.5E-5
N = 5
a = 0
b = PI/3
c = 0
d = PI/6
def f(x,y):
	return math.tan(x**2 + y**2)
def print_matr(Matrix): # print the matrix
	for mat in Matrix:
		print(mat)
def frange(x, y, jump): # the range function in python is not working when the
	while x < y:		# var is float type, so define a float type range function
		yield x			# to gen the seq_ in for
		x += jump
#the var of a,b,c,d is the integration duration of x,y in f(x,y)
def get_result(a,b,c,d,f):
	T = [([0] * N) for i in range(N)]
	E = [([0] * N) for i in range(N)]
	s=0
	pre =0
	for i in range(N): # calc the init T matrix
		m = 2**i
		n = 2**i
		h = (b-a)/m
		k = (d-c)/n
		for p in frange(a,b,h):
			for q in frange(c,d,k):
				s = s + f(p,q) + f(p+h,q) + f(p,q+k) + f(p+h,q+k)
		T[i][0] = h*k/4 * s
		E[i][0] = math.fabs(pre - T[i][0])
		pre = T[i][0]
		s = 0
	for j in range(1,N):
		for i in range(N-j):
			T[i][j] = 4**j/(4**j-1)*T[i+1][j-1] - 1/(4**j-1)*T[i][j-1]
			E[i][j] = math.fabs(pre - T[i][j]) # get the error
			if E[i][j] > esp:
				pre = T[i][j]
			else:
				break
	return {'T':T,'E':E,'result':T[0][N-1],'error':E[0][N-1]}
if __name__ == '__main__':
	result = get_result(a,b,c,d,f)
	print("the calculated Matrix is:")
	print_matr(result['T'])
	print("\nthe error Matrix is:")
	print_matr(result['E'])
	print("\nthe result is")
	print(result['result'])
	print("\nthe error is")
	print(result['error'])
