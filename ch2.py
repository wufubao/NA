# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Newton迭代法
__author__ = 'wufubao'
import math
esp=0.0000001

def f1(x): #需要求根的方程（测试用）
	return (x-1.56)**3*(x-4.56)
def f2(x): #第二题方程
	return (1/3)*x**3-x

def deriv(x0,f): #对函数f进行求导，f是一个函数
	dx=esp
	return (f(x0+dx)-f(x0))/dx
# x0:初始值 epsilon误差 f方程所对应的函数,cont为真，
# 直接输出所有信息，包括迭代次数，否则返回计算结果
def newton(x0,epsilon,f, cont = True): #牛顿法
	count =1
	x_k=x0
	x_k1=x_k - f(x_k)/deriv(x_k,f)
	while math.fabs(x_k1 - x_k)>epsilon: #若前后迭代的变化小于epsilon则停止迭代
		x_k = x_k1
		x_k1=x_k - f(x_k)/deriv(x_k,f)
		count = count +1
	if(cont):
		print('x0=', x0 , '\t\tx*=' ,x_k1, '\t\tcount=',count)
	else:
		return x_k1

# 求得det值，f为方程所对应的函数
def get_det(f):
	det = 1
	l_det = 2
	s_det = 0.5
	while True:
		# 无法迭代到0，det太大，
		if math.fabs(newton(det,esp,f,False)-0) > 0.00001 and math.fabs(newton(-det,esp,f)-0)>0.00001:
			l_det = det
			det = (det + s_det)/2
		# 迭代到0，det太小
		else:
			if math.fabs(l_det-det) < esp:
				break
			s_det = det
			det = (det + l_det)/2
	return det

# 主函数入口
if __name__ == '__main__':
	x = 0.774596706032753
	print("-max to -1")
	k=-2
	n=50
	for i in range(n):
		newton(k,esp,f2,True)
		k = k+1/n
	newton(-1,esp,f2,True)

	print("-1 to -det")
	k=-x
	n=50
	for i in range(n):
		newton(k,esp,f2,True)
		k = k+(x-1)/n

	print("-det to det")
	k=-x
	n=50
	for i in range(n):
		newton(k,esp,f2,True)
		k = k+(2*x)/n
	newton(x,esp,f2,True)

	print("det to 1")
	k=x
	n=50
	for i in range(n):
		newton(k,esp,f2,True)
		k = k+(1-x)/n
	newton(1,esp,f2,True)

	print("1 to max")
	k=1
	n=50
	for i in range(n):
		newton(k,esp,f2,True)
		k = k+1/n
