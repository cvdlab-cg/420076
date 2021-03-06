from pyplasm import *
import random

mtrx = []


def RNDM (x,y):
	f = (COS(x)+SIN(y))*random.random()
	m = [x,y,f]
	mtrx.append(m)
	return f 


dom1 = INTERVALS(20)(60)
dom2 = INTERVALS(40)(60)
domain = PROD([dom1,dom2])

def mountain (v):
	a = v[0]
	b = v[1]
	return [a, b, RNDM(a,b)]


model = MAP(mountain)(domain)
mountains = COLOR([0.6,0.4,0.2])(model)

VIEW(mountains)