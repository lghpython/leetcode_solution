class MountainArray(list):
   def get(self, index: int) -> int:
       return self[index]
   def length(self) -> int:
       return len(self)
class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        ml = mountain_arr.length()
        l, r = 0, ml -1
        ans = -1
        while l <= r:
            mid = (r-l+1)//2
            cur = mountain_arr.get(mid)
            nex = mountain_arr.get(mid+1)
            print(r,l,mid)
            if pre > cur:
                # 所处位置为上升位置
                # 当前值大于目标值，设定mid为右边界
                if cur > target:
                    r = mid
                # 当前值小于目标值，设定mid为左边界
                elif cur < target:
                    l = mid
                # 相等记录下标值
                else:
                    if mid < ans: ans = mid
            else :
                # 当前处在下降位置
                # 当前值大于目标值,设定mid为左边界
                if cur > target:
                    l = mid
                elif cur < target:
                    r = mid
                # 相等记录下标值
                else:
                    if ans < 0 or mid < ans: ans = mid

        return ans

if __name__ == '__main__':
    l = MountainArray([0,1,2,4,2,1])
    sf = Solution()
    print(sf.findInMountainArray(3,l))