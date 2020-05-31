def longestCommonPrefix(strs) -> str:
    tmp = strs[0]
    for s in strs:
        pre = min(len(tmp), len(s))
        for i in range(pre):
            if s[i] != tmp[i]:

                break
            tmp = tmp[0:i]
    return tmp

if __name__ == '__main__':
    lc =longestCommonPrefix(["aa","a"])
    print(lc)