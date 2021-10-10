

def read_tlm(packet):
    import json

    print('READ_TLM')


    subs = {
    '0000001': 'Comm',
    '0000010': 'ADCS',
    '0000011': 'OBC',
    '0000100': 'Power',
    '0000101': 'Payload',
    '0000110': 'broadcast' }
    
    try:       
        f = open("C:\\Users\\ahmed\\Downloads\\EgSA_TLM\\GUI\\tlm.json",)
        dictt  = json.load(f)
        f.close()
    except FileNotFoundError :
        dictt = {"sat1" :  {"ADCS": {"num": 0, "data": {"gyro": [0], "accelerometer": [0], "temp" : '00'}},
                "Payload": {"num": 0, "data": {"status": "OFF", "temp":'00'}},
                "Comm":    {"num": 0, "data": {"status": "OFF", "temp":'00'}},
                "OBC":     {"num": 0, "data": {"status": "OFF", "temp":'00'}},
                "Power":   {"num": 0, "data": {"status": "OFF", "temp":'00'}}},
                 
                "sat2":    {"ADCS": {"num": 0, "data": {"gyro": [0], "accelerometer": [0], "temp" : '00'}},
                "Payload": {"num": 0, "data": {"status": "OFF", "temp":'00'}},
                "Comm":    {"num": 0, "data": {"status": "OFF", "temp":'00'}},
                "OBC":     {"num": 0, "data": {"status": "OFF", "temp":'00'}},
                "Power":   {"num": 0, "data": {"status": "OFF", "temp":'00'}}}
                }  
        

    try :
        avip = packet[9:16]
        subsystem = subs[avip]
        print(avip, subsystem)
        
    except KeyError:   
        print("Can't detect AVIP bits")
    try :
        packet[47+8]
    except IndexError :
        print("The packet data must be at least one byte")
        # raise
        # sys.exit(1)
        return 0
            
    sats = {'0':'sat1', '1':'sat2'}
    status = {'0':'OFF', '1':'ON'}
    sat_num = packet[8]
    sat = sats[sat_num]
    print(sat)
    data = packet[48:]
    
    try:
        # print(subsystem)
        # print(sat)       
        # print(sat == 'sat1')
        # print(dictt)
        print("increment")
        print(dictt[sat][subsystem]['num'])
        dictt[sat][subsystem]['num']+=1
        print(dictt[sat][subsystem])
        # print("try")
        # print(dictt[sat][subsystem]['num'])
    
    except KeyError :
        print(f"{subsystem} PAID is unknown in dictionary.")
        
    if subsystem == 'ADCS' :
        try :
            dictt[sat][subsystem]['data']['gyro'] = [int(data[0*8:1*8],2),int(data[1*8:2*8],2),int(data[2*8:3*8],2)] 
            dictt[sat][subsystem]['data']['accelerometer'] = [int(data[3*8:4*8],2),int(data[4*8:5*8],2),int(data[5*8:6*8],2)] 
            print(str(int(data[6*8:7*8],2)))
            dictt[sat][subsystem]['data']['temp'] = int(data[6*8:7*8],2)
            # dictt[sat][subsystem]['data']['statlite-angle'] = [int(data[7*8:8*8],2),int(data[8*8:9*8],2),int(data[9*8:10*8],2)] 
        except IndexError:
            print("The given packet for ADCS is missing data")
    elif subsystem == 'Payload' :
        try :        
            dictt[sat][subsystem]['data']['status'] = status[data[0]]
            # dictt[sat][subsystem]['data']['mode'] = data[1:1+8]
            dictt[sat][subsystem]['data']['temp'] = int(data[8:8+8],2) 
        except IndexError:
            print("The given packet for ADCS is missing data")           
    elif subsystem == 'Comm' :
        try : 
            dictt[sat][subsystem]['data']['status'] = status[data[0]]
            dictt[sat][subsystem]['data']['temp'] = int(data[8:8+8],2) 
        except IndexError:
            print("The given packet for ADCS is missing data")
    elif subsystem == 'OBC' :
        try :
            dictt[sat][subsystem]['data']['status'] = status[data[0]]
            dictt[sat][subsystem]['data']['temp'] = int(data[8:8+8],2) 
        except IndexError:
            print("The given packet for ADCS is missing data")
    elif subsystem == 'Power' :
        try :
            dictt[sat][subsystem]['data']['status'] = status[data[0]]
            dictt[sat][subsystem]['data']['temp'] = int(data[8:8+8],2)        
        except IndexError:
            print("The given packet for ADCS is missing data")

    a_file = open("C:\\Users\\ahmed\\Downloads\\EgSA_TLM\\GUI\\tlm.json", "w")
    json.dump(dictt, a_file)
    a_file.close()
    return dictt
    
    
# read_tlm(packet)


    # f = open("C:\\Users\\ahmed\\Downloads\\EgSA_TLM-main\\EgSA_TLM-main\\Back-end\\tlm.json",)
    
    # data  = json.load(f)
    
    # dictt['subsystem']['num']+=1
    # if 'subsystem':
    #     pass
    # a_file = open("C:\\Users\\ahmed\\Downloads\\EgSA_TLM-main\\EgSA_TLM-main\\Back-end\\tlm.json", "w")
    # json.dump(dictt, a_file)
    # a_file.close()
    
    # print(data['ADCS'])

    # data['ADCS']['num']+=1
    # a_file = open("C:\\Users\\ahmed\\Downloads\\EgSA_TLM-main\\EgSA_TLM-main\\Back-end\\tlm.json", "w")
    # json.dump(data, a_file)
    # a_file.close()
    





# f = open("tlm.json",)

# data  = json.load(f)

# print(data)





# =============================================================================
# packet = bytes('0000100000000011110000000000000020111','utf-8')
# l = []
# for byte in packet:
#     # print(bin(byte-48), end=' ')
#     l.append(f'{(byte-48):0>8b}')
#     print(f'{(byte-48):0>8b}', end=' ')
#     # print(i)
#     # if i == 2:
# 
#     # (f'{byte:0>8b}')
#     
# =============================================================================



