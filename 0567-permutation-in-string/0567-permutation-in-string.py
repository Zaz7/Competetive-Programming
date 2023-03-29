class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        left = 0
        freq1 = Counter(s1)
        window_count = Counter(s2[:n1])
        
        if window_count == freq1:
            return True
        
        for right in range (n1,n2):
            window_count[s2[left]] -= 1
            if window_count[s2[left]] == 0 :
                del window_count[s2[left]]
                
            if s2[right] in window_count:
                window_count[s2[right]] += 1
            else:
                window_count[s2[right]] = 1
            
            if freq1 == window_count:
                return True
            
            left += 1
        
        return False
        
                
        
        