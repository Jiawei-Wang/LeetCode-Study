class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # Convert bank to a set for O(1) membership tests
        bank = set(bank)
        
        # If the end mutation is not reachable (not in bank), no valid path exists
        if end not in bank:
            return -1

        # Allowed characters for genetic mutation
        genes = ['A', 'C', 'G', 'T']
        
        # BFS queue: stores (current_gene, steps_taken)
        queue = deque([(start, 0)])
        
        # Visited set prevents revisiting the same mutation
        visited = set([start])

        while queue:
            current, steps = queue.popleft()
            
            # If we've reached the end gene, return number of steps taken
            if current == end:
                return steps
            
            # Try mutating each position in the current gene
            for i in range(len(current)):
                for g in genes:
                    # Skip if replacing with the same character
                    if current[i] == g:
                        continue
                    
                    # Create a new mutation by replacing character at index i
                    mutated = current[:i] + g + current[i+1:]
                    
                    # Valid mutation: must be in bank and not visited
                    if mutated in bank and mutated not in visited:
                        visited.add(mutated)
                        queue.append((mutated, steps + 1))
        
        # If BFS completes without finding 'end', no valid mutation path exists
        return -1
