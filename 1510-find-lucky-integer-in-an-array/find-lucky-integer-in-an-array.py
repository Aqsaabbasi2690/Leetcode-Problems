class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = []
        for num in set(arr):
            if arr.count(num) == num:
                count.append(num)
        if count:
                return max(count)
        return -1