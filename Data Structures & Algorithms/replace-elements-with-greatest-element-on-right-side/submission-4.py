class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_sum= -1
        for i in range(len(arr) - 1, -1 , -1):
            new_max = max(right_sum, arr[i])
            arr[i] = right_sum
            right_sum = new_max
        return arr
