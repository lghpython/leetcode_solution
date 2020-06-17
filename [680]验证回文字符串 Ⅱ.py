# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。 
# 
#  示例 1: 
# 
#  
# 输入: "aba"
# 输出: True
#  
# 
#  示例 2: 
# 
#  
# 输入: "abca"
# 输出: True
# 解释: 你可以删除c字符。
#  
# 
#  注意: 
# 
#  
#  字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。 
#  
#  Related Topics 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validPalindrome(self, s: str) -> bool:
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
# leetcode submit region end(Prohibit modification and deletion)
