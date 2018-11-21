def xor(x,y):
    result =[]
    for i in range(len(y)):
        if(x[i]==y[i]):
            result.append("0")
        else :
            result.append("1")
    return "".join(result)



def alter(str_,argu_):
    operand2 = []
    for i in range(len(str_)):
        if(i==argu_-1):
            operand2.append("1")
        else:
            operand2.append("0")
    str2_="".join(operand2)
    return xor(str_,str2_)
