class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Special case: only one row, or string shorter than numRows
        if numRows == 1 or numRows >= len(s):
            return s

        # Create a list for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False

        # Build the zigzag pattern
        for char in s:
            rows[current_row] += char

            # Reverse direction at top or bottom
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            # Move up or down
            current_row += 1 if going_down else -1

        # Combine rows
        return ''.join(rows)
