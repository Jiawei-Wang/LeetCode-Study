"""
For a product, the stock is represented by a list of a number of items for each supplier. As items are purchased, 
the suppiler raises the price by 1 per item purchased. Assume profit on any single item is the same as the number of items the supplier has left.
For example if a supplier has 4 items then profit on the first item sold is 4, then 3, then 2 and 1.

Given a list where each value in the list is the number of the item at a given supplier and also given the number of items to be ordered,
write an algorithm to find the highest profit that can be generated for the given product.

Input: 
    numSuppliers, an integer representing the number of suppliers
    inventory, a list of long integers representing the value of the item at a given supplier
    order, a long integer representing the number of items to be ordered
Output:
    return a long integer representing the highest profit that can be generated for the given product
Constraints:
    1 <= numSuppliers <= 10^5
    1 <= inventory[i] <= 10^5
    0 <= i < numSuppliers
    1 <= order <= sum of inventory
Example:
    Input:
        numSuppliers = 2
        inventory = [3, 5]
        order = 6
    Output:
        19
"""

# hashmap
class Solution:
    def highestProfit(self, numSuppliers, inventory, order):
        # list to dictionary
        profit = dict()
        for price in inventory:
            profit[price] = profit.get(price, 0) + 1
        
        curr_max = max(profit.items(), key = lambda x: x[0])[0]

        ret = 0
        while order > 0:
            maxi = min(order, profit[curr_max])
            ret += curr_max * maxi
            order -= maxi
            profit[curr_max] -= maxi
            profit[curr_max - 1] = profit.get(curr_max - 1, 0) + maxi
            if profit[curr_max] == 0:
                del profit[curr_max]
                curr_max -= 1
        return ret


# heapq
import heapq

class Solution2:
    def highestProfit(self, numSuppliers, inventory, order):
        # list to heap
        max_heap = []
        for product in inventory:
            heapq.heappush(max_heap, -product)
        
        profit = 0
        while max_heap and order > 0:
            product = heapq.heappop(max_heap)
            product_profit = -product
            profit += product_profit
            if product_profit > 0:
                product_profit -= 1
                heapq.heappush(max_heap, -product_profit)
            order -= 1
    
        return profit


if __name__ == "__main__":
    # should return 19
    case1 = Solution()
    print(case1.highestProfit(2, [3, 5], 6))

    # should return 42
    case2 = Solution()
    print(case2.highestProfit(3, [7, 5, 3], 10))

    # should return 19
    case3 = Solution2()
    print(case3.highestProfit(2, [3, 5], 6))

    # should return 42
    case4 = Solution2()
    print(case4.highestProfit(3, [7, 5, 3], 10))

