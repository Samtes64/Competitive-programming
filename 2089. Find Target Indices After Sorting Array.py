class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        num=sorted(nums)


        for i in range(0,len(num)):
            if num[i]==target:
                ans.append(i)

        return ans