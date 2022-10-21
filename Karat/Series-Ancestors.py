from collections import defaultdict, deque
from queue import Empty
#####test case
input = [
    (2, 3), (3, 15), (3, 6), (5, 6), (5, 7),
    (4, 5), (4, 8), (4, 9), (9, 11), (14, 4),
]
#####
'''Question 1
         14
         |
  2      4
  |    / | \
  3   5  8  9
 / \ / \     \
15  6   7    11
输入是int[][] input, input[0]是input[1] 的parent,比如 {{1,4}, {1,5}, {2,5}, {3,6}, {6,7}}会形成上面的图
Output:只有0个parents和只有1个parent的node
'''
def getparents(input):
    graph=dict()
    for parent, child in input:
        graph[parent]=[]
        graph[child]=[]
        
    for parent, child in input:
        graph[child].append(parent)
    
    zero=[]    
    one=[]
    for key in graph:
        if (len(graph[key])==0):
            zero.append(key)
        elif (len(graph[key])==1):
            one.append(key)
    return [zero,one]
print(getparents(input))

'''Question 2
  1    2    3
/  \  /      \
4    5        6
                \
                  7
输入是int[][] input, input[0]是input[1] 的parent,比如 {{1,4}, {1,5}, {2,5}, {3,6}, {6,7}}会形成上面的图
Output: True if x and y has common ancestor
'''

def findancestors(graph, result, node):
    for parent in graph[node]:
        result.append(parent)
        findancestors(graph, result, parent)
def commonAncestor(input,nodeA, nodeB):
    graph={}
    for parent,child in input:
        graph[parent]=[]
        graph[child]=[]
    
    for parent,child in input:
        graph[child].append(parent)
        
    nodeAList=[]
    nodeBList=[]
    findancestors(graph, nodeAList, nodeA)
    findancestors(graph, nodeBList, nodeB)
    
    for i in nodeAList:
        if i in nodeBList:
            return True
    return False
#print(commonAncestor(input, 7,11))

'''Question 3
  1    2    3
/  \  /      \
4    5        6
                \
                  7
find the earliest ancestor
'''
def findEancestor(input,node):
    graph={}
    for parent,child in input:
        graph[parent]=[]
        graph[child]=[]
        
    for parent,child in input:
        graph[child].append(parent)
    
    queue = deque()
    levels = 0
    for i in graph[node]:
        queue.append(i)
    cur = 0
    while len(queue) != 0:
        levels = len(queue)
        for i in range(0,levels):    
            cur = queue.popleft()
            for parent in graph[cur]:
                queue.append(parent)
    return cur
#print(findEancestor(input, 7))