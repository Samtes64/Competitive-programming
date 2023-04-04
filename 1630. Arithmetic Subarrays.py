class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        boolarr=[]
        for i in range(len(l)):
            arr=[]
            for j in range (l[i],r[i]+1):
                arr.append(nums[j])
            arr.sort()
            print(arr)
            boolval=True
            dif=arr[1]-arr[0]
            
            for z in range (len(arr)-1):
                
                if arr[z+1]-arr[z]!=dif:
                    boolval=False
                
            boolarr.append(boolval)

        return boolarr