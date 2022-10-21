#####test cases
meeting = [[1300, 1500], [930, 1200],[830, 845]]
#####

'''
Given a list that contains start and end time for meetings, check if a meeting time can be inserted
'''
def freeTime(list_,time):
    for start, end in list_:
        if((time[0]>end and time[0]<=start) or (time[1]>start and time[1]<=end) or (time[0]<=start and time[1]>=end)):
            return False
        return True
print(freeTime(meeting, [1450,1500]))

'''
Given a list that contains start and end time for meetings, return all its free space
'''    
def merge(list_):
    list_= sorted(list_, key=lambda l:l[0])
    pre = list_[0]
    merged = []
    for cur in list_:
        if(cur[0]<pre[1]):
            pre[0] = min(cur[0],pre[0])
            pre[1] = max(cur[1],pre[1])
        else:
            merged.append(pre)
            pre=cur
    merged.append(pre)
    
    result=[]
    start = 0
    for interval in merged:
        result.append([start, interval[0]])
        start = interval[1]
    if start < 2400:
        result.append([start, 2400])
    return result
print(merge(meeting))