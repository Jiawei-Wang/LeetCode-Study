# two hashmaps:
# horizontal: key = x, value = another hashamp: key: y, value: duplicate number
# for example: horizontal[1] = {2:3, 4:5}: there are 3 dots on [1,2], 5 dots on [1,4]
# vertical: key = y, value = set of x
# for example: vertical[1] = (2,3): there exist dots on [2,1] and [3,2] with unknown duplicates
class DetectSquares:

    def __init__(self):
        self.horizontal = dict()
        self.vertical = dict()

    def add(self, point: List[int]) -> None:
        x = point[0]
        y = point[1]

        # put y and count in horizontal[x]
        if x not in self.horizontal:
            self.horizontal[x] = dict()
            if y not in self.horizontal[x]:
                self.horizontal[x][y] = 0
            self.horizontal[x][y] += 1
        else:
            if y not in self.horizontal[x]:
                self.horizontal[x][y] = 0
            self.horizontal[x][y] += 1

        # put x in vertical[y]
        if y not in self.vertical:
            self.vertical[y] = set() 
        self.vertical[y].add(x)

    def count(self, point: List[int]) -> int:
        target_x = point[0]
        target_y = point[1]

        # first there must be at least one dot on same vertical line and at least one dot on same horizontal line
        if target_x not in self.horizontal or target_y not in self.vertical:
            return 0
        
        possible_y = self.horizontal[target_x] # possible_y is a hashmap: key = y, value = count
        possible_x = self.vertical[target_y] # possible_x is a set: x
        count = 0
        for x in possible_x: # for every dot on same vertical line
            for y in possible_y.keys(): # for every dot on same horizontal line
                if abs(target_x - x) == abs(target_y - y) != 0: # 1.only SQUARES, 2.must have positive edge length 
                    if y in self.vertical and x in self.vertical[y]: # if third dot exists
                        count += self.horizontal[x][target_y] * self.horizontal[target_x][y] * self.horizontal[x][y] # multiply all duplicates
        return count

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)