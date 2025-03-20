
my_list = [8, 2, 6, 4, 5]


def bubble_sort(a_list):

	n = len(a_list)

	for i in range(n):

		already_sorted = True

		for j in range(n - i - 1):
			if a_list[j] > a_list[j + 1]:
				a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]

				already_sorted = False

		if already_sorted:
			break

	return a_list

# print(bubble_sort(my_list))



