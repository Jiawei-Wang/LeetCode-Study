class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row = len(img)
        col = len(img[0])
        answer = [[0] * col for _ in range(row)]

        def get_average(r, c):
            total = 0
            count = 0
            for i in (r-1, r, r+1):
                for j in (c-1, c, c+1):
                    if 0 <= i < row and 0 <= j < col:
                        total += img[i][j]
                        count += 1
            answer[r][c] = total // count

        for r in range(row):
            for c in range(col):
                get_average(r, c)
        
        return answer
