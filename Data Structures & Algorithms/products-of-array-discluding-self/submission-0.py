class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        hasZeros = False

        hasMultipleZeros = False

        totalNonZeroProduct = 1

        result = []

        for i in nums:
            if i == 0:
                if hasZeros:
                    hasMultipleZeros = True
                hasZeros = True
            else:
                totalNonZeroProduct *= i
        
        for j in nums:
            if hasZeros:
                if hasMultipleZeros:
                    result.append(0)
                elif j == 0:
                    result.append(totalNonZeroProduct)
                else:
                    result.append(0)
            else:
                result.append(int(totalNonZeroProduct/j))
        
        return result
            

        