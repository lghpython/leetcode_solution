def isMatch( s: str, p: str) -> bool:
    ls, lp = len(s), len(p)
    # 初始化动态表
    dp = [[False for _ in range(lp + 1)] for _ in range(ls + 1)]
    dp[0][0] = True
    # 动态检查的前置条件
    for j in range(2, lp + 1):
        dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'

    for i in range(1, ls + 1):
        for j in range(1, lp + 1):
            m, n = i - 1, j - 1
            if p[n] == '*':
                if s[m] == p[n - 1] or p[n - 1] == '.':
                    dp[i][j] = dp[i][j - 2] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 2]
            elif s[m] == p[n] or p[n] == '.':
                dp[i][j] = dp[i - 1][j - 1]
    return dp[-1][-1]
    '''
    # 当p走到最后，s走完为True ，没走完为False
    if not p: return not s 
    # 判断当前第一个字符
    same = True if s and p[0] in {'.', s[0]} else False
    # 有星号匹配第三位，不匹配p无法前进
    # 匹配第一位
    # 无星号，匹配同步前进
    return len(p) >= 2 and p[1] == '*' and  (self. isMatch(s,p[2:]) or same and self.isMatch(s[1:],p)) or same and self.isMatch(s[1:],p[1:])  '''

if __name__ == '__main__':
    s = "aa"
    p = "a*"
    print(isMatch(s, p))
    s = "mississippi"
    p = "mis*is*p*."
    print(isMatch(s, p))
    s = "aab"
    p = "c*a*b"
    print(isMatch(s,p))