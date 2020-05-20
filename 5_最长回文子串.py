class Solution:
    """最长回文子串"""

    def longestPalindrome(self, s: str) -> str:
        '''lens = len(s)
        if lens <= 1: return s
        reversed_s = ''.join([c for c in s[lens - 1::-1]])
        max = ''
        for i in range(lens):
            for j in range(lens-1,i,-1):
                if s[i] == s[j] and j-i+1 > len(max) and s[i:j+1] == s[i:j+1][::-1]:
                    max = s[i:j+1]
                    return max
        if len(max) == 0:
            return s[0]'''

        lens = len(s)
        if len(s) <= 1:
            return s
        start = end = 0
        for n in range(lens):
            l = r = n
            while l >= 0 and r < lens and s[l] == s[r]:
                    l -= 1
                    r += 1
            odd_len = r-l-1
            l = n
            r = n+1
            while l >= 0 and r < lens and s[l] == s[r]:
                    l -= 1
                    r += 1
            even_len = r-l-1
            more_len = odd_len if even_len < odd_len else even_len
            if more_len > end - start+1:
                start = n - (more_len-1)//2
                end = n + more_len//2

        return s[start:end+1]


if __name__ == '__main__':
    str = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    s = Solution()
    ll = s.longestPalindrome(str)
    print(ll)
    ll = s.longestPalindrome("babadab")
    print(ll)
    ll = s.longestPalindrome("jdkfjllevel")
    print(ll)
    ll = s.longestPalindrome("cd")
    print(ll)
    ll = s.longestPalindrome("a")
    print(ll)