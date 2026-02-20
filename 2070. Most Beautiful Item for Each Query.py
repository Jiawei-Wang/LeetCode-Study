class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # sort items by price
        items = sorted(items + [[0, 0]])
        """
        for example items = [[1,2],[3,2],[2,4],[5,6],[3,5]]
        it becomes [[0,0], [1,2], [2,4], [3,2], [3,5], [5,6]]
        """

        # find maximum beauty up to each price
        for i in range(1, len(items)):
            items[i][1] = max(items[i-1][1], items[i][1])
        """
        [[0, 0], [1, 2], [2, 4], [3, 4], [3, 5], [5, 6]]
        explain: [3, 4] means when price = 3, maximum beauty is 4
        """

        # find most expensive item each query can afford
        # (the item already has the maximum beauty) 
        answer = []
        for q in queries:
            index = bisect.bisect_right(items, [q + 1]) - 1
            """
            1. since each element is an array in items, we also need to use array for query
            2. [q+1] is of length 1 so during query, only first element (price) of each element is used
                if q + 1 > price: target is larger
                if q + 1 <= price: target is smaller or equal
            since q + 1 > q, query will stop at first item where price > q
            then with -1, we land on the most expensive item with price <= q
            3. why not use index = bisect.bisect_right(items, [q]):
                because in python, when comparing arrays, length 1 array is smaller than length 2 array
                [3] < [3, -1] < [3, 0] < [3, 3]
            """
            beauty = items[index][1]
            answer.append(beauty)
        return answer
        # one liner version: 
        # return [items[bisect.bisect(items, [q + 1]) - 1][1] for q in queries]

