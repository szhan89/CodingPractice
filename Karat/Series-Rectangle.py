#####test case
matrix = [
[1,1,1,1,1],
[1,0,0,1,1],
[1,0,0,1,1],
[1,1,1,1,0]]
#####
'''Question 1
there is an image filled with 0s and 1s. There is at most one rectangle in this image filled with 0s, find the rectangle. 
Output could be the coordinates of top-left and bottom-right elements of the rectangle, or top-left element, width and height.
'''
def findArec(matrix):
    xMax = len(matrix[0])
    yMax = len(matrix)
    result = []
    for i in range(0, yMax):
        for j in range(0, xMax):
            if(matrix[i][j]==0):
                width = 0
                height = 0
                while( j+width+1 < xMax and matrix[i][j+width+1]==0):
                    width+=1
                    
                while( i+height+1 < yMax and matrix[i+height+1][j]==0):
                    height+=1
                result.append([i,j])
                result.append([i+height, j+width])
                break
        if(len(result)!=0):
            break
    return result
#print(findArec(matrix))

'''Question 2
for the same image, it is filled with 0s and 1s.
It may have multiple rectangles filled with 0s. The rectangles are separated by 1s. Find all the rectangles.
'''
def findAllrec(matrix):
    xMax = len(matrix[0])
    yMax = len(matrix)
    result = []
    for i in range(0, yMax):
        for j in range(0, xMax):
            if(matrix[i][j]==0):
                width = 0
                height = 0
                while( j+width+1 < xMax and matrix[i][j+width+1]==0):
                    width+=1     
                while( i+height+1 < yMax and matrix[i+height+1][j]==0):
                    height+=1

                #fill the found rectangle with 1
                for i_ in range(0, height+1):
                    for j_ in range(0, width+1):
                        matrix[i+i_][j+j_]=1
                        
                result.append([[i,j],[i+height, j+width]])
    return result
#print(findAllrec(matrix))

'''Question 3
the image has random shapes filled with 0s, separated by 1s. Find all the shapes. 
Each shape is represented by coordinates of all the elements inside.
'''
def findAllshape(matrix):
    def dfs(matrix,x,y,xMax,yMax):
        if(x < 0 or y < 0 or x>=xMax or y>=yMax or matrix[y][x] != 0):
            return
        shape.append([x,y])
        matrix[y][x]=1
        dfs(matrix,x+1,y,xMax,yMax)
        dfs(matrix,x-1,y,xMax,yMax)
        dfs(matrix,x,y+1,xMax,yMax)
        dfs(matrix,x,y-1,xMax,yMax)
    
    xMax = len(matrix[0])
    yMax = len(matrix)
    shape = []
    result =[]
    for i in range(0, yMax):
        for j in range(0, xMax):
            if matrix[i][j]==0:
                dfs(matrix,j,i,xMax,yMax)
                result.append(shape)
                shape=[]    
    return result
#print(findAllshape(matrix))