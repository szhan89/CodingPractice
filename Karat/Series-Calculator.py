#test cases
##########
expression = "2+3-999"
expression_2 = "2-(3-999)"
##########

'''
Given a string that represent an arithmetic operator with numbers and operators i.e "2+3-999". DO NOT INCLUDE parenthesis. Return the calculation result.
'''
def calculator(expression) -> int:
    if(len(expression) == 0):
        return 0
    signed = 1
    ans = 0
    i = 0
    
    ##iterate through each character of the string
    while i < len(expression):
        ##if it is a digit, find the entire number with while loop
        if(expression[i].isdigit()):
            num=expression[i]
            while i + 1 < len(expression) and expression[i + 1].isdigit():
                i += 1
                num += expression[i]
            ans += signed * int(num)#store the number to our answer and do the plus operation with whatever sign in front of a number

        ##determine the sign for the following number
        elif(expression[i]=="+"):
            signed = 1
        ##determine the sign for the following number
        elif(expression[i]=="-"):
            signed = -1
        i+=1
    return ans

print(calculator(expression))

'''
Given a string that represent an arithmetic operator with numbers and operators i.e "2+3-999". INCLUDE parenthesis. Return the calculation result.
'''
def calculator2(expression) -> int:
    if(len(expression) == 0):
        return 0
    signed = 1
    ans = 0
    i = 0
    stack=[]
    ##iterate through each character of the string
    while i < len(expression):
        ##if it is a digit, find the entire number with while loop
        if(expression[i].isdigit()):
            num=expression[i]
            while i + 1 < len(expression) and expression[i + 1].isdigit():
                i += 1
                num += expression[i]
            ans += signed * int(num)#store the number to our answer and do the plus operation with whatever sign in front of a number
        
        ##determine the sign for the following number
        elif(expression[i]=="+"):
            signed = 1
        ##determine the sign for the following number
        elif(expression[i]=="-"):
            signed = -1
        
        ##push in the stack of whatever current result is, start new calculation after the "("
        elif(expression[i]=="("):
            stack.append(ans)
            stack.append(signed)
            ans, signed = 0,1
        ##finish the calculation inside of the parethesis, then pop it out and do the calculatation with the previous result
        elif(expression[i]==")"):
            ans = ans * stack.pop() + stack.pop()
        i+=1
    return ans

print(calculator2(expression_2))