# 读题理解：将每个斜线上的数字从小到大排列

# 解法1：把每一斜线读进来，然后排序并输出
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # 首先是右上半边
        # 倒序遍历第一行每一个元素
        for i in range(len(mat[0])-1,-1,-1):
            # 创建一个array
            temp = []
            # 遍历斜线，把斜线上每个元素放进去
            '''
            for j in range(i, len(mat[0])):
                temp.append(mat[j-i][j])
            上面的代码是错误的，因为斜线并不一定总能走到最右边
            例如 2 row 4 column的array，斜线最长只有2
            所以这里要考虑边界，斜线的长度应该是row和当前 j 的range中较小者
            '''
            length = min(len(mat), len(mat[0])-i) # 例如 3 row 4 column 的mat，从[0,0]开始的斜线长度为3而非4
            for j in range(i, i+length):
                temp.append(mat[j-i][j])
            # sort
            temp.sort()
            # 再次遍历斜线，将array中元素依次放入
            for j in range(i,i+length):
                mat[j-i][j] = temp[j-i]
            del temp

        # 然后是左下半边
        if len(mat) > 1:
            # 遍历下标从 1 开始的每个row
            for x in range(1, len(mat)):
                # 同样也是创建一个array，然后计算该斜线长度
                another_array = []
                another_length = min(len(mat[0]), len(mat)-x)
                # 遍历，放进array，sort，再遍历放回
                for y in range(x, x+another_length):
                    another_array.append(mat[y][y-x])
                another_array.sort()
                for y in range(x, x+another_length):
                    mat[y][y-x] = another_array[y-x]
                del another_array

        # 返回2d array
        return mat


# 解法2：改良
class Solution:
    def diagonalSort(self, A):
        # n 是 row 数，m 是 column 数
        n, m = len(A), len(A[0])

        # defaultdict(function): 如果给的key不存在,使用function返回一个默认的value
        # 如果d中没有对应的key,初始化key,value为一个空的list
        d = collections.defaultdict(list)

        for i in range(n):
            for j in range(m):
                # d中的每个key代表的是一条斜线,它的value是线上所有元素的值的集合
                d[i - j].append(A[i][j])

        for k in d:
            # 使得value变成递减的array
            d[k].sort(reverse=1)

        # 对于A中的每个元素,找到它对应的那条斜线,将array中末尾的值填入
        for i in range(n):
            for j in range(m):
                A[i][j] = d[i - j].pop()

        return A


# 2026
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        hashmap = defaultdict(list)
        for i in range(row):
            for j in range(col):
                heappush(hashmap[i - j], mat[i][j])
        for i in range(row):
            for j in range(col):
                mat[i][j] = heappop(hashmap[i - j])
        return mat