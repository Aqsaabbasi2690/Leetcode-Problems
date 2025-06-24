class Solution:
    def singleNumber(self, nums: List[int]) -> int:
      number = 0
      for i in nums:
        number = number ^ i
      return number