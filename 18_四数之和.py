def fourSum(nums, target: int) :
    n = len(nums)
    total = []
    if n < 4:  return total
    nums.sort()
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]: continue
        if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target: break
        if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target: continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]: continue
            if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target: break
            if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target: continue
            l, r = j + 1, n - 1
            while l < r:
                sum = nums[l] + nums[r] + nums[i] + nums[j]
                if sum < target:
                    l += 1
                elif sum > target:
                    r -= 1
                else:
                    total.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    r -= 1
                    while nums[r] == nums[r + 1] and l < r:
                        r -= 1

    return total
    '''n = sorted(nums)
    ln = len(n)
    ans = []
    for i in range(ln - 3):
        if i > 0 and n[i] == n[i - 1]: continue
        l, r = i + 1, ln - 1
        tsum = target - n[i]

        while l < ln-2:

            # print(l)
            if l > i+1 and n[l] == n[l - 1]:
                l += 1
                continue
            r = ln - 1
            while  r > l + 1:
                if r < ln-1 and n[r] == n[r + 1]:
                    r -= 1
                    continue
                if tsum - n[l]-n[r] in n[l + 1:r]:
                    ans.append([n[i], n[l], tsum - n[l]-n[r], n[r]])
                r -= 1
            l += 1
    return ans'''
if __name__ == '__main__':
    # l = [1, 0, -1, 0, -2, 2]
    # t = 0
    # print(fourSum(l, t))
    # l = [0, 0, 0, 0]
    # t = -1
    # print(fourSum(l, t))
    # l = [-3,-1,0,2,4,5]
    # t =2
    # print(fourSum(l, t))
    l = [-3,-2,-1,0,0,1,2,3]
    t = 0
    print(fourSum(l, t))