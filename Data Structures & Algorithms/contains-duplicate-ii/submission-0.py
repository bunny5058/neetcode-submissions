class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap={}
        for R in range(len(nums)):
            print(R)
            if nums[R] in hashmap and R-hashmap[nums[R]]<=k:
                return True
            hashmap[nums[R]]=R
        return False