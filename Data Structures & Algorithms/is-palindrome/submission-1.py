import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_cleaned= re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        i,j=0,len(s_cleaned)-1
        print(s_cleaned)
        while i < j:
            if s_cleaned[i]==s_cleaned[j]:
             i=i+1 
             j=j-1
             pass
            else :
                return False 
        return True