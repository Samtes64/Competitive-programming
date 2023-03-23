class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        ans=[int(i) for i in nums]
        ans.sort()

        return str(ans[len(nums)-k])