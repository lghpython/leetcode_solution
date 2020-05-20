def subarraySum(nums, k: int) -> int:
    l = len(nums)
    count, pre = 0, 0
    tmp = {0: 1}
    for i in range(l):
        pre += nums[i]
        if pre - k in tmp.keys():
            count += tmp.get(pre - k)
        tmp[pre] = tmp[pre] + 1 if pre in tmp.keys() else 1

    return count;

    '''
    l = len(nums)
    times = 0
    for i in range(l):
        count = 0
        for j in range(i,-1,-1):
            count += nums[j] 
            if count == k:
                times += 1

    return times
    '''


if __name__ == '__main__':
    print(subarraySum([100,1,2,3,4],3))