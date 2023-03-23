class Solution(object):
    
    def merge(self, intervals):
        intervals.sort()
        result=[]
        for i in intervals:
            if result==[] or i[0] > result[-1][1]:
                result.append(i)
            else:
                result[-1][1] = max(result[-1][1], i[1])
        return result