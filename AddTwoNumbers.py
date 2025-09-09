class Solution:
    def addTwoNumbers(self, l1, l2):
        # reverse for easier digit-wise addition (like manual math)
        l1 = l1[::-1]
        l2 = l2[::-1]
        

        n = max(len(l1), len(l2))
        carry = 0
        ans = []

        for i in range(n):
            d1 = l1[i] if i < len(l1) else 0
            d2 = l2[i] if i < len(l2) else 0

            temp = d1 + d2 + carry
            ans.append(temp % 10)  
            carry = temp // 10  

        if carry:
            ans.append(carry)

        
        return ans[::-1]


sol = Solution()

