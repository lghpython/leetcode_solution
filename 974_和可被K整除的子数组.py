class Solution:
    def subarraysDivByK(self, A, K) -> int:
        # res = 0
        # total = 0
        # record = {0:1} # 记录余数
        # for i in A:
        #     total += i
        #     mo = total%K
        #     s = record.get(mo,0)
        #     res += s
        #     record[mo] = s + 1
        # return res
        pres = 0
        res = 0
        count = [1] + [0]*K
        for i in A:
            pres = (pres+i)%K
            res += count[pres]
            count[pres] += 1
        return res