class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        
        # Constant defined for color drawing to person
        BLUE, GREEN = 1, -1
        # -------------------------------------
        
        def draw( person_id, color ):
            
            # Draw person_id as color
            color_of[person_id] = color
            
            # Draw the_other, with opposite color, in dislike table of current person_id
            for the_other in dislike_table[ person_id ]:
   
                if color_of[the_other] == color:
                    # the_other has the same color of current person_id
                    # Reject due to breaking the relationship of dislike
                    return False

                if (not color_of[the_other]) and (not draw( the_other, -color)):
                    # Other people can not be colored with two different colors. 
					# Therefore, it is impossible to keep dis-like relationship with bipartition.
                    return False
                    
            return True
        
        
        # ------------------------------------------------
		
        if N == 1 or not dislikes:
            # Quick response for simple cases
            return True
        
        # each person maintain a list of dislike
        dislike_table = defaultdict( list )
        
        for p1, p2 in dislikes:
            
            # P1 dislikes P2
            # P1 and P2 should be painted with two different color
            dislike_table[p1].append( p2 )
            dislike_table[p2].append( p1 )
        
        # quick lookup table to check a person's assigned color
        # key: person ID
        # value: color of person
        color_of = defaultdict(int)

        # Try to draw dislike pair with different colors in DFS
        for person_id in range(1, N+1):
            
            if (not color_of[person_id])  and (not draw( person_id, BLUE)):
                # Other people can not be colored with two different colors. 
				# Therefore, it is impossible to keep dis-like relationship with bipartition.
                return False 
        
        return True


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        
        # Constant defined for color drawing to person
        BLUE, GREEN = 1, -1
        # -------------------------------------

        # Update dislike relationship, either a dislikes b, or b dislikes a        
        dislike = defaultdict(list)
        for a, b in dislikes:
            dislike[a].append(b)
            dislike[b].append(a)
        
        # Color map of each person
        color_of = dict()

        for person in range(1, N+1):
            
            # If this person has been draw, just skip
            if person in color_of: continue
            
            # Without the loss of generality, start drawing from BLUE        
            # (It can be GREEN if you like)
            color_of[person] = BLUE
            bfs_queue = deque([(person, BLUE)])

            while bfs_queue:

                cur, color = bfs_queue.popleft()
                for enemy in dislike[cur]:
                    
                    if enemy not in color_of:
                        # Draw enemy with opposite color
                        color_of[enemy] = -1*color
                        bfs_queue.append( (enemy, color_of[enemy]) )

                    elif color_of[enemy] == color:
                        # If enemy and me have same color, woops, it is impossible to being bipartite
                        return False
                    
        return True