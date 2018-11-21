def xor(x,y):
    # Return string that calcualtes xor of two binary strings
    result =[]
    for i in range(len(y)):
        if(x[i]==y[i]):
            result.append("0")
        else :
            result.append("1")
    return "".join(result)
        


def generate(d,g):
    d=d + "0"*(len(g)-1)
    x1=0 #boundary for the data bits to xor it with the gen or zeroes 
    x2=len(g)
    # operand1 = int(d[0:x2],2)
    operand1 = d[0:x2]
    operand2 = g
    # remainder = xor(d[0:x2],operand2)[1:] + d[x2]
    while(1):
        remainder = xor(operand1,operand2)[1:] + d[x2] # in bin 3 to negelect the first bit and in d we add the next bit
        operand1 = remainder
        x2+=1
        x1+=1
        if(remainder[0] == "0"):
            operand2 = "0"*len(g)
        elif(remainder[0] == "1"):
            operand2 = g
        if(x2 == len(d)):
            break
        
    
    return d[:len(d)-len(g)] + xor(d[len(d)-len(g):len(d)] , remainder)