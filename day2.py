### 1 ###
# Fibonacci

# Ex 1 1 2 3 5 8 13 21
# Simple fibo
def fibonacci(nr):
	x = 0
	fibo = [1, 1]
	while x < nr:
		a = fibo[-2]
		b = fibo[-1]
		c = a + b
		fibo.append(c)
		x += 1
	else:
		return fibo

# print(fibonacci(10))

# ------------------------------ #

# Fibo recursion
def fibonacci_recursion(nr):
	if nr in {0, 1}:
		return nr
	return fibonacci_recursion(nr-1) + fibonacci_recursion(nr-2)

# fibo = 10
# for i in range(fibo):
# 	print(fibonacci_recursion(i))

# ------------------------------ #


### 2 ###
# Factorial using recursion

def factorial(x):
	if x == 1:
		return x
	return x * factorial(x-1)

# print(factorial(10))




### 3 ###
# Multiplication table

def multi_table(x):
	for i in range(1, x+1):
		for j in range(1, x+1):

			print(i * j, end='\t')
		print()

# multi_table(10)




### 4 ###
# Reverse a string without using slicing
# b = "Hello world"
# print(b[2:5]) - slicing

b = "Hello world"
# print(''.join(reversed(b)))




### 5 ###
# Sort a list without using sort()

nr_list2 = [40, 21, 1, 2, 5, -100, 0, -22, 99, 1, 105]


def list_sort(my_list):
	x = 0
	ordered_list = []
	while len(ordered_list) != len(my_list):
		if my_list[x] == min(my_list):
			ordered_list.append(my_list[x])
			x += 1
		print(x)
	return ordered_list

# print(list_sort(nr_list2))
print(min(nr_list2))