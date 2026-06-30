class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        global_sum = 0
        curr_sum = 0
        for num in nums:
            if num == 1:
                curr_sum +=1
                global_sum = max(global_sum, curr_sum)

            else:
                curr_sum = 0
        return global_sum
        