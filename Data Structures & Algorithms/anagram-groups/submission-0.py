class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            new_s = "".join(sorted(s))
            if new_s not in anagrams:
                anagrams[new_s] = []
            anagrams[new_s].append(s)

        result = []
        for a in anagrams.keys():
            result.append(anagrams[a])
        return result