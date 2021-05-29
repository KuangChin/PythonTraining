# from numpy import iinfo, int32
# class Solution:
#     def myAtoi(self, str: str) -> int:
#         s = str.strip() # shadowing python's internal str, excellent work guys
#         if not s: return 0
#         info = iinfo(int32)
#         built_string = ""
#         for k, i in enumerate(s):
#             if k == 0 and i != '-' and i != '+' and not i.isnumeric(): return 0
#             if k > 0:
#                 if not i.isnumeric() and (built_string == '-' or built_string == '+'): return 0
#                 if not i.isnumeric(): 
#                     break
#             built_string += i
#         multiplier = 1
#         if built_string[0] == '-': 
#             multiplier = -1
#             built_string = built_string[1:]
#         elif built_string[0] == '+':  
#             print(built_string)
#             built_string = built_string[1:]
#         if not built_string: return 0
#         final = int(built_string) * multiplier
#         if final < info.min: return info.min
#         if final > info.max: return info.max
#         return final

# S = Solution()
# print(S.myAtoi("-5-"))

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.read(s)
    def read(self, s):
        s = s.strip()
        res = ''
        m = 1
        if s == "":
            return 0
        else:
            for i in range(len(s)):
                if i == 0:
                    if not s[i].isnumeric() and s[i] != '-' and s[i] != '+':
                        return 0
                if i > 0 :
                    if not s[i].isnumeric() and (res == '-' or res == '+') :
                        return 0
                    if not s[i].isnumeric():
                        break
                res += s[i]
            if res[0] == '+':
                m = 1
                res = res[1:]
            elif res[0] == '-':
                m = -1
                res = res[1:]
            if not res: 
                return 0
            res = int(res) * m
            
            if res < -2**(31):
                
                return -2**(31)
            
            elif res > 2**(31) or res == 2**(31):
                
                return (2**(31)-1)
            else:
                return res

S = Solution()
print(S.myAtoi("-a5"))
