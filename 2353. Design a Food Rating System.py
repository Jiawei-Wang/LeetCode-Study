class FoodRatings:
    
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # use 3 hashmaps
        self.food_cuisine = {}   # food -> cuisine
        self.food_rating = {}    # food -> rating
        self.cuisine_heaps = {}  # cuisine -> heap of (-rating, name)

        # build these hashmaps
        for f, c, r in zip(foods, cuisines, ratings):
            self.food_cuisine[f] = c
            self.food_rating[f] = r

            if c not in self.cuisine_heaps:
                self.cuisine_heaps[c] = []
            heapq.heappush(self.cuisine_heaps[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_cuisine[food]
        oldRating = self.food_rating[food]

        # Update stored rating
        self.food_rating[food] = newRating

        # Push new tuple into heap
        heapq.heappush(self.cuisine_heaps[cuisine], (-newRating, food))

        # Lazy deletion (we don't remove old entries — too slow in a heap)
        # They will be ignored when popped later.

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_heaps[cuisine]

        # Pop outdated heap entries
        while True:
            rating, food = heap[0]
            if -rating == self.food_rating[food]:
                return food   # valid top element
            heapq.heappop(heap)    # remove stale entry


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)