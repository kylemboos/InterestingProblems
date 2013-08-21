'''
The following iterative sequence is defined for the set of positive integers:

n --> n/2 (n is even)
n --> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 --> 40 --> 20 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
'''

'''thoughts: 
			Time to code up the brute force solution first. making the collatz function will be trivial then just keep track and loop.
			That works but takes a minute or maybe a little longer.
		
			Unlike the factor problem.. this one will finally work dynamically with a map. YESS lets code it.
			.
			.
			.
			OMG SO BEAUTIFUL. Brute force takes 73 seconds to complete. Dynamic soltion takes 6. SIX. SIIIIIIIIIIIIIHHHHIIIIIIIX
'''

#written by: Kyle Boos
import time

def collatz(n):
	if n % 2 == 0:
		n = n/2
	else:
		n = (3*n)+1
	return n

def collatzDynamic(n, map, chain, count):
	if n == 1:
		return count
	if n in map:
		count += map[n]
		return count
	else:
		n = collatz(n)
		chain.append(n)
		count += 1
		return collatzDynamic(n, map, chain, count)

		
		

#Dynamic Solution!
start = time.clock()
map = {}
longest = 0
largest = 13
chain = []
for i in range(13,1000001):
	count = collatzDynamic(i,map,[i], 0)
	map[i] = count
	if count >= longest:
		longest = count
		largest = i	
end = time.clock()
print largest , (end-start)

#Brute Force
'''start = time.clock()
longest = 0
largest = 13
for i in range(13,1000001):
	n = i
	chain = [n]
	while n != 1:
		n = collatz(n)
		chain.append(n)
	if len(chain) >= longest:
		longest = len(chain)
		largest = i
end = time.clock()
print largest, (end-start)'''
