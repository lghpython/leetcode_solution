def findTheLongestSubstring(self, s: str) -> int:
    t, l, r, v = 0, {0: -1}, {0: -1}, {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
    # for i, c in enumerate(s):
    for i in range(len(s)):
        if s[i] in v:
            t ^= v[s[i]]
        # 保存右边界，包含非元音字母下标
        r[t] = i
        # 保存左边界,第一个出现的元音下标
        if t not in l:
            l[t] = i
    # print(r,l)
    return max(map(lambda x, y: x - y, r.values(), l.values()))
    '''
    ans, status = 0, 0
    pos = [0] + [-1] * 31
    vo = 'aeiou'
    for i in range(len(s)):
        if s[i] in vo :
            status ^= 1 << vo.index(s[i])
        if pos[status] == -1:
            pos[status] = i + 1
        else:
            ans = max(ans, i + 1 - pos[status])
    return ans
    '''