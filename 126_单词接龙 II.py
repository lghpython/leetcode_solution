class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        ans = []
        lb = len(beginWord)
        print("22")
        if endWord not in wordList: return ans
        print("33")
        while beginWord != endWord:
            for w in wordList:
                ss = set(beginWord) | set(w)
                # 判断只有一个不同的单词
                count = -1
                if len(ss) <= 2 * lb - 2:
                    count += 1
                    ans.append(w)
            beginWord = ans[0]
            wordList.remove(ans[0])
            print(ans)
            ans = []




if __name__ == '__main__':
    b = 'hit'
    e = 'cog'
    wl = ["hot", "dot", "dog", "lot", "log", "cog"]
    Solution().findLadders(b, e, wl)
