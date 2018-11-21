
import generator,alter,verifier
import time


def getDataFromFile(file_address):
    myfile = open(file_address,'r')
    data = myfile.readline()
    gen = myfile.readline()
    myfile.close()
    data=data[0:-len('\r\n')+1]
    return data,gen

def addDataToFile(trans_m):
    my_file = open("transmitted_message.txt",'w')
    my_file.write(trans_m)
    my_file.close()


def greeting_message():
    time.sleep(1)
    print("hello there!",end="\n")
    time.sleep(1)
    print("please select the way of inputting the message and generator key!",end="\n")
    time.sleep(1)
    print("if command line choose 1!",end="\n")
    time.sleep(1)
    print("else if file choose 2!",end="\n")
    time.sleep(1)
    choice = input("your choice?\n")
    time.sleep(1)
    print("please select if you choose to use alter or not!",end="\n")
    time.sleep(1)
    print("if you will use alter type \"yes\"!",end="\n")
    time.sleep(0.5)
    print("else if not using alter type \"no\"!",end="\n")
    time.sleep(1)
    alter = input("your choice?\n")
    pos = -1
    if(alter.lower()=="yes"):
        pos = int(input("which bit to do alter on?\n"))
    else:
        pos = -1
    #way = input("Enetr the way of work (with alter or not)!\n")
    #time.sleep(1)
    return choice,pos
    #return way




def main():
    
    choice,alter_pos = greeting_message()
    
    if(choice == "2"):
        file_address = input("type the address of your file!\n")
        data_str,gen_str=getDataFromFile(file_address)
    elif(choice == "1"):
        data_str = input("enter the data message!\n")
        gen_str = input("enter the generator key!\n")
    else :
        print("wrong choice please try again!")
        choice,alter_pos = greeting_message()

    transmitted_data = ""
    verified_data = ""

    if(alter_pos == -1):
       transmitted_data = generator.generate(data_str,gen_str)
       addDataToFile(transmitted_data)
       verified_data = verifier.verifier(transmitted_data,gen_str)
       print(verified_data,end="\n")
       #print (int("5"))

    elif(alter_pos != -1):
        transmitted_data = generator.generate(data_str,gen_str)
        addDataToFile(transmitted_data)
        altered_transmitted_data = alter.alter(transmitted_data,alter_pos)
        verified_data = verifier.verifier(altered_transmitted_data,gen_str)
        print(verified_data,end="\n")


    #print(way)
    #print("Transmited data :",transmitted_data)
    #print("verified data :",verified_data)
    #print("alter :",alter.alter(gen_str,2))
    
    

if __name__=="__main__":
    main()