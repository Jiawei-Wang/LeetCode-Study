# if the area of the large rectangle == sum of all small rectangles
# that means there is no overlapping
# if all small rectangles form a perfect rectangle
# any point on those small rectangles should have either 2 or 4 copies
# except the 4 corner points, they only have 1 copy each
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        """
        Check if the given rectangles exactly cover a rectangular region.

        Approach:
        1. Compute the bounding rectangle (minX, minY, maxX, maxY)
        2. Sum up the areas of all small rectangles
        3. Track the corners using a set:
           - Each corner should appear even times except the four corners of the bounding rectangle
        4. Compare total area of small rectangles with the bounding rectangle's area
        """
        
        # Initialize variables for bounding rectangle
        minX = minY = float('inf')
        maxX = maxY = float('-inf')
        corners = set()
        total_area = 0
        
        for x1, y1, x2, y2 in rectangles:
            # Update bounding rectangle coordinates
            minX = min(minX, x1)
            minY = min(minY, y1)
            maxX = max(maxX, x2)
            maxY = max(maxY, y2)
            
            # Calculate area of this rectangle
            area = (x2 - x1) * (y2 - y1)
            total_area += area
            
            # Add/remove corners from the set
            rect_corners = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
            for corner in rect_corners:
                if corner in corners:
                    corners.remove(corner)
                else:
                    corners.add(corner)
        
        # The set should contain exactly the 4 corners of the bounding rectangle
        expected_corners = {(minX, minY), (minX, maxY), (maxX, minY), (maxX, maxY)}
        
        # Check corner set and total area match
        if corners != expected_corners:
            return False
        
        # Check if total area equals the area of the bounding rectangle
        bounding_area = (maxX - minX) * (maxY - minY)
        if total_area != bounding_area:
            return False
        
        return True
