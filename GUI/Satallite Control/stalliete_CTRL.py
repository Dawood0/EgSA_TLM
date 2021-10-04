import json
import sys
import os
import mysql.connector
import bitstring

az="\\".join(os.getcwd().split("\\")[:-2])

json_file = json.load(open('{}\\commands.json'.format(az)))
commands_front = (open('{}\\txt_files\\commands.txt'.format(az)).read()).split(',')

sub_json = json.load(open(f'{az}\\subsystems.json'))
subsystem = open(f'{az}\\txt_files\\sub.txt').read()

ground = '10'
pkt_ver = '000'
pkt_type = '0'
sec_hdr_flg = '1'
seq_flg = '11'
pkt_data_len = '{0:072b}'.format(3)

subsys = []

def Targets():
    print("Connecting to the DataBase...")
    mydb = mysql.connector.connect(
       # host="153.92.220.1",
       host="sql514.main-hosting.eu",
       user="u952728553_egsa",
       password="Egsa1234",
       database="u952728553_egsa"
    )
    print("CONNECTED SUCESSFULLY")
    targets = []
    targets_table = mydb.cursor()
    targets_table.execute("SELECT x_axis, y_axis FROM targets")
    myresult = targets_table.fetchall()
    for coor in myresult:
        targets.append(coor)
    return targets

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

def packet(sat):
    pkt_name = "00000000000000" #sequence for the packages from 1 to 2^14
    list_package = []
    for command in commands_front:
        print("Sending the Space packets....")
        if command == 'getImage':
            opcode,apid = commands(command)
            for coord in Targets():
                print("Sending the Space packets....")
                x,y = coord
                package = "%s%s%s%s%s%s%s%s%s%s%s%s"%(pkt_type,pkt_ver,sec_hdr_flg,ground,sat,apid,seq_flg,pkt_name,pkt_data_len,opcode,bitstring.BitArray(float=x, length=32).bin,bitstring.BitArray(float=y, length=32).bin)
                pkt_name = increment(pkt_name)
                list_package.append(package)

        elif command == 'getTLM':
            print("Sending the Space packets....")
            if subsystem in sub_json:
                opcode,apid = commands(command)
                sub_id = sub_json[subsystem]
                package = "%s%s%s%s%s%s%s%s%s%s"%(pkt_type,pkt_ver,sec_hdr_flg,ground,sat,sub_id,seq_flg,pkt_name,pkt_data_len,opcode)
                pkt_name = increment(pkt_name)
                list_package.append(package)
        else:
            print("Sending the Space packets....")
            opcode,apid = commands(command)
            package = "%s%s%s%s%s%s%s%s%s%s"%(pkt_type,pkt_ver,sec_hdr_flg,ground,sat,apid,seq_flg,pkt_name,pkt_data_len,opcode)
            pkt_name = increment(pkt_name)
            list_package.append(package)
    return list_package

def text_file(packet):
    increment = 0
    tot=""
    import os
    newPath = os.path.join("\\".join(os.getcwd().split("\\")[:-1]), "txt_files")
    with open(newPath + "\\encode.txt", "w") as f:
        for pac in packet:
            tot+=str(pac)+'\n'
            f.write(str(pac)+'\n')
    return tot

text_file(packet("01"))
print("The Space packets has been sent.")
print("FINISED SUCCESSFULLY")
