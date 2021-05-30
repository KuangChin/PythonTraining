# class Solution:
#     def validSquare(self, p1=[int], p2=[int], p3=[int], p4=[int]) -> bool:

#         def get_distance(p1, p2):
#             d_x = (p2[0] - p1[0])**2
#             d_y = (p2[1] - p1[1])**2
#             return d_x + d_y
#         def sort(list):
#             for i, j in enumerate(list):
#                 min = j
#                 min_pos = i
#                 for k, l in enumerate(list[i+1:]):
#                     if l < min:
#                         min = l
#                         min_pos = k+(i+1)
#                 list[i] = min
#                 list[min_pos] = j
#             return list
                    
#         distances = []
#         points = [p1, p2, p3, p4]
#         for i, j in enumerate(points):
#             for k in points[i+1:]:
#                 print(j, k)
#                 distances.append(get_distance(j, k))
#         sort_distance = sort(distances)
#         if sort_distance[0] == sort_distance[1] and sort_distance[1] == sort_distance[2] and sort_distance[2] == sort_distance[3] and sort_distance[4] == sort_distance[5]:
#             return True
#         else:
#             return False

class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        points = [p1, p2, p3, p4]
        return len({(a[0]-b[0])**2 + (a[1]-b[1])**2 for a in points for b in points}) == 3 and \
               len(set(map(tuple, points))) == 4

# S = Solution()
# print(S.validSquare(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]))
p1 = [0,0] 
p2 = [1,1] 
p3 = [1,0]
p4 = [1,1]
points = [p1, p2, p3, p4]
print(set(map(tuple, points)))