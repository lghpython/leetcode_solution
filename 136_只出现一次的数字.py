def singleNumber(nums):
    if len(nums) == 1: return nums[0]
    odd = [i for i in nums if i % 2 == 1]
    even = [i for i in nums if i % 2 == 0]
    odd_len = len(odd)

    tmp = singleNumber(odd) if odd_len % 2 == 1 else singleNumber(even)
    return tmp
ll = singleNumber([2,2,1])

print(ll)