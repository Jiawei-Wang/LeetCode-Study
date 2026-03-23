class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        count = defaultdict(int)
        for number in arr:
            count[number] += 1

        counter = [[] for _ in range(0, n+1)]
        # counter[i] = [a, b, c]: there are 3 numbers that occur i times in the input arr

        for number, occur in count.items():
            counter[occur].append(number)
        
        remove = 0
        total = 0
        for i in range(n, 0, -1): # one number can occur anywhere between 1 and n times
            curr = counter[i]
            if curr:
                for number in curr:
                    remove += 1
                    total += i
                    if total >= n//2:
                        return remove



