def validPalindrome(s) -> bool:
    r = s[::-1]
    if s == r:
        return True
    for i in range((len(s) + 1) // 2):
        if s[i] != r[i]:
            # 正序多一个
            if s[i + 1:len(s) - i] == r[i:len(s) - i - 1]:
                s = s[:i] + s[i + 1:]
                r = s[::-1]
                return s == r
            # 反序多一个
            elif s[i:len(s) - i - 1] == r[i + 1:len(s) - i]:
                r = r[:i] + r[i + 1:]
                s = r[::-1]
                return s == r
            else:
                return False

if __name__ == '__main__':
    vp = validPalindrome('abca')
    print(vp)