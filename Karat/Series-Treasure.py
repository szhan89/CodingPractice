##########Test case
from collections import defaultdict
from tempfile import tempdir


matrix=[
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","1","0"],
  ["0","0","0","0","0"]
]
board=[
    [  1,  0,  0, 0, 0 ],
    [  0, -1, -1, 0, 0 ],
    [  0, -1,  0, 1, 0 ],
    [ -1,  0,  0, 0, 0 ],
    [  0,  1, -1, 0, 0 ],
    [  0,  0,  0, 0, 0 ],    
]

##########
'''
You are given a 2D array consisting of 1's and 0's and a tuple of starting coordinates in the matrix. 
Return a list of the neighboring coordinates that are 0's NOT 1's.
'''

def findZerosFourDirection(matrix, x, y):
    result = []
    def dfs(x,y):
        if(x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]) or matrix[x][y]!= '0'):
            return
        matrix[x][y] = '1'
        result.append([x,y])
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
    dfs(x,y)
    return result
#print(findZerosFourDirection(matrix,2,2))


'''
You are given a 2D array consisting of 1's and 0's and a tuple of starting coordinates in the matrix. 
Check whether you can traverse all the zero
'''
def main2(matrix, start):
    result=[]
    x = start[0]
    y = start[1]
    findZeros(matrix, x, y, result)
    
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if(matrix[i][j]=='0'):
                return False
    for line in matrix:
        print(line,'\n')
    return True
def findZeros(matrix, x, y, result):
    if(x < 0 or y <0 or x>=len(matrix) or y>=len(matrix[0]) or matrix[x][y]!='0'):
        return
    result.append([x,y])
    matrix[x][y]='#'
    findZeros(matrix, x+1, y, result)
    findZeros(matrix, x-1, y, result)
    findZeros(matrix, x, y-1, result)
    findZeros(matrix, x, y+1, result)
    
#print(main2(matrix, [2,2]))

def findShortestPath(start,end,matrix):
    allPaths = defaultdict(list)
    x,y = start[0], start[1]
    xlen = len(matrix)
    ylen = len(matrix[0])
    remain = 0
    path_ =[]
    #count remains
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if(matrix[i][j]==1):
                remain+=1
    
    def dfs(x,y, path, remains):
        if(x<0 or y<0 or x >= xlen or y >= ylen or matrix[x][y] == -1 or matrix[x][y] == 2):
            return
        path.append([x,y])
        cur=matrix[x][y]
        if(cur==1):
            remains-=1
        if(x==end[0] and y==end[1] and remains==0):
            allPaths[len(path)].append(path.copy())
            #backtrack
            path.pop()
            matrix[x][y]=cur
            return
        matrix[x][y]=2
        dfs(x+1,y,path,remains)
        dfs(x-1,y,path,remains)
        dfs(x,y+1,path,remains)
        dfs(x,y-1,path,remains)
        #back track
        path.pop()
        matrix[x][y]=cur
    dfs(start[0],start[1],path_,remain)
    return(allPaths[min(allPaths)])
print(findShortestPath([5,2],[2,0],board))
    