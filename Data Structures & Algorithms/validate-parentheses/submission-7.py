class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {"(":")","[":"]","{":"}"}
        ptr =0
        seen = []
        while(ptr<len(s)):
            if s[ptr] in dict1:
                seen.append(s[ptr])
            if(s[ptr] in dict1.values()):
                if not seen:
                    return False
                if(s[ptr]==dict1[seen[-1]]):
                    seen.pop()
                else:
                    return False
            ptr+=1
        return len(seen) == 0