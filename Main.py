# Absoluted path import method
from ModuleTest.CustomMod import distance
import ModuleTest.CustomMod
# print(distance(1,1,5,5))
print(ModuleTest.CustomMod.distance(1,1,5,5))

# Sys path import method
import sys
sys.path.append("ModuleTest")
# print(sys.path)
import CustomMod
print(CustomMod.distance(1,1,5,5))
