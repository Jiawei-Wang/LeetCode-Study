# sort一个list，但是有两个限制：1. 不能用built in sort，2. in place

"""
一个想法：我们知道一共只有3个数字0，1，2，所以数出一共有多少个0，1，2，然后让对应长度的sublist全部修改为对应数字
time n (一次遍历，一次修改)，space 1 (保存一个只有三个key value pair的dictionary即可)
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        d = {0: 0, 1: 0, 2: 0}
        for i in nums:
            d[i] += 1
        
        for i in range(0, d[0]):
            nums[i] = 0
        for i in range(d[0], d[0]+d[1]):
            nums[i] = 1
        for i in range(d[0]+d[1], d[0]+d[1]+d[2]):
            nums[i] = 2
        return nums


"""
dutch national flag problem
If the ith element is 0 then swap the element to the low range, thus shrinking the unknown range.
Similarly, if the element is 1 then keep it as it is but shrink the unknown range.
If the element is 2 then swap it with an element in high range.
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 初始化让low和mid都等于0，high指向末尾
        red, white, blue = 0, 0, len(nums)-1
        
        # 将list分为四部分，0-low，low-mid，mid-high，high-end
        while white <= blue: # mid-high部分存储的是待检测的元素
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red] # 如果为0则将它和low指向的元素对调
                white += 1 # 对调后low和mid各往前挪一格
                red += 1
            elif nums[white] == 1: # 如果为1则直接让mid往前挪一格
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white] # 如果为2则让它和high对调
                blue -= 1 # 然后high往后退一格