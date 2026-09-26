class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        uniqueSet = sorted(set(nums))

        longest = 1
        currLongest = 1
        lastElement = uniqueSet[0]
        for i,element in enumerate(uniqueSet):
            if(lastElement == element - 1):
                currLongest += 1
                if currLongest > longest:
                    longest = currLongest
            else:
                currLongest = 1
            lastElement = element
        
        return longest