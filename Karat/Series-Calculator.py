#test cases
##########
expression = "2+3-999"
expression_2 = "2-(3-999)"
##########

'''
Given a string that represent an arithmetic operator with numbers and operators i.e "2+3-999". DO NOT INCLUDE parenthesis. Return the calculation result.
1.traverse expression
2.if minus sign then set the next number to negative
3.add all the number while travese
'''
def calcNoParen(expression):
    i,ans,sign=0,0,1
    len_=len(expression)
    while i < len_:
        if(expression[i].isdigit()):
            num = expression[i]
            while(i+1 < len_ and expression[i+1].isdigit() ):
                num+=expression[i+1]
                i+=1
            ans+=int(num)*sign
        
        elif(expression[i]=="+"):
            sign=1
            
        elif(expression[i]=="-"):
            sign=-1
        i+=1
    return ans
#print(calcNoParen(expression))

'''
Given a string that represent an arithmetic operator with numbers and operators i.e "2+3-999". INCLUDE parenthesis. Return the calculation result.
1.traverse expression
2.if minus sign then set the next number to negative
3.if ( then push the current calculated value to stack, then push the sign, start a new calculation and reset sign to 1
4.if ) then pop the sign to time with the current calculated value, then add with calculated value out side of the parenthesis
3.add operation for all number while travese
'''
def calcWithParen(expression):
    i,ans,sign=0,0,1
    stack = []
    len_=len(expression)
    while i < len_:
        if(expression[i].isdigit()):
            num = expression[i]
            while(i+1 < len_ and expression[i+1].isdigit() ):
                num+=expression[i+1]
                i+=1
            ans+=int(num)*sign
        elif(expression[i]=="+"):
            sign=1
        elif(expression[i]=="-"):
            sign=-1
        elif(expression[i]=="("):
            stack.append(ans)
            stack.append(sign)
            sign,ans=1,0
        elif(expression[i]==")"):
            ans = stack.pop()*ans +stack.pop()
        i+=1
    return ans

print(calcWithParen(expression_2))