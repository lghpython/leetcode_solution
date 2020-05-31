class Solution:
    def decodeString(self, s: str) -> str:

        # 栈解法
        stack = []
        digit = ''
        char = ''  # 保存括号内字符
        for c in s:
            # 添加数字和括号到栈里,quo保存括号索引,清空数字
            if c == '[':
                stack.append([digit, char])
                digit, char = '', ''
            # 保存数字
            elif '0' <= c <= '9':
                digit += c
            elif c == ']':
                d, ch = stack.pop()
                char = ch + int(d) * char
            else:
                char += c
        return char

        # 栈解法二
        # stack = []
        # for i, c in enumerate(s):
        #     if c == ']':
        #         cur = ''
        #         while stack:
        #             pre = stack.pop()
        #             if pre == '[': break
        #             cur = pre + cur
        #
        #         num = ''
        #         while stack and stack[-1].isdigit():
        #             num = stack.pop() + num
        #         stack.append(int(num) * cur)
        #     else:
        #         stack.append(c)
        # return ''.join(stack)

        # 正则表达式解法
        # pat = r'(\d+)\[(\w+)\]'
        # m=1
        # while m:
        #     m=re.findall(pat,s)
        #     for num,char in m:
        #         s=s.replace(f'{num}[{char}]',char*int(num))
        # return s
