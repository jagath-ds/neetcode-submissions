class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left=0
        window = Counter()
        b = Counter(s1)
        for right in range(len(s2)):
            window[s2[right]] +=1
            if right-left+1 > len(s1):
                window[s2[left]] -=1
                left+=1
            if window == b:
                return True
        return False
