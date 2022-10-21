##########Test case
matrix=[
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","1","0"],
  ["0","0","0","0","0"]
]
##########
'''
You are given a 2D array consisting of 1's and 0's and a tuple of starting coordinates in the matrix. 
Return a list of the neighboring coordinates that are 0's NOT 1's.
'''

def main(matrix, start):
    result=[]
    x = start[0]
    y = start[1]
    findZeros(matrix, x, y, result)
    for line in matrix:
        print(line,'\n')
    return result

def findZeros(matrix, x, y, result):
    if(x < 0 or y <0 or x>=len(matrix) or y>=len(matrix[0]) or matrix[x][y]!='0'):
        return
    result.append([x,y])
    matrix[x][y]='#'
    findZeros(matrix, x+1, y, result)
    findZeros(matrix, x-1, y, result)
    findZeros(matrix, x, y-1, result)
    findZeros(matrix, x, y+1, result)
    
#print(main(matrix,[2,2]))

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
    
print(main2(matrix, [2,2]))