# -*- coding: utf-8 -*-
#!/usr/bin/env python
# 列主元的Gauss消去伐
# 需要注意的是所有的下标都是从0开始
__author__ = 'wufubao'
import math
_ACC_ = 5 #精确度
# 测试用数据test*x=b,x为解
test = [[2,-4,6], [4,-9,2], [1,-1,3] ]
b = [3,5,4]
# 问题数据
R = [[31,-13,0,0,0,-10,0,0,0],\
	[-13,35,-9,0,-11,0,0,0,0],\
	[0,-9,31,-10,0,0,0,0,0],\
	[0,0,-10,79,-30,0,0,0,-9],\
	[0,0,0,-30,57,-7,0,-5,0],\
	[0,0,0,0,-7,47,-30,0,0],\
	[0,0,0,0,0,-30,41,0,0],\
	[0,0,0,0,0,-5,0,27,-2],\
	[0,0,0,-9,0,0,0,-2,29]\
	]
V=[-15,27,-23,0,-20,12,-7,7,10]


def print_matr(Matrix): # print the matrix
	for mat in Matrix:
		print(mat)

# 返回最大值及其坐标
# Matrix为待求矩阵，col为第col列
# 返回值pos为位置，absmax为元素最大值
def get_max(Matrix,col=0):
	dem = len(Matrix)
	col_list =[x[col] for x in Matrix]
	absList = list(map(math.fabs, col_list))[col:dem]
	absmax = max(absList)
	pos = col + absList.index(absmax)
	return {'pos': pos, 'absmax':absmax}

# 利用列主元高斯法化为等价三角形
# Matrix为待求矩阵A，b=Ax
# 返回值为Matrix和b
def guass(Matrix,b):
	dem = len(Matrix)
	for i in range(dem):
		result = get_max(Matrix,i)
		pos = int(result['pos'])
		absmax = result['absmax']
		if pos != i:	#若本行为主元，则不交换
			Matrix[pos],Matrix[i] = Matrix[i],Matrix[pos]
			b[pos],b[i] = b[i],b[pos]
		for j in range(i+1,dem):
			if math.fabs(Matrix[j][i]) <= 0.0000000000001:	#若当主元下三角所对应的元素为0时
				continue									#跳过计算
			b[j] = b[j] - b[i] * Matrix[j][i]/absmax	#b
			Matrix[j] = sub_map(Matrix[j], mul_row(Matrix[i],Matrix[j][i]/absmax) )	#Matrix
	return {'Matrix':Matrix, 'b':b}

# 三角方程组的解法
# Matrix为上三角矩阵A，b=Ax
# 返回值为解x
def solution(M,b):
	dem = len(M)
	x=[]
	x.append(b[dem-1]/M[dem-1][dem-1])	# 第一步直接求解
	for i in range(dem-1):
		ii = dem - i - 2
		sol = x[:]
		sol.reverse() #由于从下开始，故解需要调换顺序
		ans = (b[ii]- mul_map(M[ii][ii+1:dem],sol))/M[ii][ii]
		x.append(ans)
	x.reverse()
	return x

# 向量运算的一些定义
def sub(a,b):	#基本加法定义
	return a-b
def mul(a,b):	#基本乘法定义
	return a*b
def mul_row(R,b): #列向量R中的元素同时乘以b
	r=R[:]
	dem = len(r)
	for i in range(dem):
		r[i] = r[i]*b
	return r
def mul_map(R1,R2): #向量R1和向量R2的标准内积
	r1=R1[:]
	r2=R2[:]
	return sum(list(map(mul,r1,r2)))
def sub_map(r1,r2): #向量R1和向量R2相减
	return list(map(sub,r1,r2))
def valid(num):
	v = 10**(_ACC_+1)
	n = int(num*v)
	rest = n % 10
	if rest >= 5:
		ans = (n+5)/(v)
	else:
		ans = n/(v)
	return ans
def valid_map(r):
	return list(map(valid,r))

# main函数入口
if __name__ == '__main__':
	result = guass(R,V) # 求上三角
	A = result['Matrix']
	b = result['b']
	print('A is :')
	print_matr(A)
	print('b is :')
	print(b)
	print('solution is :')
	result=solution(A,b) # 使用逐步消去法获得解
	print(result)
	print('Values after the decimal point five digits:')
	res = valid_map(result) # 打印结果保留5位有效数字
	print(res)