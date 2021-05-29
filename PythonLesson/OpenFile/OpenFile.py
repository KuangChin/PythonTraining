# Open - Close
# f = open("./File.txt", mode='r')
# print(f.read())
# f.close
# f1 = open("./File.txt", mode='w')
# f1.write("QQQ")
# f1.close

# With Open (Better)
with open("./File.txt", mode='w') as f:
    f.write("CCC")
with open("./File.txt", mode='r') as f:
    print(f.read())

with open("./File.txt", mode='r') as f:
    for line in f:
        print(line)

## JSON
# import json

# with open("./Config.json", mode="r") as f:
#     data = json.load(f)

# print("name: ", data["name"])
# print("version: ", data["version"])
# data["name"] = "Your Name"

# with open("./Config.json", mode="w") as f:
#     json.dump(data,f)

# print("name: ", data["name"])
# print("version: ", data["version"])