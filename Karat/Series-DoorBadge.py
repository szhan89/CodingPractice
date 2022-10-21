#####test case
from collections import defaultdict
import math
from unittest import result

badge_records = [
   ["Martha",   "exit"],
   ["Paul",     "enter"],
   ["Martha",   "enter"],
   ["Martha",   "exit"],
   ["Jennifer", "enter"],
   ["Paul",     "enter"],
   ["Curtis",   "enter"],
   ["Paul",     "exit"],
   ["Martha",   "enter"],
   ["Martha",   "exit"],
   ["Jennifer", "exit"],
]

access =[["Paul", "1355"],
["Jennifer", "1910"],
["John", "835"],
["John", "830"],
["Paul", "1315"],
["John", "1615"],
["John", "1640"],
["Paul", "1405"],
["John", "855"],
["John", "930"],
["John", "915"],
["John", "730"],
["John", "940"],
["Jennifer", "1335"],
["Jennifer", "730"],
["John", "1630"],
["Jennifer", "500"]] 

#####


'''Question 1
Given a list of people who enter and exit, find the people who entered without
their badge and who exited without their badge.
Personal Notes:
    if the person is inside, it entered -> invalid exit
    if the persion not inside, it exit -> invalid enter 
'''

def invalidEnterExit(list):
    inside= set()
    invalidEnter = set()
    invalidExit = set()
    for name, action in list:
        #for name, action in record:
            if(action=="enter"):
                if (name in inside):
                    invalidExit.add(name)
                else:
                    inside.add(name)
            elif(action=="exit"):
                if (name not in inside):
                    invalidEnter.add(name)
                else:
                    inside.remove(name)
                    
    while len(inside)!=0:
        invalidExit.add(inside.pop())
    
    return [invalidExit,invalidEnter]
#print(invalidEnterExit(badge_records))

'''Question 2
Given a list of people who access door with their badge in a time interval, find the persion who access multiple time within one hour
'''

def timeDifference(time1, time2):
    hour1 = math.floor((int(time1)/100))*60 + int(time1)%100
    hour2 = math.floor((int(time2)/100))*60 + int(time2)%100
    return abs(hour2-hour1)
def accessWithOneHour(visits):
    access = defaultdict(list)
    for name, time in visits:
        access[name].append(time)
    
    result = {}
    for key in access:
        times = sorted(access[key])
        freqTime = set()
        for i in range(0,len(times)):
            if(i+1 < len(times) and timeDifference(times[i],times[i+1])<=60):
                freqTime.add(times[i])
                freqTime.add(times[i+1])
        if(len(freqTime)>1):
            result[key]=sorted(freqTime)
    return result           

print(accessWithOneHour(access))