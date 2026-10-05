class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left=0
        max_f =0
        res =0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right],0)
            max_f = max(count.values())
            if(((right-left+1)-max_f)<=k ):
                res = max(res,(right-left+1))
            else:
                count[s[left]] -=1
                left+=1
        
        return res