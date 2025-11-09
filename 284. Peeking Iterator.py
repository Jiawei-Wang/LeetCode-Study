# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize the PeekingIterator with an existing iterator.
        We eagerly pull the next element (if any) into the buffer `_next`.
        This makes peek(), next(), and hasNext() easy to implement.
        """
        self._it = iterator                # underlying iterator (provided by LeetCode)
        self._next: Optional[int] = None   # buffer holding the next element, or None if empty
        self._has_next: bool = False       # boolean flag mirroring whether buffer is valid

        # Preload the buffer with the first element if available
        if self._it.hasNext():
            self._next = self._it.next()
            self._has_next = True
            
        

    def peek(self) -> int:
        """
        Return the next element in the iteration without advancing the iterator.
        Since we keep the next element in `_next`, just return it.
        Assumes the caller only calls peek() when hasNext() is true (LeetCode guarantee).
        """
        if not self._has_next:
            raise StopIteration("No more elements to peek")
        return self._next
        

    def next(self) -> int:
        """
        Return the next element and advance the iterator.
        Steps:
         1. Save the buffered value to return.
         2. Attempt to load the subsequent element from the underlying iterator.
         3. Update the buffer flag.
        """
        if not self._has_next:
            raise StopIteration("No more elements")

        # value to return
        current = self._next

        # refill buffer from underlying iterator if possible
        if self._it.hasNext():
            self._next = self._it.next()
            self._has_next = True
        else:
            self._next = None
            self._has_next = False

        return current
        

    def hasNext(self) -> bool:
        """
        Return True if there are still elements remaining.
        This is simply whether our buffer is filled.
        """
        return self._has_next
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].