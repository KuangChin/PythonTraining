### Set
# s = {3,4,5}
# print(3 in s, 6 in s, 3 not in s)

### operator of Set
## Intersection (交集)
# s1 = {3,4,5}
# s2 = {4,5,6,7}
# s3 = s1&s2
# print(s3)
## Union (聯集), remove duplicate
# s4 = s1 | s2
# print(s4)
## 差集, Substration 
# s5 = s1 - s2 # 從s1中減掉與s2重複的
# s6 = s2 - s1 # 從s2中減掉與s1重複的
# print(s5, s6)
## Anti-intersection (反交集), 取兩個集合不重疊的部分
# s7 = s1 ^ s2
# print(s7)
## Seperate string to set, remove duplicate and random ordered
# s = set("Hello")
# print("H" in s)

### Dict Key-Value mapping, changable
# dic = {"apple":"蘋果", "bug": "蟲蟲", "int":1}
# print(dic["apple"], type(dic["int"]))

## Changable
# dic["apple"] = "小蘋果"
# print(dic)

## in or not in (only find key not value)
# print("apple" in dic, "蘋果" in dic)

## Removable - remove key and value
# del dic["apple"]
# print(dic)

## Variable for dict
# l = [1,2,3,4]
# dic = {x:x*2 for x in l}
# print(dic)