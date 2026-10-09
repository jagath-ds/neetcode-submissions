class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left=0
        t_count = Counter(t)
        required = len(t_count)
        s_count = Counter()
        formed = 0
        min_len = float("inf")
        start=0
        for right in range(len(s)):
            s_count[s[right]] +=1
            char = s[right]
            if char in t_count and t_count[char] == s_count[char]:
                formed +=1
            while required == formed:
                window = right-left+1
                if(min_len>window):
                    min_len = window
                    start = left
                char = s[left]
                if char in t_count and s_count[char] == t_count[char]:
                    formed-=1
                s_count[s[left]] -=1
                left+=1
        if min_len == float("inf"):
            return ""
        return s[start:start+min_len]

                
            
            




