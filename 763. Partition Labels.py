class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # turn input string into segment hashmap
        # key: char, value: an array of char indexes in the string
        hashmap = dict()
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = [i]
            else:
                hashmap[s[i]].append(i)
        
        answer = []
        head = -1
        tail = 0
        for i in range(len(s)):
            char = s[i]
            tail = max(tail, hashmap[char][-1])
            if tail == i: # if all elements in current segment don't expand segment anymore
                answer.append(tail-head) # we finish current segment
                head = tail # create a new segment
        return answer