class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        L,R=0,1
        curr=""
        leng=1
        while R <  len(arr):

              if arr[R-1]>arr[R] and curr !=">":
                   leng=max(leng,R-L+1)
                   R=R+1
                   curr=">"
              elif arr[R-1]<arr[R] and curr!="<" :
                   leng=max(leng,R-L+1)
                   R=R+1
                   curr="<"
              else:
                   if arr[R]==arr[R-1]:
                         R=R+1
                   else:
                         R=R
                
                   L=R-1
                   curr=""
            
                    
        return leng
