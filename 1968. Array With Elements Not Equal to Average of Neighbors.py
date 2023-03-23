class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans=[]

        l=0
        r=len(nums)-1
        while len(ans)!=len(nums):
            ans.append(nums[l])
            l+=1

            if r>=l:
                ans.append(nums[r])
                r-=1

        return ans