class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        new_muns = set(nums)

        return len(nums) != len(new_muns)
        