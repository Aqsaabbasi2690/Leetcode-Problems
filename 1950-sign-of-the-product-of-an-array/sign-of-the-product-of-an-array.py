class Solution:
    def arraySign(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                count = count + 1
        return 1 if count % 2 == 0 else -1

        