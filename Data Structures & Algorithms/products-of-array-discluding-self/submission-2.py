class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        length_nums = len(nums)

        suffix = [1] * length_nums

        prefix = [1] * length_nums

        j = length_nums - 1

        prefix_prod = 1
        suff_prod = 1
        for i in range(length_nums):

            prefix[i] = prefix_prod 
            prefix_prod *= nums[i]
            suffix[j] = suff_prod
            suff_prod *= nums[j]   
            j-=1
        
        result = [1] * length_nums

        for i in range(length_nums):
            result[i] = (suffix[i] * prefix[i])
        
        return result

