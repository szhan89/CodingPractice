'''
Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique positive integer identifier.

For example, in this diagram, 6 and 8 have common ancestors of 4 and 14.

               15
              / \
         14  13  21
         |   |
1   2    4   12
 \ /   / | \ /
  3   5  8  9
   \ / \     \
    6   7     11

pairs = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (15, 21), (4, 8), (4, 9), (9, 11), (14, 4), (13, 12),
    (12, 9), (15, 13)
]

Write a function that takes this data and the identifiers of two individuals as inputs and returns true if and only if they share at least one ancestor. 

Sample input and output:

hasCommonAncestor(pairs, 3, 8)   => false
hasCommonAncestor(pairs, 5, 8)   => true
hasCommonAncestor(pairs, 6, 8)   => true
hasCommonAncestor(pairs, 6, 9)   => true
hasCommonAncestor(pairs, 1, 3)   => false
hasCommonAncestor(pairs, 3, 1)   => false
hasCommonAncestor(pairs, 7, 11)  => true
hasCommonAncestor(pairs, 6, 5)   => true
hasCommonAncestor(pairs, 5, 6)   => true
hasCommonAncestor(pairs, 3, 6)   => true
hasCommonAncestor(pairs, 21, 11) => true

n: number of pairs in the input
'''
pairs = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (15, 21),
    (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9),
    (15, 13)
]

from collections import defaultdict

def hasCommonAncestor(pairs, node1, node2):
    def dfs(map_,node,list_):
        for i in map_[node]:
            list_.append(i)
            dfs(map_,i,list_)
            
    #map_ = defaultdict(list)
    map_ = dict()
    #initialize the map
    for parent, child in pairs:
        map_[child]=[]
        map_[parent]=[]
        
    #build the map, find ancestors
    for parent, child in pairs:
        map_[child].append(parent)
    
    ancestorsA = []
    ancestorsB = []
    dfs(map_, node1,ancestorsA)
    dfs(map_, node2, ancestorsB)
    print(ancestorsA)
    print(ancestorsB)
    
    #check for shared ancestor
    for i in range(0,len(ancestorsA)):
        print(ancestorsA[i])
        for j in range(0,len(ancestorsB)):
            if (ancestorsA[i] == ancestorsB[j]):
                return True
    return False
    
    '''for a in ancestorsA:
        print(a)
        if (a in ancestorsB):
            return True
        return False'''
    


print(hasCommonAncestor(pairs, 6, 8))        
        
'''print(hasCommonAncestor(pairs, 3, 8))
print(hasCommonAncestor(pairs, 5, 8))
print(hasCommonAncestor(pairs, 6, 8))
print(hasCommonAncestor(pairs, 6, 9))
print(hasCommonAncestor(pairs, 1, 3))
print(hasCommonAncestor(pairs, 3, 1))
print(hasCommonAncestor(pairs, 7, 11))
print(hasCommonAncestor(pairs, 6, 5))
print(hasCommonAncestor(pairs, 5, 6))
print(hasCommonAncestor(pairs, 3, 6))
print(hasCommonAncestor(pairs, 21, 11))'''