# brute force: test all combinations
# abc + def: make two cuts, one for abc and one for def
# left cut can be placed on left of a, b, or c
# right cut can be placed on right of d, e, or f
class Solution:
    def minimizeResult(self, expression: str) -> str:
        strings = expression.split("+")
        left_string = strings[0]
        right_string = strings[1]
        left_combinations = [("1", left_string)] + [(left_string[:i], left_string[i:]) for i in range(1, len(left_string))]
        right_combinations = [(right_string[:i], right_string[i:]) for i in range(1, len(right_string))] + [(right_string, "1")]
        # for example: 123 + 456
        # left_combinations = [('1', '123'), ('1', '23'), ('12', '3')]
        # right_combinations = [('4', '56'), ('45', '6'), ('456', '1')]

        target = float("inf")
        answer = "(" + expression + ")"
        for l in left_combinations:
            for r in right_combinations:
                if target > int(l[0])*(int(l[1])+int(r[0]))*int(r[1]):
                    target = int(l[0])*(int(l[1])+int(r[0]))*int(r[1])
                    if l[1] == left_string:
                        if r[0] == right_string:
                            answer = "(" + expression + ")"
                        else:
                            answer = "(" + l[1] + "+" + r[0] + ")" + r[1]
                    else:
                        if r[0] == right_string:
                            answer = l[0] + "(" + l[1] + "+" + r[0] + ")"
                        else:
                            answer = l[0] + "(" + l[1] + "+" + r[0] + ")" + r[1]
        return answer


# clean up
class Solution:
    def minimizeResult(self, expression: str) -> str:
        left, right = expression.split("+")
        min_value = float("inf")
        result_expr = ""

        for i in range(len(left)):
            for j in range(1, len(right) + 1):
                a, b = left[:i], left[i:]
                c, d = right[:j], right[j:]

                left_mult = int(a) if a else 1
                right_mult = int(d) if d else 1
                middle_sum = int(b) + int(c)
                value = left_mult * middle_sum * right_mult

                if value < min_value:
                    min_value = value
                    result_expr = f"{a}({b}+{c}){d}"

        return result_expr