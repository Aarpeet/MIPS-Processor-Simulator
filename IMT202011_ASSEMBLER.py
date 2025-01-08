def assembly_code(assembly):

    assembly_dic = {
        'LOAD': '00000001',
        'STOR': '00010010',
        'SUB': '00000110',
        'JUMP-': '00001111',
        'INR' : '11111111',
        'ADD': '00000101',
        'JUMP': '00001101',
        'DIV': '00001100',
        'LOAD MQ': '11000000',
        'ANI': '11111110',
        'END\n' : '11110000',
        'DCR' : '00000111'
    }

    
    machine_code = []
    
    for line in assembly:
        s = line.split(' ')
        opcode1 = ""
        opcode2 = ""
        mm1 = ""
        mm2 = ""
        add = ""
        if(len(s)>2):
            for i in range(0,len(s)):
                if (i == 0):
                    add = (bin(int(s[0]))[2:]).zfill(12)
                if(i ==1):
                    if(s[i] == "END\n"):
                        opcode1 = assembly_dic[s[1]]
                        opcode2 = "00000000" 
                        mm1 = '000000000000'
                        mm2 = '000000000000'
                        break
                    else:
                        opcode1 = assembly_dic[s[i]]
                if(i ==2):
                    if s[i] == "ZERO":
                        mm1 = '000000000000'
                    elif s[i] == "MQ\n":
                        mm1 = '110000000000'
                        opcode1 = '11000000'
                    else:
                        if s[1] == "JUMP" or s[1] == "JUMP-":
                            mm1 = (bin(int(s[i][2:5]))[2:]).zfill(12)
                        else:
                            mm1 = (bin(int(s[i][2:4]))[2:]).zfill(12)
                if(i==3):
                    if(s[i] == "END\n"):
                        opcode2 = assembly_dic[s[i]]
                        mm2 = '000000000000'
                        break
                    else:
                        opcode2 = assembly_dic[s[i]]
                if(i == 4):
                    if s[i] == "ZERO":
                        mm2 = '000000000000'
                    else:
                        if s[i-1] == "JUMP" or s[i-1] == "JUMP-":
                            mm2 = (bin(int(s[i][2:5]))[2:]).zfill(12) 
                        elif s[i] == "MQ\n":
                            mm2 = '110000000000'
                            opcode2 = '11000000'
                        else:
                            mm2 = (bin(int(s[i][2:4]))[2:]).zfill(12)
            machine_code.append(add + " " + opcode1 +  mm1 +  opcode2  + mm2 + "\n")
        
        else:
            machine_code.append((bin(int(s[0]))[2:]).zfill(12) +" " +  (bin(int(s[1]))[2:]).zfill(12) + "\n")


    return machine_code

file_path = r"C:\Users\Bhavya Jain\OneDrive\Desktop\Python\code1.txt"
with open(file_path, 'r') as file:
    assembly = file.readlines()
machine_code = assembly_code(assembly)
for code in machine_code:
    print(code)
file_pathw = r"C:\Users\Bhavya Jain\OneDrive\Desktop\Python\test.txt"
with open(file_pathw,'w') as filew:
    filew.writelines(machine_code)
# ANI ZERO 
# STOR M(60)
# STOR M(61)
# SUB M(51)
# STOR M(50)
# JUMP+ M(14,0:19)
# LOAD M(60)
# INR M(61)
# ADD M(61)
# STOR M(60)
# INR M(50)
# LOAD M(50)
# JUMP M(6,0:19)
# LOAD M(60)
# DIV M(50)
# LOAD MQ
# STOR M(50)