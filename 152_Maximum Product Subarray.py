def maxProduct(nums) -> int:

    max = nums[0]
    for i in range(len(nums)):
        pre = 1
        for num in nums[i:]:
            pre *= num
            if pre > max:
                max = pre
    return max




    '''
    class Solution:
        def maxProduct(self, nums: List[int]) -> int:
            rev = nums[::-1]
            for i in range(1, len(nums)):
                rev[i] *= rev[i - 1] or 1
                nums[i] *= nums[i - 1] or 1
            return max(rev + nums)

    '''

if __name__ == '__main__':
    maxProduct([-2, 0, -1])
    # maxProduct([2,3,-2,4])
    # maxProduct([2,3,-2,4,0,10,-1,3,-5,6,7,-7,9,8])
