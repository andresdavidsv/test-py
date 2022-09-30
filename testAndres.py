def check_valid_additions(arr_1: list, arr_2: list, total: int) -> None:

	index = 0

	while index < len(arr_1):
		for value in arr_2:
			if arr_1[index] + value == total:
				print()
				print(arr_1[index], value)
				print()
		index = index + 1

numbers = [11, 3, 12, 0, -1, 9, 5, 4]
total = 12

apply = []

numbers_half = int(len(numbers)/2)

arr_1 = numbers[:numbers_half]
arr_2 = numbers[numbers_half:]

check_valid_additions(arr_1, arr_2, total)
check_valid_additions(arr_1, arr_1[::-1], total)