class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {"(":")","[":"]","{":"}"}
        ptr =0
        s_ptr = 0
        seen = []
        while(ptr<len(s)):
            if s[ptr] in dict1:
                seen.append(s[ptr])
                s_ptr +=1
            if(s[ptr] in dict1.values()):
                if not seen:
                    return False
                if(s[ptr]==dict1[seen[s_ptr-1]]):
                    seen.pop()
                    s_ptr-=1
                else:
                    return False
            ptr+=1
        return len(seen) == 0