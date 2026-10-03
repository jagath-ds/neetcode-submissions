class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = ""
        max_l = 0
        for i in s:
            if i in seen:
                seen = seen[seen.index(i)+1:]
            seen += i
            max_l = max(max_l,len(seen))
        return max_l


