class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums.sort()
        
        # split into two halves
        half = (n + 1) // 2 # take the ceiling
        first_half = nums[:half][::-1]  # reverse to interleave largest of smaller half
        second_half = nums[half:][::-1] # reverse to interleave largest of larger half
        """
        why we need to reverse: to prevent same value getting woven together
        for example: 4 5 5 6
        if we don't reverse: first = 4 5 and second = 5 6
        then two 5s get woven together
        also we need to reverse both not just single one:
        for example 1 1 2 2 3 3
        if we only reverse one, it will be 
        either: first = 1 1 2, second = 3 3 2
        or: first = 2 1 1, second = 2 3 3
        two 2s get woven together
        so we need to reverse both to move same value away from each other 
        """

        # interleave halves
        i = 0
        for f, s in zip(first_half, second_half):
            nums[i] = f
            nums[i + 1] = s
            i += 2
        
        # if odd length, one element left
        if len(first_half) > len(second_half):
            nums[-1] = first_half[-1]


