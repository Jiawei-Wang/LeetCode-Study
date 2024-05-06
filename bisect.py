# Taken from cpython/lib/bisect.py
# https://github.com/python/cpython/blob/3.9/Lib/bisect.py

def bisect_right(a, x, lo=0, hi=None):
    """
    return index i to insert value x into sorted list a, such that after the insertion:
        1. everything on the left <= x 
        2. x < everything on the right
        3. for example: [0, 1, 2, 4]: 
            1) to insert value 3, return index 3 
            2) to insert value 2, return index 3 (both 3 and 2 should be inserted at the current location of value 4)
            3) to insert value 0, return index 1 (0 should be inserted at the current location of value 1)
            4) to insert value -1, return index 0 (-1 should be appended to the left at the begining of a)
            5) to insert value 5, return index 4 (5 should be appended to the right at the end of a)
        
        insert at index i: everything (including the element currently at index i) will be moved one index towards the right side
    """

    """
    length = how many slots between lo and hi (both included)

    part one: two pointers
        1. lo is by default 0, pointing at the first element in a
        2. hi is by default len(a), pointing behind the last element in a

        why for first loop: hi = len(a) instead of len(a) -1 
        because then we are only looking between [lo:hi] (both included)
        so for example: [0, 1, 2] to insert 3, correct answer should be index 3 
        if hi = len(a) -1, it will return index 2, which is incorrect

        3. for first loop: length = len(a) + 1, mid = length // 2 
           (since hi is pointing behind the last element in a, and a has at least 1 element, so length is at least 2)
            1) if len(a) is even, mid will be the middle-right one 
               for example: 4 elements in a, lo = 0, hi = 4 (length is 5), mid = (0 + 4) // 2 = 2 (mid is pointing at the 3rd element)
                            2 elements in a, mid = (0 + 2) // 2 = 1 (mid is pointing at the 2nd element, the right one between the two)
            2) if len(a) is odd, mid will be the middle one
               for example: 3 elements in a, mid = (0 + 3) // 2 = 1 (mid is pointing at the 2nd element)
                            1 element in a, mid = (0 + 1) // 2 = 0 (mid is pointing at the 1st element, the only one)
    """
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)

    """
    part two: loops
        1. end goal is to return the index i where lo = i = hi, so:
            1) if x < mid: we don't know anything about mid - 1 and x, but x < mid is for sure, so i can only be at most mid (mid - 1 <= x < mid then we insert at index mid)
            2) if mid <= x: we don't know anything about x and mid + 1, but mid <= x is for sure, so i can only be at least mid + 1 (mid <= x < mid + 1 then we insert at index mid + 1)
        2. first loop cuts half of the list off, future loops start
        3. for all future loops: hi could be pointing at an index within a, or still at len(a), length = a[lo:hi] (hi included)
            1) first case: hi no longer points at len(a)
                1> if length >= 3: mid will be the middle (odd) or middle-left one (even), everything else is the same as first loop
                   for example: 3 elements in a, mid is pointing at the middle one, 4 elements in a: mi is pointing at the middle left one
                2> if length = 2: mid will be the left one of the two (lo = mid = hi - 1), after the loop:
                    1- hi is moved to lo 
                    2- or lo is moved to hi
                    (either case length becomes 1)
                3> if length = 1: lo == hi, there will be no further loop
                   (this is different from first loop, in first loop there is at least 1 element, so length = len(a) + 1 is at least 2)
            2) second case: hi stays at len(a):
                just treat it the same as first loop 
                1> if length >= 3: doesn't matter, we treat it same as the first loop, get the middle one or middle-right one
                2> if length = 2: we only have 1 element in a[lo: hi] (hi included)
                                  lo is the last element in original a and only element, hi is pointing behind a, mid is pointing at lo, after the loop:
                                    1- hi is moved to lo
                                    2- or lo is moved to hi <- this case is for: everything in original a is <= x, so return value is len(a)
                                    (either case length becomes 1, no further loop) 
    """
    while lo < hi:

        """
        why while lo < hi rather than lo <= hi:
        to prevent endless loop

        if we have while lo <= hi:
        1. if 3 elements: it will go into either 2 elements loop or 1 element loop
        2. if 2 elements: it will go into either 1 element loop or stop
        3. if 1 element: it will go into either 1 element loop or stop
        for example: [0, 1, 2], lo = 0, hi = 2, to insert -1, we should return 0
        however with while lo <= hi:
        1. mid = 1: lo = 0, hi = 1
        2. mid = 0: lo = 0, hi = 0
        3. mid = 0: endless loop

        if we have while lo < hi: 
        for example: [0, 1, 2], lo = 0, hi = 2, to insert -1, we should return 0
        1. mid = 1: lo = 0, hi = 1
        2. mid = 0: lo = 0, hi = 0
        3. ends
        """
        mid = (lo+hi)//2
        if x < a[mid]: hi = mid
        else: lo = mid+1
    return lo 


def bisect_left(a, x, lo=0, hi=None):
    """
    what if we want to insert x such that
    1. everything on the left < x
    2. x <= everything on the right
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        
        """
        this is the only place where logic is changed:
        1. if mid < x: i can only be at least mid + 1 (mid < x <= mid + 1)
        2. if x <= mid: i can only be at most mid (mid - 1 < x <= mid)
        """
        if a[mid] < x: lo = mid+1
        else: hi = mid
    return lo


def insort_right(a, x, lo=0, hi=None):
    """
    this one is simple, get the index i then insert new element x into a
    """
    lo = bisect_right(a, x, lo, hi)
    a.insert(lo, x)


def insort_left(a, x, lo=0, hi=None):
    """
    this one is the same
    """
    lo = bisect_left(a, x, lo, hi)
    a.insert(lo, x)