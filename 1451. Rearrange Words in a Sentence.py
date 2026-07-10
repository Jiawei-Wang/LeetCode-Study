class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split()
        words[0] = words[0].lower()
        hashmap = defaultdict(list) 
        for word in words:
            length = len(word)
            hashmap[length].append(word)

        sorted_values = [value for key, value in sorted(hashmap.items())]
        answer = ""
        for value in sorted_values:
            for word in value:
                answer += " " + word
        return answer[1:].capitalize()


