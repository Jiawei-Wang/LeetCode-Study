class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        length = max(costs) + 1
        counter = [0] * length
        for cost in costs:
            counter[cost] += 1

        answer = 0
        for i in range(length):
            price = i
            number = counter[i]
            if number == 0:
                continue
            can_take = coins // price

            if can_take >= number:
                answer += number
                coins -= number * price
            else:
                answer += can_take
                return answer
            
        return answer