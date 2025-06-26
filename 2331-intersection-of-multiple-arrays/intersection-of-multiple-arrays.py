class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        number = set(nums[0])
        for i  in range(1, len(nums)):
         number = number.intersection(nums[i])
        return sorted(number)
        