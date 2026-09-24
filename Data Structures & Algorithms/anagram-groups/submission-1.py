class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        pairs = {}

        for i in range(len(strs)):
            sorted_key = "".join(sorted(strs[i]))

            if(sorted_key in pairs):
                pairs[sorted_key].append(strs[i])
            else:
                pairs[sorted_key] = [strs[i]]
        
        answer = []
        for key, value in pairs.items():
            answer.append(value) 
        return answer
        