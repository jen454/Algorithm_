def multiply(arr):
    ans = 1
    for n in arr:
        ans *= n
    return ans

def solution(num_list):
    return sum(num_list) if (len(num_list) >= 11) else multiply(num_list)