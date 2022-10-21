import collections
#####test case
student_course_pairs_1 = [
  ["58", "Software Design"],
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["17", "Software Design"],
  ["58", "Mechanics"],
  ["58", "Economics"],
  ["17", "Linear Algebra"],
  ["17", "Political Science"],
  ["94", "Economics"],
  ["25", "Economics"],
]
courses =  [
    [ 'DataStructures', 'Algorithms' ], [ 'FoundationsOfCS', 'OperatingSystems' ], [ 'ComputerNetworks', 'ComputerArchitecture' ], [ 'Algorithms', 'FoundationsOfCS' ], [ 'ComputerArchitecture', 'DataStructures' ], [ 'SoftwareDesign', 'ComputerNetworks' ]\
    ]

#####

'''Question1
Write a function that takes in a list of (student ID number, course name) pairs and returns, for every pair of students, a list of all courses they share.
'''
def findPairs(pairs):
    mapVar = collections.defaultdict(list)
    for student, course in pairs:
        mapVar[student].append(course)
    
    keys = list(mapVar.keys())    
    result = collections.defaultdict(list)
    
    for i in range(0,len(keys)):
        for j in range(i+1, len(keys)):
            for course in mapVar[keys[i]]:
                result[keys[i],keys[j]]
                if course in mapVar[keys[j]]:
                    result[keys[i],keys[j]].append(course)
                
    return result 
#print(findPairs(student_course_pairs_1))

'''Question2
Find the mid point of a course
'''
def findMidptCourse(coures):
    map_ = collections.defaultdict(str)
    count = collections.defaultdict(int)
    startKey = str()
    #build map
    for cur, next in courses:
        map_[cur]=next
        count[cur]+=1
        count[next]+=1
        
    #find start course
    for key in count:
        if count[key]==1 and key in map_:
            startKey=key
            break
    
    midpt = len(count)//2
    
    pt = startKey
    result = str()
    while midpt>0:
        result = map_[pt]
        pt = map_[pt]
        midpt-=1
    
    return result
print(findMidptCourse(courses))
