# Build-in module
import sys
from ModuleTest.CustomMod import distance # [A] path
# from .CustomMod import distance # [R] path
# print(sys.path)

# # Import module
# from ModuleTest.CustomMod import distance
# print(sys.platform)
# print(sys.maxsize)

# import sys as s
# print(s.platform)
# print(s.maxsize)

# # Import module'
print(distance(1,1,5,5))