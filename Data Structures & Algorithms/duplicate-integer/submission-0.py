class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         digit =[]
         for num in nums:
            if num in digit:
                return True
            digit.append(num)
         return False
                