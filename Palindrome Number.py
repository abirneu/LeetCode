class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            str_x = str(x)
            rev_str = str_x[::-1]
            rev_x = int(rev_str)
            if rev_x == x:
                return True
            else:
                return False
            
       
        

