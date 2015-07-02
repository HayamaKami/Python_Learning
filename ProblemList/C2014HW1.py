#the problem on https://github.com/pangfengliu/programmingtasks/issues/27
import sys

def volume(x,y,z) :
	return x * y * z

def small(x,e) :
	return x - (2 * e)

def cube_surArea(a,b,c) :
	return a * b * 2 + b * c * 2 + a * c * 2

def weird_vol(a,b,c,d,e) :
	a_small = small(a,e)
	b_small = small(b,e)
	c_small = small(c,e)
	decr = volume(a_small,b_small,d) * 2 + volume(a_small,c_small,d) * 2 + volume(b_small,c_small,d) * 2
	print(volume(a,b,c) - decr)

def weird_surArea(a,b,c,d,e) :
	a_small = small(a,e)
	b_small = small(b,e)
	c_small = small(c,e)
	print(cube_surArea(a,b,c) + (a_small + b_small + c_small) * d * 8)

a = int(input("the value of a is :"))
b = int(input("the value of b is :"))
c = int(input("the value of c is :"))
d = int(input("the value of d is :"))
e = int(input("the value of e is :"))

weird_surArea(a,b,c,d,e)
weird_vol(a,b,c,d,e)