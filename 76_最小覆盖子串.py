def check(ssum, tsum):
    for i in tsum:
        if ssum[i]< tsum[i]:
            return False
        # print(i)
    return True


def minWindow( s: str, t: str) -> str:
    ins =[]
    need = []
    for i, c in enumerate(s):
        if c in t:
            ins.append(i)
            need.append(c)
    tsum = {}
    for k in t: tsum[k] = 0
    ssum = dict(tsum)
    for k in t: tsum[k]+= 1
    left = 0
    min = len(s)
    ans = ''
    for i,n in enumerate(need):

        ssum[n]+=1
        while check(ssum,tsum):
            if ins[i] - ins[left] < min:
                min = ins[i]- ins[left]
                ans = s[ins[left]:ins[i]+1]
            ssum[need[left]] -= 1
            left += 1
    # print(ans+'------')
    return ans




if __name__ == '__main__':
    S = "ADOBECODEBANC"
    T = "ABC"
    result = minWindow(S,T)
    print(result)