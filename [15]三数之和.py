# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复
# 的三元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
# 
#  
# 
#  示例： 
# 
#  给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#  
#  Related Topics 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sn = sorted(nums)  # 正序列表
        ln = len(nums)
        res = []

        # 左右渐进
        for j in range(ln - 2):
            if sn[j] > 0: break
            if j > 0 and sn[j] == sn[j - 1]: continue
            l, r = j + 1, ln - 1
            while l < r:
                total = sn[j] + sn[l] + sn[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([sn[j], sn[l], sn[r]])
                    while l < r and sn[l] == sn[l + 1]: l += 1
                    while l < r and sn[r] == sn[r - 1]: r -= 1
                    l += 1
                    r -= 1
        return res
        '''
        po = sorted([a for a in nums if a > 0])   # 负数列表
        zero = [a for a in nums if a == 0]
        ne = sorted([a for a in nums if a < 0])  # 正数列表
        lp, ln = len(po), len(ne)
        if (lp == 0 or ln==0) and len(zero)<3:
            return False
        res = []
        # 有一位数为a = 0
        a = set([i for i in ne if -i in po])
        for i in a:
            res.append([0, i, -i])
        # 两位为正,一个负数
        for j in set(ne):
            l, r = 0, lp - 1
            while l < r:
                total = j + po[l] + po[r]
                if total > 0: r -= 1
                elif total < 0: l +=1
                else:
                    if {j,po[l],po[r]} not in [set(re) for re in res]:
                        res.append([j,po[l],po[r]])
                    l += 1
                    r -= 1
                    continue
        # 两数为负，一个正数
        for k in set(po):
            l,r = 0, ln-1
            while l < r:
                total = k + ne[l] + ne[r]
                if total > 0:  r -= 1
                elif total < 0: l += 1
                else:
                    if {k, ne[l], ne[r]} not in [set(re) for re in res]:
                        res.append([k, ne[l], ne[r]])
                    l+=1
                    r-=1
                    continue

        if len(res) == 0:
            return False
        # print(ne, po, res)
        return res
        '''
# leetcode submit region end(Prohibit modification and deletion)
