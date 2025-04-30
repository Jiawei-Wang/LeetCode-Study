class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        unique = set([])
        for word in words:
            string = []
            for char in word:
                string.append(morse[ord(char)-ord('a')])
            unique.add("".join(string))
        return len(unique)