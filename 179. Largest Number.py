class Solution:
    def largestNumber(self, nums: List[int]) -> str:

      ans = [str(i) for i in nums]     
           
      ans.sort(key= cmp_to_key(lambda x,y:1 if x+y<y+x else -1))
              
      return str(int("".join(ans)))