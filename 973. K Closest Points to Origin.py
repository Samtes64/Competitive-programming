class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans=[]


        # maxind=0
        # for i in range(1,len(points)-1):
        #     if (points[i][0] ** 2 + points[i][1] ** 2) > (points[i+1][0] ** 2 + points[i+1][1] ** 2):
        #         maxind=i
        #     elif (points[i][0] ** 2 + points[i][1] ** 2) < (points[i+1][0] ** 2 + points[i+1][1] ** 2):
        #         minind=i
        # points[maxind],points[len(points)-1]=points[len(points)-1],points[maxind]
        
        # for i in range(k):
        #     ans.append(points[i])  




        # time limit exceed
        # for i in range(len(points)):
        #     for j in range(i+1,len(points)):
        #         if (points[i][0] ** 2 + points[i][1] ** 2) > (points[j][0] ** 2 + points[j][1] ** 2):
        #             points[j],points[i]=points[i],points[j]

        # for i in range(k):
        #     ans.append(points[i]) 




        # for i in range(k):
        #     for j in range(i+1,len(points)):
        #         if (points[i][0] ** 2 + points[i][1] ** 2) > (points[i+1][0] ** 2 + points[i+1][1] ** 2):
        #             points[i],points[j]=points[j],points[i]

        # for i in range(k):
        #     ans.append(points[i]) 




        points.sort(key= lambda x: x[0]**2 + x[1]**2)

        for i in range(k):
            ans.append(points[i])         

            

            
            
        return ans