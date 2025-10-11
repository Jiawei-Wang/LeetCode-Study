class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = sum(arr[0:k])
        count = 0
        if total / k >= threshold:
            count += 1
        for i in range(k, len(arr)):
            total += arr[i] - arr[i-k]
            if total / k >= threshold:
                count += 1
        return count

