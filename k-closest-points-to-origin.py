class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
  
        dis = []
        new_dis=[]
        for i in points:
            distance = i[0]**2 + i[1]**2
            dis.append((distance,i))
        sort= sorted(dis)
        for j in sort:
            new_dis.append(j[1])

        return new_dis[0:k]
