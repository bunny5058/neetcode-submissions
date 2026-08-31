class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        k=0
        j=0
        for i in nums:
            if i==1:
                j=j+1
                k=max(k,j)
            else:
                j=0
        return k
