class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n * 2
        print(ans)
        for i in range(len(nums)):
            ans[i+n],ans[i] = nums[i],nums[i]
            
        return ans
