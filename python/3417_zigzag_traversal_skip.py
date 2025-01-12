def zigzagTraversal(grid):
        x = 1 # 1:right, 0:left
        c = 0
        n = len(grid[0])
        res = []
        
        for row in grid:
            
            for i in range(0,n):
                if c>0:
                    c = 0
                    continue
                
                res.append(row[i] if x==1 else row[n-i-1])
                c += 1

            x ^= 1

        return res