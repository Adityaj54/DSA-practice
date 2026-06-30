class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_sum = 0
        for i in range(len(arr)):
            if i == len(arr) - 1:
                arr[i] = -1
            else:
                curr_sum = max(arr[i+1:])
                arr[i] = curr_sum
        return arr
