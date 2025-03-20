


### 1 ###
"""
Write a Python program that iterates through integers from 1 to 50. For each multiple of three,
print "Fizz" instead of the number; for each multiple of five, print "Buzz". For numbers that are multiples
of both three and five, print "FizzBuzz".

The FizzBuzz problem is a common coding challenge that is often used in programming interviews
to test basic programming skills. The problem typically requires writing a function that
prints numbers from 1 to a given limit, but with a twist:

For multiples of 3, print "Fizz" instead of the number.
For multiples of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz".
This problem helps assess the ability to use conditionals, loops, and modulus operations effectively.

"""

def fizzbuzz(start, end):

	for i in range(start, end +1):

		if i % 3 == 0 and i % 5 == 0:
			print('FizzBuzz', i)
		elif i % 3 == 0:
			print('Fizz', i)
		elif i % 5 == 0:
			print('Buzz', i)
		else:
			print(i)
# fizzbuzz(1, 50)



### 2 ###
# Prime numbers

def prime_number(start, end):

	prime_num = []

	for i in range(start, end+1):
		x = 0
		for j in range(1, i+1):
			if i % j == 0:
				x += 1
		if x == 2:
			prime_num.append(i)

	return prime_num

# print(prime_number(1, 101))

### 3 ###
# Find the largest number in a list

nr_list = [40, 21, 1, 2, 5, -100, 0, -22, 99, 1, 105]

def max_number(*args):
	for i in args:
		return max(i)

# print(max_number(nr_list))


### 4 ###
# Count occurrences of a character in a string

string_ex = 'natural number greater than 1 that is not a product of two smaller natural numbers'

def char_counter(str_ex, ch):
	counter = 0
	for char in str_ex:
		if char == ch:
			counter += 1

	return f'Your character "{ch}", appeared {counter} times'

# print(char_counter(string_ex, 'y'))



