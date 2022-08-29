def solution(numbers, target_sum):
    calc_numbers = {}
    for n in numbers:
        y = target_sum - n
        if y in calc_numbers:
            return [y, n]
        else:
            calc_numbers[n] = True
    return []


arr = [4, 1, 2, -2, 11, 15, 1, -1, -6, -4]
target = 9
print(solution(arr, target))