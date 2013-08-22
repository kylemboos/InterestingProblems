'''
Problem 16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''
'''thoughts:
			The fact that we can throw the answer to the power into a string makes it possible to loop through
			the string int by int and sum all of the digits very easily in python.
			
			If you are limited in space for the variable to store the number in, an array can be used of length 1000
			since 2^1000 < 10^1000 you know that the number can not be more than 1001 digits long for the array.
			
			Then for each exponent we multiply each index of the array by 2 and keep track of the carry which can only be
			0 or 1 (biggest being 9*2 = 18).
			
			At the end we have the answer with the last digit being at the front of the list.
'''

#written by: Kyle Boos (sumPower)
import time

def noStrings(exp):
	L = [0] * exp # make a list exp long
	L[0] = 1
	for power in range(exp):
		carry = 0
		for index in range(exp):
			prod = L[index] * 2 + carry
			if prod > 9:
				carry = 1
				prod = prod % 10
			else: carry = 0
			L[index] = prod
	return sum(L)

def sumPower(n):
	number = str(2 ** n)
	sum = 0
	for i in range(len(number)):
		sum += int(number[i])
	return sum
		
start = time.clock()
sum = noStrings(1000)
end = time.clock()

print sum, (end-start)
