class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        # for example: xxyyxyxyxx and xyyxyxxxyx
        # 1. remove indexes with same chars: we got xyxyyx and yxyxxy
        # 2. get the count of (x and y) and (y and x)
        x_y, y_x = 0, 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                if c1 == 'x':
                    x_y += 1
                else:
                    y_x += 1
        # 3. if sum of both counts is odd then return -1
        if (x_y + y_x) % 2 == 1: # they must be both even or both odd
            return -1
        # 4. for (xx and yy) and (yy and xx) case:
        # Each 2 count of "x_y" needs just 1 swap. So add half of "x_y" count to the result
        # Each 2 count of "y_x" needs just 1 swap. So add half of "y_x" count to the result
        res = x_y // 2
        res += y_x // 2
        # 5. if we still have 1 count of "x_y" and 1 count of "y_x" then they need 2 swaps so add 2 in result.
        # (xy and yx) needs 2 swaps
        if x_y % 2 == 1:
            res += 2

        return res