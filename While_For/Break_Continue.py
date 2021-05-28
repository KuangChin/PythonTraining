##Break
# n=1
# while n<5:
#     if n==3:
#         break
#     else:
#         print(n)
#     n+=1
# print(n)

##Continue
# n=0
# for x in [0,1,2,3]:
#     if x%3 == 0:
#         continue #跳過後方的程式，直接run下一個迴圈
#     print(x)
#     n+=1
# print("Final: ",n)

# n=0
# while n<5:
#     print(n)
#     n+=1
# else:
#     print(n)

# for s in "Hello":
#     print(s)
# else:
#     print(s)

# sum=0
# for n in range(11):
#     sum+=n
# else:
#     print(sum)

### Example

x = int(input("Please input a value:"))
# if type(x ** 0.5) == int:
#     print("整數平方根為:", x ** 0.5)
# elif type(x ** 0.5) != 0:
#     print("沒有整數平方根")
# else:
#     print("WTF are you input!!!")

for i in range(0, x):
    if i * i == x:
        print("整數平方根:", i)
        break
else:
    print("沒有整數平方根")
