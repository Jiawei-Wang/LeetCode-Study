"""
thinking process:
imagine Attack and Defense being two two axis in a 2d plane

example:
a = [2 , 10]
b = [2 , 5 ]
c = [4 , 1 ]
d = [6 , 9 ]
e = [8 , 10]
f = [8 , 7 ]
g = [10, 7 ]
h = [12, 3 ]

Defense
|
|
|------a---------------e
|               d      |
|                      f-------g
|      b                       |
|                              |------h
|           c                         |
|_____________________________________|____  Attack

then for player g, any player that is strictly on the bottom left side of g is weaker
so it's a rectangular shadow with f on the edge and b, c inside
so b and c are weaker
and in this example the overall shadow will be 3 overlapping parts
coming from shadow of e, shadow of g, and shadow of h


an easy way to check if future players are inside the shadow is to 
first make sure future players are on the left side then we only to care about bottom side
to do this we need to sort players by attack, higher goes first
then sort by defense, lower goes first
so the order of traversal would be: h, g, f, e, d, c, b, a
future player is guaranteed to have <= current attack (on the left side)
if it has higher defense (on the top side), increase the shadow
otherwise, it is weaker
"""

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # Sort by attack DESC, defense ASC (for ties on attack)
        properties.sort(key=lambda x: (-x[0], x[1]))
        
        max_def = 0
        weak = 0
        
        for _, defense in properties:
            if defense < max_def: # it is in bottomleft shadow
                weak += 1
            else:
                max_def = defense # it is too high for the shadow, expand the shadow
        
        return weak



