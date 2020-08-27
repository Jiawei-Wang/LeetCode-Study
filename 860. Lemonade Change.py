class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # corner case
        if not bills[0] or bills[0] != 5:
            return False

        # 记录所剩零钱数量
        five = 0
        ten = 0

        # 遍历
        for i in bills:
            # 5元直接保留
            if i == 5: five += 1
            # 10元的找零：1个5元
            elif i ==10:
                five -= 1
                ten += 1
            # 20元的找零：先用10元，10元不够时使用5元
            else:
                if ten >= 1:
                    ten -= 1
                    five -= 1
                else:
                    five -= 3
            # 检查所剩零钱是否符合要求
            if five < 0 or ten < 0:
                return False
        return True
