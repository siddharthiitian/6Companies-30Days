class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # smoother = [[0,0][0,1],[0,2],[1,0][1,1][1,2],[2,0],[2,1],[2,2]]
        rows, cols = len(img), len(img[0])
        img_c = [[0] * cols for _ in range(rows)]
        
        for i in range(len(img)):
            for j in range(len(img[i])):
                # up
                sum_c = img[i][j]
                valid_i = 1
                if i-1>=0:
                    sum_c += img[i-1][j]
                    valid_i += 1
                # down
                if i+1<=len(img)-1:
                    sum_c += img[i+1][j]
                    valid_i += 1
                # left
                if j-1>=0:
                    sum_c += img[i][j-1]
                    valid_i += 1
                # right
                if j+1<=len(img[i])-1:
                    sum_c += img[i][j+1]
                    valid_i += 1
                # diagonal up    1
                if i-1>=0 and j-1>=0:
                    sum_c += img[i-1][j-1]
                    valid_i += 1
                # diagonal down 2
                if i-1>=0 and j+1<=len(img[i])-1:
                    sum_c += img[i-1][j+1]
                    valid_i += 1
                # diagonal down  2
                if i+1<=len(img)-1 and j-1>=0:
                    sum_c += img[i+1][j-1]
                    valid_i += 1
                # diagonal down 2
                if i+1<=len(img)-1 and j+1 <=len(img[i])-1:
                    sum_c += img[i+1][j+1]
                    valid_i += 1
                
                img_c[i][j] = floor(sum_c/valid_i)
                # d

        return img_c