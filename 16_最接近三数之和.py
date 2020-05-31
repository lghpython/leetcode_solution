class Solution:
    def threeSumClosest(self, nums, target) -> int:
        ln = len(nums)
        n = sorted(nums)
        if ln< 3: return
        ans = n[0] + n[1] + n[2]
        for i in range(ln):
            l, r = i+1, ln-1
            while  l<r:
                total = n[i] + n[l] +n[r]
                # print(total)
                if abs(total-target)< abs(ans-target):
                    ans = total
                if total > target:
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    return target
        return ans


if __name__ == '__main__':

    l = [6,-18,-20,-7,-15,9,18,10,1,-20,-17,-19
               ,-3,-5,-19,10,6,-11,1,-17,-15,6,17,-18,-3,16,19,-20
               ,-3,-17,-15,-3,12,1,-9,4,1,12,-2,14,4,-4,19,-20,6,0,-19,18,14
               ,1,-15,-5,14,12,-4,0,-10,6,6,-6,20,-8,-6,5,0,3,10,7,-2,17,20,12,19,-13,-1
               ,10,-1,14,0,7,-3,10,14,14,11,0,-4,-15,-8,3,2,-5,9,10,16,-4,-3,-9,-8,-14,10,6,
            2,-12,-7,-16,-6,10]
