"""
Solve 1D first:
To determine if two segments on a 1D plane overlap 
specifically having a shared segment rather than just touching
we have to look at the boundaries of Segment A [x1, y1] and Segment B [x2, y2]

First, ensure your coordinates are ordered correctly: 
x must be the start (min) and y must be the end (max). 
If they aren't, you'd swap them so x1 < y1 and x2 < y2.

The Mathematical Requirement: two segments overlap if and only if:
max(x1, x2) < min(y1, y2)

This logic checks the innermost boundaries of the two segments:
max(x1, x2): This is the "latest" start point between the two.
min(y1, y2): This is the "earliest" end point between the two.
If the latest start occurs before the earliest end, there must be a shared interval between them.

Moving on to 2D:
For two rectangles to overlap, 
they must overlap on both axes simultaneously. 
If they only overlap on the X-axis, 
they are just "above or below" each other. 
If they only overlap on the Y-axis, they are "side-by-side."
"""
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # X-axis segment for rec1 is [rec1[0], rec1[2]]
        # X-axis segment for rec2 is [rec2[0], rec2[2]]
        # Check if the overlap on X-axis is positive
        width_overlap = min(rec1[2], rec2[2]) > max(rec1[0], rec2[0])
        
        # Y-axis segment for rec1 is [rec1[1], rec1[3]]
        # Y-axis segment for rec2 is [rec2[1], rec2[3]]
        # Check if the overlap on Y-axis is positive
        height_overlap = min(rec1[3], rec2[3]) > max(rec1[1], rec2[1])
        
        # They only overlap in 2D if they overlap on both 1D axes
        return width_overlap and height_overlap