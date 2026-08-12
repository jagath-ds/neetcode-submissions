class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        value = []
        for i in nums:
            if i in value:
                return True
            else:
                value.append(i)
        return False