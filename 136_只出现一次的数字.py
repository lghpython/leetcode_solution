from functools import  reduce
def singleNumber(nums):
    '''for i,n in enumerate(nums):
        if n not in nums[:i]+nums[i+1:]:
            return n'''
    return reduce(lambda x, y: x ^ y, nums)

print(dir(reduce))
ll = singleNumber([2,2,1])

print(ll)