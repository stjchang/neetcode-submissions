class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Read each string, if it has unique characters compared to the last string, add it to the list. If not, don't add.

        ans = []
        occ = []

        for n in strs:
            if sorted(n) not in occ:
                ans.append([n])
                occ.append(sorted(n))
            else: 
                for x in ans:
                    if sorted(x[0]) == sorted(n):
                        x.append(n)
                        break
        return ans



