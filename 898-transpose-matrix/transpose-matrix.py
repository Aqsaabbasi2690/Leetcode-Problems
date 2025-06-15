class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
      zipped = zip(*matrix)
      return (list(zipped))