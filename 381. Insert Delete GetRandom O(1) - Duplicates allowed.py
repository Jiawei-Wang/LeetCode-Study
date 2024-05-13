class RandomizedCollection:
    def __init__(self):
        self.map = {} # key: val, value: a list of indices where val apperars in nums
        self.nums = [] # tuple: (val, index of this specific val in map[val], map[val] is a list)
    
    # for example: if we insert these five: 5, 7, 3, 7, 5 without any removal
    # then map will be:
    # 3: [2]       (3 appeared once in nums, with index = 2 in nums)
    # 7: [1, 3]    (5 appeared twice in nums, first index = 1, second index = 3 in nums)
    # 5: [0, 4]
    # and nums will be: 
    # [(5, 0), (7, 0), (3, 0), (7, 1), (5, 1)] ((5,0): this 5 exists in map, and it is stored on map[5][0])
    # so all three: input, map, nums are connected: 
    # the last input element val will be appended to the end of nums
    # so we store key=val, value=len(nums) (element is not in nums yet) in map
    # then we append tuple (val, len(map[val])-1) (element is already in map) in nums
    def insert(self, val: int) -> bool:
        not_exist = val not in self.map
        
        if not_exist:
            self.map[val] = []

        self.map[val].append(len(self.nums))
        self.nums.append((val, len(self.map[val]) - 1))
        
        return not_exist

    # getRandom is easy, just randomly pick one 
    def getRandom(self) -> int:
        return random.choice(self.nums)[0] # random.choice(list): return a randomly selected element

    # remove is the only time when data structures need to be re-organized
    def remove(self, val: int) -> bool:
        exist = val in self.map

        if exist:
            last = self.nums[-1] # get last input's value and its pos in map
            self.map[last[0]][last[1]] = self.map[val][-1] # change its index in nums to val's index in nums
            self.nums[self.map[val][-1]] = last # change the value of element on this location in nums to last 
            self.nums.pop() # delete last element in nums 
            self.map[val].pop() # delete last pos of val in map
            if not self.map[val]:
                del self.map[val]

        """
        for example: 
        # map:
        # 3: [2]       
        # 7: [1, 3]    
        # 5: [0, 4]
        # nums: 
        # [(5, 0), (7, 0), (3, 0), (7, 1), (5, 1)] 
        and we want to remove one of the two 7s from nums:
        1. get last input by picking last element (5,1) from nums
        2. locate it on map using map[5][1]
        3. its value is 4, meaning it's on nums[4]
        4. change the value to the last 7's value, meaning this 5 now is re-assigned to (7, 1)'s pos in nums
        5. now we have:
           map =
           3: [2]
           7: [1, 3]
           5: [0, 3] <- 4 is changed to 3
           nums is not changed
        6. now we let nums[3] = (5, 1), meaning we finally move this 5 into 7's position in nums
        7. and we still have to clean up 7: we remove last element from nums, and pop last element on map[7]
        """
        return exist

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()