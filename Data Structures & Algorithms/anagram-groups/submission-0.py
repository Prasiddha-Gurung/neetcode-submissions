class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

            dict_list = {}

            for n in strs:
                key = tuple(sorted(n))
                if key in dict_list:
                    dict_list[key].append(n)
                else:
                    dict_list[key] = [n]

            return list(dict_list.values())
        