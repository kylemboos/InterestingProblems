'''
Problem 9:

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

#written by Kyle Boos

#thoughts:  well lets implement the obvious brute force solution first
#			since we are only dealing with a loop < 500


#helpers for computation
def checkSum(a,b,c):
	if (a+b+c) == 1000:
		return True 
	return False
	
def square(i):
	return i*i
	
def pythag(a,b,c):
	if (square(a) + square(b)) == square(c):
		return True
	return False
	

#brute. force. wow so clean.... jk n^3.
for a in range (1,500):
	for b in range(1,500):
		for c in range(1,500):
			if pythag(a,b,c):
				if checkSum(a,b,c):
					print a*b*c
					
# so we get the answer 200,375,425 but there must be a better way that
# dosen't involve having to take a coffee break to get the answer.