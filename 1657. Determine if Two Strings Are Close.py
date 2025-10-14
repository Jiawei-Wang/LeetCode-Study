class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1)
        array1 = sorted([freq for key, freq in counter1.items()])
        set1 = set([key for key, freq in counter1.items()])
        
        counter2 = Counter(word2)
        array2 = sorted([freq for key, freq in counter2.items()])
        set2 = set([key for key, freq in counter2.items()])

        return array1 == array2 and set1 == set2