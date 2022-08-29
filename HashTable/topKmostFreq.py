def solution(numbers, k):
    hash_map = {}
    
    for n in numbers:
        if n not in hash_map:
            hash_map[n] = 0
        hash_map[n] += 1
    #print(hash_map)   --> {1: 3, 3: 2, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1}
    freq = {}
    for number, count in hash_map.items():
        if count not in freq:
            freq[count] = []
        freq[count].append(number)
    ##print(freq)   -->  {3: [1], 2: [3], 1: [5, 6, 7, 8, 9, 10]}
    result = []
    for n in reversed(range(len(numbers)+1)):
        if n in freq:
            result.extend(freq[n])
            
    return result[:k]



k = 2
numbers = [1, 1, 1, 3, 3, 5, 6, 7, 8, 9, 10]

print(solution(numbers, k))