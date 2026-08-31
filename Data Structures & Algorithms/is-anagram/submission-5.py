class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
             s=list(s)
             t=list(t)
             for i in s:
                 if i in t:
                    t.remove(i)
                    pass
                 else:
                      return False
        return True