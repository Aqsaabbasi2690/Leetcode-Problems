class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        number = sum(nums[:k])
        maxsum = number

        for i in range(k, len(nums)):
            number = number - nums[i - k] + nums[i]
            maxsum = max(maxsum, number)

        return maxsum / k
