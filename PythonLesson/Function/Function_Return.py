### Function
# def say(msg):
#     print(msg)
#     #return
#     return "CC"
# print(say("QQ"))

# def say(msg):
#     print(msg)
#     return msg

# print(say("QQ"))


## Mapping variable

# def say(msg1=4, msg2=2):
#     say(msg1/msg2)

# say(2, 4 )
# say(msg2 = 2, msg1 = 4)

## Dynamic parameter - 傳進去的值會以Tuple存放!!
def avg(*msg):
    print(msg)
    sum=0
    for i in msg:
        sum += i
    res = sum/len(msg)
    return res
print(avg(1,2,3,4,5))
print(avg(1,2,3))