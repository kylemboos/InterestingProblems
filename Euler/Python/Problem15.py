''' Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
	
	How many such routes are there through a 20x20 grid?
'''

'''thoughts:

	I took some time to really think about this one and drew out some of the boxes to look for patterns between bigger squares as they grow.
	
	I noticed the top and bottom of the grid increase by one with the base case of 1 square being 2 paths. I started to get the sense the the squares could be linearized
	and use memoization	but I could not quite figure out how to piece it together. This code was not written by me but solves the problem in the way in which I was trying to approach it.
	
	Written and explained here: http://code.jasonbhill.com/python/project-euler-problem-15/
'''

import time

def calcRoute(gridSize):
	squares = [1]*gridSize
	for i in range(gridSize):
		for j in range(i):
			squares[j] = squares[j] + squares[j-1]
		squares[i] = 2 * squares[i-1]
	return squares[gridSize-1]
		
start = time.clock()
answer = calcRoute(50000)
end = time.clock()

print answer, (end-start)