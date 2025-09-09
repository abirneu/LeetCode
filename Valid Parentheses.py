class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in "({[":
                stack.append(char)   # push opening brackets
            else:
                if not stack:        # if stack is empty but found a closing
                    return False
                top = stack.pop()
                if (char == ')' and top != '(') or \
                   (char == '}' and top != '{') or \
                   (char == ']' and top != '['):
                    return False     # mismatch case

        return not stack   # valid only if stack is empty at the end


# Example usage with user input
if __name__ == "__main__":
    user_input = input()
    sol = Solution()
    result = sol.isValid(user_input)
    print(result)
