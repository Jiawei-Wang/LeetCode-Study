class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]
        seen = set(stack)
        while stack:
            i = stack.pop()
            for j in rooms[i]:
                if j not in seen:
                    stack.append(j)
                    seen.add(j)
                    if len(seen) == len(rooms): return True
        return len(seen) == len(rooms)