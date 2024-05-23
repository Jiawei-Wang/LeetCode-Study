class Solution:
    def fullJustify(self, words: List[str], max_width: int) -> List[str]:
        """
        input: a list of strings
        output: a list of strings

        combine strings from input with " " to create output
        1. each string in output is of length maxWidth
        2. each string contains as many words as possible 
        3. " " between input strings should be distributed evenly
           or the slots on the left have more than the one on the right
           so 5 spaces for 3 slots should be: [2, 2, 1], not [3, 1, 1]
        4. last string should be aligned to the left with all extra " " on the right
        
        thoughts:
        1. go through input array one element at a time
        2. see if new element can be added (still have room for next: yes/no)
            1) if yes, we add it, move to next element
            2) if not, we create current string 
                1- check how many " " we have 
                2- distribute the " " between slots
        """
        
        def distribute(a, b): # to evenly distrubte a spaces between b slots
            q = a // b
            r = a % b
            return [q + 1] * r + [q] * (b - r)

        length = len(words)
        answer = [] # holds return value: list of strings
        cur_width = 0 # holds width of current string
        start_index = 0 # holds index of start word of current string

        for index in range(length):
            if index == length - 1:
                string = ""
                for i in range(start_index, index):
                    string += words[i] + " "
                string += words[index]
                left_over = max_width - len(string) 
                answer.append(string + " " * left_over)
                break

            word = words[index]
            cur_width += len(word) + 1
            available_for_next = max_width - cur_width
            
            if available_for_next >= len(words[index+1]):
                continue
            else: # word is the last one for cur_string, we start building cur_string
                slot_number = index - start_index
                if slot_number == 0:   
                    answer.append(words[index] + " " * (max_width-len(words[index])))
                else:
                    space_number = slot_number + available_for_next + 1
                    distribution = distribute(space_number, slot_number)
                    string = words[start_index] + " " * distribution[0]
                    for i in range(start_index+1, index):
                        string += words[i] + " " * distribution[i-start_index]
                    answer.append(string+words[index])

                start_index = index+1    
                cur_width = 0
        
        return answer
                


                
                







        