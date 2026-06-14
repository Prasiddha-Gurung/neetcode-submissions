class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

            count_dict = {}

            result = []

            for i in nums:
                if i in count_dict:
                    count_dict[i] += 1
                else:
                    count_dict[i] = 1
            sorted_dict = dict(sorted(count_dict.items(), key=lambda item: item[1], reverse=True))
            for i in sorted_dict:
                if len(result) < k:
                    result.append(i)
            
            return result