class Solution:
    def capitalizeTitle(self, title: str) -> str:
        def change(word):
            if len(word) <= 2:
                return word.lower()
            else:
                return word[0].upper() + word[1:].lower()
        
        array = title.split(" ")
        for i in range(len(array)):
            array[i] = change(array[i]) 
        return " ".join(array)