class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max=0

        if len(s)==0:
            return 0
        elif len(s)==1:
            return 1


        for i in range(len(s)-1):
            j=i+1
            arr=[]
            arr.append(s[i])
            while j<len(s) and s[j] not in arr:
                arr.append(s[j])
                j+=1
            print(arr)
            if len(arr)>max:
                max=len(arr)
            
        return max