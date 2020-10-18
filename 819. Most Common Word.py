class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        """
        remove all punctuations
        change to lowercase words 
        count for each word not in banned set
        return the most common word
        """
        ban = set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        return collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]