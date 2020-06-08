import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i=0
       	while True:
           num=math.pow(2,i)
           if n==num:
               return True
           if num>n:
               return False
           i+=1
        
       
