#!/usr/bin/env python
# -*- coding: utf-8 -*-
#hello.py

import filemanager

# import requestMethod

# print 'hello world'

# name = raw_input ('please input you name \n')

# print 'hello' , name

# print 'im \'\" fine'

# letleist = ['123',345,True]

# print letleist

# print len(letleist)

# print letleist[0]

# print letleist[-1]

# letleist.pop()

# letleist[1] = '007'

# print letleist


# letsecondList =(1)

# print letsecondList

# letsecondList =(1,)

# print letsecondList

# print letleist[3]

# age = 20

# if age>=18:
# 	print 'your age is' , age
# 	pass

# names = ['yinyin','yanyan','gege','wuwu']

# for name in names:

# 	print name
# 	pass

# sum = 0

# for x in [1,2,3,4,5,6,7,8,10]:

# 	sum = x + sum
# 	print sum

#  	pass

#  	for y in range(101):
#  		sum =x +sum
#  		print sum
#  		pass


# brith = int(raw_input('input your age \n'))

# if brith < 20:
# 	print 'yonger'
# 	pass
# else :
# 	print 'older'
# 	pass


# info ={'michael':99,'bob':20,'xixi':60}

# # str = raw_input('input your name \n')


# # print info[str]

# print 'bob' in info

# print info.get('bob')

# info.pop('bob')

# print info


# print abs(-100)

# print cmp(110,120)

# print float('123')

# a = abs

# print a(-1)

# x =int(raw_input('input x -----\n'))

# def  myfunction(x):
# 	if x>=0:
# 		print x
# 		pass
# 	else :
# 		print -x
# 		pass

# print x

# import math

# def  move(s,y,step,angle=0):
# 	nx = x + step * math.cos(angle)
# 	ny = y - step * math.sin(angle)
# 	pass

# r = move(100,100,60,math.pi / 6)

# x,y = move(100,100,60,math.pi / 6)

# print x,y



# def mj(x):
# 	return x*x
# 	pass

# mjm = int(raw_input('input x  get squal \n'))

# print mj(mjm)


# def power(x,n):

# 	s =1;
# 	while n > 0:
# 		n = n - 1
# 		s = s * x
# 		return s
# 		pass

# 	pass

# lfmx = int(raw_input('input x  get squal \n'))
# lfmn = int(raw_input('input n  get squal \n'))

# print power (lfmx,lfmn)


# def  add_end(L=[]):
# 	if L is None:
# 		L =[]
# 		pass
# 	L.append('End')
# 	return L
# 	pass
#
# print add_end(['1','2','3'])
#
# print add_end()
#
# print add_end()


# def fact(n):
# 	if  n ==1:
# 		return 1;
# 	return n * fact(n-1)


# max1 =int(raw_input('input x get result \n'))

# print fact(max1)




# def  method(c):
# 	if  c == 1:
# 		return 1;
# 		pass
# 	return c * method(c-1)
# 	pass


# degitalx = int(raw_input('int put a count \n'))

# print method(degitalx)


# L = []

# n = 1

# while n < 99:
# 	L.append(n)
# 	n =n + 2
# 	pass

# print L


# L=['123','232','4323','4543534']
# i = 1
# print[L[0],L[1],L[2]]

 # for i in len(L):
 # 	L.append(L[i])
 # 	i = i+1
 # 	print L
 # 	pass

# for  x in L:
# 	print x
# 	pass

# x = range(1,100)
# print x
# L =[]
# for y in x(if y %2 ==0):
# 	pass:
# 	L.append(y*y)
# 	print L
# 	pass


# L=['AADAD','VFDSDF','QWEQWE','FADSFDAS']

# # [s.lower() for s in L]

# print [s.lower() for s in L]

# print abs(-10)

# f = abs

# print f(-123)


# def  add(x,y,z):
# 	return z(x) + z(y)
# 	pass

# print add(-100,-20,abs)

# def  f(x):
# 	return x * x
# 	pass

# print map(f,[1,2,3,4,5,6,7,8,9])

# print map(str,[1,2,3,4,5,6,7,8,9])


# def is_older(n):
# 	return n%2 ==1
# 	pass

# print filter(is_older,[1,2,3,4,5,6,7,8,9])


# def not_empty(x):
# 	return x and x.strip()
# 	pass

# print filter(not_empty,['A','','B','','c'])

# print sorted([21,2,22,11,23,56,11])

# def lazy_sum(*args):
# 	def  sum():
# 		ax =0;
# 		for  n in args:
# 			ax =ax +n
# 			return ax
# 			pass
# 		pass
# 	return sum
# 	pass

# f = lazy_sum(1,3,5,7,9)

# print f()


# let = map(lambda x: x * x,[1,2,3,4,5,6,7,8,9])

# print let

# f = lambda x:x*x

# print f(10)

# def build(x,y):
# 	return lambdab: x * x + y * y
# 	pass

# print build(100,99)

# def  now():
# 	print '2018-05-16'
# 	pass
#
#
# print now.__name__

# def log(func):
#     def wrapper(*args, **kw):
#         print 'call %s():' % func.__name__
#         return func(*args, **kw)
#     return wrapper


# print log(now)

# print int('123456',base=8)

# def  int2(x,base=2):
# 	return int(x,base=2)
# 	pass

# y = raw_input('int a num x\n')

# print int2(y,base=2)

# import functools
#
# int2 = functools.partial(int,base=16)
#
# print int2('10101010101010')


# import test
# test.testMethod()

# test.addMethod([1,2,3,4,5])

# import testmodule

# import future

# import simpleClass

# simpleClass.print_score

# testmodule.test()
# import fatherClass
#
# f = fatherClass
# print  dir(f)
#
# print help(f)

# import gloable
