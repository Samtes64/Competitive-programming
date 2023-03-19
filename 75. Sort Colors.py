class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red=int(nums.count(0))
        white=int(nums.count(1))
        blue=int(nums.count(2))
        nums.clear()
        for i in range (0,red):
            (nums.append(0)) 
        for i in range (0,white):
            (nums.append(1)) 
        for i in range (0,blue):
            (nums.append(2))    

        
       
        """
        Do not return anything, modify nums in-place instead.
        """