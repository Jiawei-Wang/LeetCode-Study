# convex hull
# https://www.youtube.com/watch?v=B2AJoQSZf4M

# Graham scan algorithm
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        # cross function determines the orientation:
        # positive: counterclockwise
        # zero: collinear
        # negative: clockwise
        def cross(o, a, b):
            """Cross product of OA and OB vectors, returns z-component of the 3D cross product."""
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
        
        # Sort the points lexicographically (first by x, then by y)
        trees.sort()

        # Build the lower hull
        lower = []
        for point in trees:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], point) < 0:
                lower.pop()
            lower.append(tuple(point))  # use tuple to avoid duplicates

        # Build the upper hull
        upper = []
        for point in reversed(trees):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], point) < 0:
                upper.pop()
            upper.append(tuple(point))

        # Concatenate lower and upper hulls, remove duplicates using set
        return list(set(lower + upper))
    

# jarvis march
class Solution:
    def distance(self, p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def orientation(p, q, r):
            """Returns:
            0 if collinear,
            >0 if counterclockwise,
            <0 if clockwise
            """
            return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])

        def in_between(p, q, r):
            """Return True if point q is on segment pr"""
            return min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and \
                   min(p[1], r[1]) <= q[1] <= max(p[1], r[1])

        n = len(trees)
        if n <= 3:
            return trees

        # Find the leftmost point
        leftmost = min(trees, key=lambda x: (x[0], x[1]))
        hull = set()
        p = tuple(leftmost)

        while True:
            hull.add(p)
            q = trees[0]
            for r in trees:
                if tuple(r) == p:
                    continue
                cross = orientation(p, q, r)
                if cross < 0 or (cross == 0 and self.distance(p, r) > self.distance(p, q)):
                    q = r

            # Add all collinear points
            for r in trees:
                if tuple(r) == p or tuple(r) == tuple(q):
                    continue
                if orientation(p, q, r) == 0 and in_between(p, r, q):
                    hull.add(tuple(r))

            p = tuple(q)
            if p == tuple(leftmost):
                break

        return list(hull)


