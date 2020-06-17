# 给出一个区间的集合，请合并所有重叠的区间。 
# 
#  示例 1: 
# 
#  输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#  
# 
#  示例 2: 
# 
#  输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。 
#  Related Topics 排序 数组


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        for i in range(1,len(intervals)):
            if intervals[i-1][-1] >= intervals[i][0]:
                intervals[i][0]= min(intervals[i][0],intervals[i-1][0])
                intervals[i][1]= max(intervals[i][1],intervals[i-1][1])
                intervals[i-1] = []
        return [i for i in intervals if len(i) != 0]
