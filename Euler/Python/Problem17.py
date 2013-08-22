'''
Problem 17.py

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

'''thoughts:
			This problem looks really fun. I can already see the pattern. Additional words like 'hundred' 'thousand' and 'and' will be needed 
			as well as modifications for the tens digits and numbers that are only 2 digits. 
			
			I decided to not create a table for each number to its word count since time really isn't issue and debugging is much easier with the actual
			words, but counts can be used directly istead of words to optimize. A shorter implementation could also uses pythons dictionary to map the numbers to strings.
			
			The total can also be calculated directly by observing how many instances of 1-9, 10-90, etc..
			
			Well that was interesting. The one edge case that got me was on each hundred number 'and' should not be appended.
			
'''
#written by: Kyle Boos
import time

def wordify(n):
	word = ''
	num = str(n)
	#1000
	if len(num) == 4: return 'onethousand'
	#hundreds
	elif len(num) == 3 :
		word += simpleWord(int(num[0]))
		word += 'hundred'
		if (int(num[1]) != 0) or (int(num[2]) != 0):
			word += 'and'
			if int(num[1]) == 1:
				word += simpleWord(int('%d%d' % (int(num[1]),int(num[2]))))
			else:
				word += tensWord(int(num[1]))
				word += simpleWord(int(num[2]))
	#tens			
	elif len(num) == 2:
		if n < 20:
			return simpleWord(n)
		else:
			word += tensWord(int(num[0]))
			word += simpleWord(int(num[1]))
	#onesies		
	else:
		word += simpleWord(n)
		
	return word

def tensWord(n):
	if n == 0: return ''
	if n == 2: return 'twenty'
	if n == 3: return 'thirty'
	if n == 4: return 'forty'
	if n == 5: return 'fifty'
	if n == 6: return 'sixty'
	if n == 7: return 'seventy'
	if n == 8: return 'eighty'
	if n == 9: return 'ninety'
	
def simpleWord(n):
	if n == 0: return ''
	if n == 1: return 'one'
	if n == 2: return 'two'
	if n == 3: return 'three'
	if n == 4: return 'four'
	if n == 5: return 'five'
	if n == 6: return 'six'
	if n == 7: return 'seven'
	if n == 8: return 'eight'
	if n == 9: return 'nine'
	if n == 10: return 'ten'
	if n == 11: return 'eleven'
	if n == 12: return 'twelve'
	if n == 13: return 'thirteen'
	if n == 14: return 'fourteen'
	if n == 15: return 'fifteen'
	if n == 16: return 'sixteen'
	if n == 17: return 'seventeen'
	if n == 18: return 'eighteen'
	if n == 19: return 'nineteen'

start = time.clock()
word = ''
count = 0
for i in range(1,1001):
	word = wordify(i)
	count += len(word)
end = time.clock()
print count, (end-start)