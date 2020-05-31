class Solution:
    def myAtoi(self, str: str) -> int:
        s = str.strip()
        p = '0123456789'
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        neg = False
        pos = False
        num = ''
        for i in s:
            if i == '-' and len(num) ==0:
                if  pos or neg :
                    return 0
                neg = True
                continue
            elif i == '+' and len(num) ==0:
                if  pos or neg :
                    return 0
                pos = True
                continue
            if i in p: num += i
            else: break
        num = int(num) if len(num)!= 0 else 0
        if neg:
            if num > 2**31:
                return  INT_MIN 
            else:
                return -num
        else:
            if num > 2**31-1:
                return INT_MAX 
            else:
                return num
