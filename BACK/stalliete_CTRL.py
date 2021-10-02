import json
from bitarray import bitarray

json_file = json.load(open('../test.json'))
commands_front = (open('../txt_files/commands.txt').read()).split(',')

pkt_ver = '000'
pkt_type = '0'
sec_hdr_flg = '1'
seq_flg = '11'
pkt_data_len = '2'

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
            package = bytes("%s%s%s%s%s%s%s%s%s%s"%(pkt_type,pkt_ver,sec_hdr_flg,apid,seq_flg,pkt_name,pkt_data_len,opcode,x,y),'utf-8')
            pkt_name = increment(pkt_name)
            list_package.append(package)
        else:
            opcode,apid = commands(command)
            package = bytes("%s%s%s%s%s%s%s%s"%(pkt_type,pkt_ver,sec_hdr_flg,apid,seq_flg,pkt_name,pkt_data_len,opcode),'utf-8')
            pkt_name = increment(pkt_name)
            list_package.append(package)
    return list_package
