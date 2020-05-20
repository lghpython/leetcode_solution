class Solution:
    def convert(self, s: str, numRows: int) -> str:
       ''' # 字符串长度
        lens = len(s)
        if numRows == 1:
            return s
        elif numRows == 2:
            return ''.join([s[o] for o in range(0,lens,2)]+[s[e] for e in range(1,lens,2)])
        tmp = [[] for i in range(numRows)]
        a = 0
        pre_a = -1

        for n in range(lens):
            # 从上到下，填入二维列表
            if a < numRows and a > pre_a:
                pre_a = a
                tmp[a].append(s[n])
                # print("+", s[n])
                a += 1
                if a == numRows:
                    a -= 2

            elif a >= 0 and a < pre_a :
                pre_a = a
                tmp[a].append(s[n])
                # print("-",s[n])
                a -= 1
                if a <= 0 :
                    a = 0
                    pre_a = -1

        # print(tmp)

        return ''.join([ ''.join(tmp[n]) for n in range(numRows)])
'''
       # 字符串长度
       lens = len(s)
       cur = 0
       goingDown = False
       tmp = [[] for i in range(min(numRows, lens))]
       for c in s:

           tmp[cur].append(c)
           # 从上到下，填入二维列表
           if cur == 0 or cur == numRows - 1: goingDown = not goingDown
           cur += 1 if goingDown else -1
           print(tmp)

       return ''.join([''.join(tmp[n]) for n in range(numRows)])


if __name__ == '__main__':
    # s = "ABCD"
    s = "LEETCODEISHIRING"
    # s = "PAYPALISHIRING"

    sc = Solution()

    result = sc.convert(s=s,numRows=2)
    print(result)
    # tmp = [['a','b','c','d'],['d','f','g','h'],['i','j','k','l'],['m','n','o','p']]
    # print(''.join([''.join(tmp[n]) for n in range(4)]))
