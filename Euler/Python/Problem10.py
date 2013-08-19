'''

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''
#written by Kyle Boos

'''thoughts: The straightforward way to check for primality is to ensure that for all numbers
			 from 2 to n, n % m is not equal to 0 or else the number would not be prime.
			 
'''

# written by Kyle Boos
import math

#brute force prime check for any given number. Really. really. slow.
def primeTest(n):
	for i in range(2,n):
		if n % i == 0:
			return False
			
	return True

#now we will implement the sieve of Eratosthenes technique for checking primes.
#returns a boolean array where each true index is a prime.
def eratosCheck(n):
	m = int(math.sqrt(n))
	numbers = [True]*(n+1)
	
	for i in range(2,m):
		if numbers[i] is True:
			for j in range(i*i,n,i):
				numbers[j] = False
		
	return numbers
	

sum = 0
primes = eratosCheck(2000000)
for i in range(2,2000000):
	if primes[i] is True:
		sum+=i
print sum