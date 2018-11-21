
def XOR (S1,S2):
    #function takes two strings and perform an XOR between their charachters
    
    result = ""
    for i in range(len(S1)):
        if S1[i] == S2[i]:
            result+='0'
        else:
            result+='1'
    return result

def verifier(transmitted_message,generator_key):
    
    key_length = len(generator_key)
    temp=transmitted_message[:key_length]
    transmitted_message = transmitted_message[key_length:]
    
    while len(transmitted_message) > 0:
        
        if temp[0] == '1':
            temp = XOR(temp,generator_key)+transmitted_message[0]
        else:
            temp = XOR('0'*key_length,temp)+transmitted_message[0]
        transmitted_message = transmitted_message[1:]
        temp = temp[1:]
    
    if temp[0] == '1':
        temp = XOR(temp,generator_key)
    else:
        temp = XOR('0'*key_length,temp)
        
    if int(temp) == 0:
        return "The message is correct"
    else:
        return "The message is not correct"
