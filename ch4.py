# -*- coding: utf-8 -*-
#!/usr/bin/env python
from __future__ import division
import ch3 as Guass
import traceback
import math
def get_M(R,d):#若已经构建矩阵，直接求解得到M
	result = Guass.guass(R,d) # 求上三角
	A = result['Matrix']
	b = result['b']
	return Guass.solution(A,b) # 使用逐步消去法获得解
def get_h(x):#求h的值
	h=[]
	dem = len(x)
	for i in range(dem-1):
		h.append(x[i+1] - x[i])
	return h

def get_u(h):#求u的值
	u=[]
	dem = len(h)
	for i in range(dem-1):
		u.append(h[i]/(h[i]+h[i+1]))
	return u

def get_lamda(u):#求lamda的值
	lamda=[]
	dem = len(u)
	for i in range(dem):
		lamda.append(1-u[i])#直接由u求得
	return lamda
def get_d(y,x,f0,fn):#构建d向量，其中f0和fn为第一类型边界条件
	d=[]
	dem = len (x)
	for i in range(dem):
		if i is 0:
			dd = ((y[1]-y[0])/(x[1]-x[0])-f0)/(x[1]-x[0])
			d.append(dd)
		elif i is dem-1:
			dd = (fn-(y[i]-y[i-1])/(x[i]-x[i-1]))/(x[i]-x[i-1])
			d.append(dd)
		else:
			dd = ((y[i+1]-y[i])/(x[i+1]-x[i])-(y[i]-y[i-1])/(x[i]-x[i-1]))/(x[i+1]-x[i-1])
			d.append(dd)
	return d

def get_Matrix(u,lamda):#构建A矩阵
	dem = len(u)
	if dem != len(lamda):#维度不同的判断
		raise Exception("not the same dem!!!")
	else:
		mat=[[0 for i in range(dem+2)] for j in range(dem+2)]
		mat[0][0]=2
		mat[0][1]=1
		for i in range(dem):
			mat[i+1][i]=u[i]
			mat[i+1][i+1]=2
			mat[i+1][i+2]=lamda[i]
		mat[dem+1][dem]=1
		mat[dem+1][dem+1]=2
		return mat
def get_S(x,x_,y_,f0,fn):#获取s的值，所求的值，x_和y_为n个节点，f0和fn为第一类型边界条件
	h = get_h(x_)
	u = get_u(h)
	lamda = get_lamda(u)
	d = get_d(y_,x_,f0,fn)
	d6 = Guass.mul_row(d,6)#将d向量乘以6
	Matrix = get_Matrix(u,lamda)
	M = get_M(Matrix,d6)#求解得到M
	dem = len(x_)
	i=0
	while i<dem-1:#区间判断
		if x >=x_[i] and x<=x_[i+1]:
			s = y_[i]+((y_[i+1]-y_[i])/(x_[i+1]-x_[i])-(1/3 * M[i] + 1/6 * M[i+1])*h[i]) * (x - x_[i])\
			 + 1/2 * M[i] * (x - x_[i]) * (x - x_[i]) + 1/(6 * h[i]) * (M[i+1] - M[i]) * (x - x_[i])*(x - x_[i])*(x - x_[i])
			return s
		i = i + 1
	raise Exception("Out of the range!!!")

def print_S_func(x_,y_,f0,fn):#打印S插值函数
	h = get_h(x_)
	u = get_u(h)
	lamda = get_lamda(u)
	d = get_d(y_,x_,f0,fn)
	d6 = Guass.mul_row(d,6)
	Matrix = get_Matrix(u,lamda)
	M = get_M(Matrix,d6)
	dem = len(x_)
	i=0
	while i<dem-1:
		print("S(x) = %s + %s * (x - %s) + %s * (x- %s)^2 + %s * (x - %s)^3" %(y_[i],((y_[i+1]-y_[i])/(x_[i+1]-x_[i])-(1/3 * M[i] + 1/6 * M[i+1])*h[i]),x_[i],1/2 * M[i],x_[i],1/(6 * h[i]) * (M[i+1] - M[i]),x_[i]))
		i = i + 1
def print_temp_val(x,y,f0,fn):#打印中间变量
	h = get_h(x)
	u = get_u(h)
	print("the u is:")
	print(u)
	lamda = get_lamda(u)
	print("lamda is:")
	print(lamda)
	print("d is:")
	d = get_d(y,x,f0,fn)
	print(d)
	d6 = Guass.mul_row(d,6)
	Matrix = get_Matrix(u,lamda)
	print("Matrix is")
	Guass.print_matr(Matrix)
	M = get_M(Matrix,d6)
	print("M is")
	print(M)
def get_S_dot(x,y,f0,fn):
	dem = len(x)
	if dem != len(y):#维度不同的判断
		raise Exception("not the same dem!!!")
	N=100
	s=[]
	xx=[]
	det = abs(x[0] -x[dem-1])/N
	for i in range(N):
		s.append(get_S(x[0]+i*det,x,y,f0,fn))
		xx.append(x[0]+i*det)
	result={'y':s,'x':xx}
	return result
if __name__ == '__main__':
	# =======测试数据==========
	# y=[6,0,2]
	# x=[3,4,6]
	# f0 = 1
	# fn = -1
	# =======测试数据==========

	# =======实际数据==========
	y=[2.51,3.30,4.04,4.70,5.22,5.54,5.78,5.40,5.57,5.70,5.80]
	x=[0,1,2,3,4,5,6,7,8,9,10]
	f0 = 0.8
	fn = 0.2
	# =======实际数据==========

	print_temp_val(x,y,f0,fn)
	for i in range(10):
		x_ = i+0.5
		s = get_S(x_,x,y,f0,fn)
		print("the x is :%s and the result is :%s" %(x_,s))
	print_S_func(x,y,f0,fn)
	# s = get_S_dot(x,y,f0,fn)
	# print(s['x'])
	# print(s['y'])
