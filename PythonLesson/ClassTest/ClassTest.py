# 類別與類別屬性

# class IO:
#     def __init__(self):
#         print("init class IO")
#         self.supportedSrcs = ["console", "file"]
#     def read(src):
#         print("Read from", src)
#     def change(self):
#         self.supportedSrcs[0] = "SSH"
#         return self.supportedSrcs
# io = IO()
# print(io.supportedSrcs)
# print(io.change())

#類別與實體物件、實體屬性

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def diff(self):
#         d = self.y - self.x
#         print(d)

# p = Point(3, 5)
# print(p.x, p.y)
# p.diff()

# class Peugeot308:   #Class
#     def __init__(self, color, size, torque, price): #Constructor
#         self.drive = "Owned Row, 自手排"    #Attribute
#         self.refuel = "Diseal Oil, 柴油"
#         self.color = color
#         self.size = size
#         self.torque = torque
#         self.price = price
#     def drive_method(self): #Method, self表示實體物件本身
#         return(self.drive)
#     def refuel_type(self):
#         return(self.refuel)
# print("######### KuangChin's Car #########")
# My_car = Peugeot308(color= "dark gray", size= "1.6L", torque= "28kg-m", price= "108w" ) #Object
# print("Color: ", My_car.color,
# "\nSize: ", My_car.size, 
# "\nTorque: ", My_car.torque, 
# "\nPrice: ", My_car.price)
# print("Drive Method", My_car.drive_method())
# print("Refueling", My_car.refuel_type())

# print("######### ChongYuan's Car #########")
# ChongYuan_car = Peugeot308(color= "white", size= "2.0", torque="26kg-m", price="110w" )
# print("Color: ", ChongYuan_car.color,
# "\nSize: ", ChongYuan_car.size, 
# "\nTorque: ", ChongYuan_car.torque, 
# "\nPrice: ", ChongYuan_car.price)
# print("Drive Method", ChongYuan_car.drive_method())
# print("Refueling", ChongYuan_car.refuel_type())


# class File:
#     def __init__(self, name):
#         self.name = name
#         self.file = None    #因尚未開啟，所以file為空的
#     def open(self):
#         self.file = open(self.name, mode="r", encoding="utf-8")
#     def read(self):
#         return self.file.read()
#     def close(self):
#         self.file.close()
# f = File("Test.txt")
# f.open()
# print(f.read())
# f.close()

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.read(s)
    def read(self, s):
        res = ''
        num_neg = 0
        num_type = 0
        if s == "":
                return 0
        else:
            for i in range(len(s)):
                if s[i] == ' ':
                    pass
                elif s[i] == '-':
                    num_neg += 1
                    num_type += 1
                elif s[i] == '+':
                    num_type += 1
                elif s[i] == '.':
                    if len(res) > 0:
                        break
                    else:
                        return 0
                elif ord(s[i]) > 65 or s[i] == None:
                    if len(res) > 0:
                        break
                    else:
                        return 0
                else:
                    res+=s[i]
            if num_type > 1:
                return 0
            elif num_neg % 2 == 0:
                pass
            else:
                res = int(res) * -1
            print(res)
        # if float(res) < -2**(31):
        #     return -2**(31)
        # elif float(res) > 2**(31):
        #     return 2**(31)
        # else:
        #     return int(res)
# print(int('3.14159'))
print("")
S = Solution()
print(S.myAtoi(""))

# x = "words and 987"

# for i in range(len(x)):
#     print(ord(x[i]))

