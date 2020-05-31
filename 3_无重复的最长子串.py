def lengthOfLongestSubstring( s: str) -> int:
    ls = len(s)
    if ls <= 1: return ls
    tmp = []
    l, max, count = 0, 0, 0
    for i in range(ls):
        # 当无重复,添加到列表,max加1
        if s[i] not in tmp:
            tmp.append(s[i])
            count += 1
        else:
            # 出现重复删除第一个,直到不重复
            while s[i] in tmp:
                tmp.pop(0)
                l += 1
                count -= 1
            tmp.append(s[i])
            count += 1
        if count > max:
            max = count
    return max


if __name__ == '__main__':
    ll = lengthOfLongestSubstring("bbbbb")
    print(ll)
    ll = lengthOfLongestSubstring("abcabcbb")
    print(ll)
    ll = lengthOfLongestSubstring("fhkjahklf")
    print(ll)