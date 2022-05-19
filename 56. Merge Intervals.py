class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort: nlogn
        # merge: n
        if len(intervals) <= 1:
            return intervals
        
        intervals.sort(key=lambda x: x[0]) # 用start作为sort的标准
        # intervals现在长这样：
        # [[1,5],
        #  [2,11],
        #  [15,20],
        #  [16,18]]
        # 所有的元素的头部都按顺序排列，但尾部未知
        
        result = [intervals[0]]
        curr = intervals[0]
        
        # 一个逻辑是：当重叠发生时，result中的元素总数就相应-1，可以使用修改当前元素并略过下一个元素的方法来减少append操作次数
        for i in intervals:
            if i[0] <= curr[1]: 
                curr[1] = max(curr[1], i[1]) # 如果发生重叠，则一定是前一个元素尾部长于后一个元素的头部，将前者尾部设为两者中尾部较大者，后者被自动略过
            else:
                curr = i # 如果无重叠，则将新元素加入，并更新curr指针
                result.append(i)
        
        return result

    """
    关于为什么初始化result = [[1,5]]，且一直只有append操作，但最后结果为[[1,11], [15,20]]的理解：
    
    1. Immutable type: 
    a = 'abc'
    print(id(a)) # 地址1
    b = [a]
    print(id(b)) # 地址2
    a = 'def'
    print(b) # ['abc']
    print(id(a)) # 地址3
    print(id(b)) # 地址2
    immutable类型的变量，在重新赋值时，即在内存内创建新的值，然后将变量指向该值，之前的则被抛弃，所以改变a并不会改变b
    
    2. mutable type:
    a = [1,2]
    print(id(a)) # 地址1
    b = [a]
    print(b) # [[1, 2]]
    print(id(b)) # 地址2
    a[1] = 3
    print(b) # [[1, 3]]
    print(id(a)) # 地址1
    print(id(b)) # 地址2
    mutable类型的变量，比如list，更改其中的值的时候会保留相同的地址，所以改变a的时候b也发生改变
    
    但是注意下面的情况：
    a = [1,2]
    print(id(a))

    b = [a]
    print(b)
    print(id(b))

    a = [5,6]
    print(id(a))
    print(b)
    print(id(b))
    在这里a的地址发生了变化，所以即使a发生了改变，b并不改变
    """