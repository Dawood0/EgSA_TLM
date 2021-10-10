import time
import receive
import random
from TLM import read_tlm


x = input("Do you wanna receive packets? ")
if x == '1' :
    receiving = True 
elif x == '0' :
    receiving = False
    
while True:
    if receiving == True : 
        receiver = receive.Receiver()
        received = receiver.receive
        if  received[1] == True :
        # if True :
            try :  
                f = open('C:\\Users\\ahmed\\Downloads\\EgSA_TLM\\GUI\\packet2.txt','r')
                packet = f.read()
                print(packet)
                f.close()
                read_tlm(packet)
            except FileNotFoundError: 
                print("packet doens't exist")
                time.sleep(5)
    else : 
        try :  
            # f = open('C:\\Users\\ahmed\\Downloads\\EgSA_TLM\\GUI\\packet2.txt','r')
            # packet = f.read()
            # print(packet)
            # f.close()
            f = open('C:\\Users\\ahmed\\Downloads\\EgSA_TLM\\GUI\\packet.txt','r')
            packets = f.readlines()
            f.close()
            l = []
            for line_index in range(len(packets)) :
                i = random.randint(0,len(packets)-1)
                packet = packets[i][3:].strip('\n').replace(' ','')
                l.append(packet)
                read_tlm(packet)
                print(packet)
                time.sleep(5)
        except FileNotFoundError: 
            print("packets don't exist")
    
    

