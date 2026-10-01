class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        same = {}

        for s in strs:
            key = ''.join(sorted(s))

            if key not in same:
                same[key] = []

            same[key].append(s)

        return list(same.values())