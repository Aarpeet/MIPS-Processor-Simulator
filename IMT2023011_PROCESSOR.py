def working(ml):
    main_memory = {}
    for line in ml:
        s = line.split()
        main_memory[s[0]] = s[1]
    line = ml[0].split()
    PC = line[0]
    IR = '0'
    MAR = '0'
    IBR = '0'
    MBR = '0'
    MQ = '0'
    AC = '0'


    k =0
    #main_memory['000000110011']+= (bin(int(main_memory['000000110011'],2)+1))[2:]
    while(IR != "11110000"):
        
        print()
        print("FETCH CYCLE BEGINS")
        print()
        print("PC: ",PC)
        MAR = PC
        print("MAR: ",MAR)
        MBR = main_memory[MAR]
        print("MBR: ",MBR)
        IBR = MBR[20:40]
        print("IBR: ",IBR)
        IR = MBR[0:8]
        print("IR: ",IR)
        MAR = MBR[8:20]
        print("MAR: ",MAR)
        print()
        print('FETCH CYCLE ENDS')
        i =0
        while(i<2):            
            print()
            print("DECODE AND EXECUTE PART")
            print()
            if (IR == '00000001'): #LOAD
                print()
                print("LOAD")
                print()
                MBR = main_memory[MAR]
                print('MBR: ',int(MBR,2))
                AC = MBR
                print("AC: ",int(AC,2))

            if (IR == '00010010'): #STOR
                print()
                print("STOR")
                print()
                MBR = AC
                print("MBR: ",int(MBR,2))
                main_memory[MAR] = MBR
                print(MAR,int(main_memory[MAR],2))
            
            if (IR == '00000110'): #SUB
                print()
                print("SUB")
                print()
                MBR = main_memory[MAR]
                print("MBR: ",int(MBR,2))
                AC = str((bin(int(AC,2) - int(MBR,2)))[2:])
                print("AC: ",int(AC,2))
            
            if (IR == '11111111'): #INR
                print()
                print("INR")
                print()
                main_memory['000000111110'] = AC
                AC = main_memory[MAR]
                print("AC: ",AC)
                AC = str((bin(int(main_memory[MAR],2) + 1)[2:]))
                print("AC: ",AC)
                main_memory[MAR] = AC
                print(MAR," ",main_memory[MAR])
                AC = main_memory['000000111110']
                print("AC: ",AC)

            if (IR == '00000101'): #ADD
                print()
                print("ADD")
                print()
                MBR = main_memory[MAR]
                print("MBR: ",int(MBR,2))
                AC = str((bin(int(AC,2) + int(MBR,2)))[2:])
                print("AC: ",int(AC,2))
            
            if (IR == '00001100'): #DIV
                print()
                print("DIV")
                print()
                MBR = main_memory[MAR]
                print("MBR: ",MBR)
                print("AC: ",AC)
                MQ = str((bin(int(AC,2)//int(MBR,2)))[2:])
                AC = str((bin(int(AC,2)%int(MBR,2)))[2:])
                print("MQ: ",int(MQ,2))
                print("AC: ",int(AC,2))
                main_memory['000001000000'] = MQ
            
            if (IR == '11000000'): #LOAD MQ
                print()
                print("MQ")
                print()
                AC = MQ
                print("AC: ",AC)
            
            if (IR == '11111110'): #ANI
                print()
                print("ANI")
                print()
                AC = str(int(AC,2) | 0)
                print("AC: ",AC)
            
            if (IR == '11110000'): #END
                print()
                print("END")
                print()
                return MQ
            
            if (IR == '00001111'): #JUMP-
               
                if (int(AC,2)<=0):
                    print()
                    print("JUMP-")
                    print()
                    print("PC: ",PC)
                    print("MAR: ",MAR)
                    PC = (str(bin(int(MAR,2))[2:]).zfill(12))
                    print("PC: ",PC)
                    PC = PC[4:12]
                    IR  = main_memory[MAR][20:28]
                    MAR = main_memory[MAR][28:40]
                    continue
               
            if  (IR == '00001101'): #JUMP
                print()
                print("JUMP")
                print()
                PC = str((bin(int(MAR,2))[2:]).zfill(12))
                print('PC: ',PC)
                i+=1
                PC = PC[4:12]
                IR =  main_memory[MAR][20:28]
                print("MAR: ",MAR)
                MAR = main_memory[MAR][28:40]
                print("MAR: ",MAR)
                continue

            if (IR == '00000111'): #DCR
                print()
                print("DCR")
                print()
                main_memory['000000111111'] = AC
                AC = main_memory[MAR]
                print("AC: ",AC)
                AC = str((bin(int(main_memory[MAR],2) - 1)[2:]))
                print("AC: ",AC)
                main_memory[MAR] = AC
                print(MAR," ",main_memory[MAR])
                AC = main_memory['000000111111']
                print("AC: ",AC)

            
            i+=1
            IR  = IBR[0:8]
            print("IR: ",IR)
            MAR = IBR[8:20]
            print("MAR: ",MAR)

        PC = str(bin(int(PC,2) + 1)[2:].zfill(12))

        k+=1



file_path = r"C:\Users\Bhavya Jain\OneDrive\Desktop\Python\test.txt"
with open(file_path, 'r') as file:
    ml = file.readlines()
MQ = working(ml)
print(int(MQ,2))