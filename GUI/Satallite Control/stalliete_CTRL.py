import json

import os
az="\\".join(os.getcwd().split("\\")[:-2])
json_file = json.load(open('{}\\test.json'.format(az)))
commands_front = (open('{}\\txt_files\\commands.txt'.format(az)).read()).split(',')

pkt_ver = '000'
pkt_type = '0'
sec_hdr_flg = '1'
seq_flg = '11'
pkt_data_len = '{0:016b}'.format(3)

def increment(binary):
    if len(binary) == 0:
        return binary

    if binary[-1] == '0':
        binary = binary[:-1] + '1'
    else:
        binary = increment(binary[:-1]) + '0'

    return binary

def commands(command):
    opcode = json_file[str(command)]['opcode']
    apid = json_file[str(command)]['vaip']
    return opcode, apid

def packet(x,y):
    pkt_name = "00000000000000" #sequence for the packages from 1 to 2^14
    list_package = []
    for command in commands_front:
        if command == 'getimage':
            opcode,apid = commands(command)
            package = "%s%s%s%s%s%s%s%s%s%s"%(pkt_type,pkt_ver,sec_hdr_flg,apid,seq_flg,pkt_name,pkt_data_len,opcode,'{0:08b}'.format(x),'{0:08b}'.format(y))
            pkt_name = increment(pkt_name)
            list_package.append(package)
        else:
            opcode,apid = commands(command)
            package = "%s%s%s%s%s%s%s%s"%(pkt_type,pkt_ver,sec_hdr_flg,apid,seq_flg,pkt_name,pkt_data_len,opcode)
            pkt_name = increment(pkt_name)
            list_package.append(package)
    return list_package

def text_file(packet):
    increment = 0
    tot=""
    import os
    newPath = os.path.join("\\".join(os.getcwd().split("\\")[:-2]), "txt_files")

    with open(newPath + "\\encode.txt", "w") as f:

        # f.write("")
        for pac in packet:
            tot+=str(increment)+' '+str(pac)+'\n'
            f.write(str(increment)+' '+str(pac)+'\n')
            increment+=1
    return tot


x=text_file(packet(2,3))
print(x)