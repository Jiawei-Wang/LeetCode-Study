class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # time: nlogn, space: n
        # dic = collections.defaultdict(int)
        # for i in nums:
        #     dic[i] += 1
        # # 下面这句语法用于sort dict中的值
        # ans = [k for k, v in sorted(dic.items(), key=lambda x: x[1], reverse=True)]
        # # sorted()的语法：https://www.w3schools.com/python/ref_func_sorted.asp
        # # key=lambda x: x[1]的解释：
        # # https://stackoverflow.com/questions/8966538/syntax-behind-sortedkey-lambda
        # return ans[:k]
        
        # bucket sort: time n space n
        bucket = [[] for _ in range(len(nums) + 1)] # every element in bucket is a list, and represents all elements with same frequency
        Count = collections.Counter(nums).items() # dictionary.items() returns a view point that contains tuples of key-value pairs
        for num, freq in Count: 
            bucket[freq].append(num) 
        ans = list(itertools.chain(*bucket)) # itertools.chain() takes a series of iterables and returns one iterable
        return ans[::-1][:k]
        
        """
        上面这个答案的思路：
        1. bucket sort用时最短
        2. 因为元素个数固定，所以频率固定，故可以使用bucket sort
        3. 创建一个二维list，下标为频率，元素为此频率的所有数字
        4. 将二维list拍扁成一维的，然后取末尾k个元素即可
        
        使用的技巧：
        1. 使用for循环创建二维list
        2. 使用collections.Counter()来计数
        3. 使用dictionary.items()来获取所有元素
        4. 使用itertools.chain()来给list降维
        5. 使用[::-1]来省去反转元素的步骤
        """