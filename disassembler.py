def findOp(aLine):
    length = 5
    i = 0
    sum = 0
    while i <= length:
        sum += int(aLine[i]) * (2 ** (length - i))
        i += 1
    return sum


def findRS(aLine):
    shift = 6
    length = 4
    i = 0
    sum = 0
    while i <= length:
        sum += int(aLine[i + shift]) * (2 ** (length - i))
        i += 1
    return sum


def findRT(aLine):
    shift = 11
    length = 4
    i = 0
    sum = 0
    while i <= length:
        sum += int(aLine[i + shift]) * (2 ** (length - i))
        i += 1
    return sum


def findRD(aLine):
    shift = 16
    length = 4
    i = 0
    sum = 0
    while i <= length:
        sum += int(aLine[i + shift]) * (2 ** (length - i))
        i += 1
    return sum


def findShamt(aLine):
    shift = 21
    length = 4
    i = 0
    sum = 0
    while i <= length:
        sum += int(aLine[i + shift]) * (2 ** (length - i))
        i += 1
    return sum


def findFunct(aLine):
    shift = 26
    length = 5
    i = 0
    sum = 0
    while i <= length:
        sum += int(aLine[i + shift]) * (2 ** (length - i))
        i += 1
    return sum


def findImm(aLine):
    shift = 16
    length = 15
    i = 0
    sum = 0
    while i <= length:
        sum += int(aLine[i + shift]) * (2 ** (length - i))
        i += 1
    return sum


def findJAddr(aLine):
    shift = 6
    length = 25
    i = 0
    sum = 0
    while i <= length:
        sum += int(aLine[i + shift]) * (2 ** (length - i))
        i += 1
    return sum


# grab a machine file
file = input("Input a machine file: ")
mach_file = open(file, 'r')

line_count = 0  # count each line

for line in mach_file:  # for each line . . .
    #print("Line #: %d" % int(line_count + 1))

    opCode = findOp(line)

    if opCode is 0 or opCode is 17:

        rs = findRS(line)
        rt = findRT(line)
        rd = findRD(line)
        sft = findShamt(line)
        fct = findFunct(line)

        #print("Type R - opCode: %d, rs: %d, rt: %d, rd: %d, shift: %d, funct: %d" % (opCode, rs, rt, rd, sft, fct))
        if fct is 0:
            print("sll $%d $%d %d" % (rs, rt, sft))
        if fct is 2:
            print("srl $%d $%d %d" % (rs, rt, sft))
        if fct is 3:
            print("sra $%d $%d %d" % (rd, rt, sft))
        if fct is 4:
            print("sllv $%d $%d %d" % (rd, rt, rs))
        if fct is 6:
            print("srlv $%d $%d %d" % (rd, rt, rs))
        if fct is 7:
            print("srav $%d $%d %d" % (rd, rt, rs))
        if fct is 8:
            print("jr $%d" % rs)
        if fct is 9 and rd is not 31:
            print("jalr $%d $%d" % (rd, rs))
        if fct is 9 and rd is 31:
            print("jalr $%d" % rs)
        if fct is 12:
            print("syscall")
        if fct is 16:
            print("mfhi $%d" % rd)
        if fct is 17:
            print("mthi $%d" % rs)
        if fct is 18:
            print("mflo $%d" % rd)
        if fct is 19:
            print("mtlo $%d" % rs)
        if fct is 24:
            print("mult $%d $%d" % (rs, rt))
        if fct is 25:
            print("multu $%d $%d" % (rs, rt))
        if fct is 26:
            print("div $%d $%d" % (rs, rt))
        if fct is 27:
            print("divu $%d $%d" % (rs, rt))
        if fct is 32:
            print("add $%d $%d $%d" % (rd, rs, rt))
        if fct is 33:
            print("addu $%d $%d $%d" % (rd, rs, rt))
        if fct is 34:
            print("sub $%d $%d $%d" % (rd, rs, rt))
        if fct is 35:
            print("subu $%d $%d $%d" % (rd, rs, rt))
        if fct is 36:
            print("and $%d $%d $%d" % (rd, rs, rt))
        if fct is 37:
            print("or $%d $%d $%d" % (rd, rs, rt))
        if fct is 38:
            print("xor $%d $%d $%d" % (rd, rs, rt))
        if fct is 39:
            print("nor $%d $%d $%d" % (rd, rs, rt))
        if fct is 42:
            print("slt $%d $%d $%d" % (rd, rs, rt))
        if fct is 43:
            print("sltu $%d $%d $%d" % (rd, rs, rt))


    elif opCode is 2 or opCode is 3:

        psuedoAddr = findJAddr(line)

        if opCode is 2:
            print("j %d" % psuedoAddr)
        else:
            print("jal %d" % psuedoAddr)

    else:

        rs = findRS(line)
        rt = findRT(line)
        iMM = findImm(line)

        #print("Type I - opCode: %d, rs: %d, rt: %d, imm: %d" % (opCode, rs, rt, iMM))

        if opCode is 4:
            print("beq $%d $%d %d" % (rs, rt, iMM))
        if opCode is 5:
            print("bne $%d $%d %d" % (rs, rt, iMM))
        if opCode is 6:
            print("blez $%d %d" % (rs, iMM))
        if opCode is 7:
            print("bgtz $%d %d" % (rs, iMM))
        if opCode is 8:
            print("addi $%d $%d %d" % (rs, rt, iMM))
        if opCode is 9:
            print("addiu $%d $%d %d" % (rs, rt, iMM))
        if opCode is 10:
            print("stli $%d $%d %d" % (rs, rt, iMM))
        if opCode is 11:
            print("stliu $%d $%d %d" % (rs, rt, iMM))
        if opCode is 12:
            print("andi $%d $%d %d" % (rs, rt, iMM))
        if opCode is 13:
            print("ori $%d $%d %d" % (rs, rt, iMM))
        if opCode is 14:
            print("xor $%d $%d %d" % (rt, rs, iMM))
        if opCode is 15:
            print("lui $%d %d" % (rt, iMM))
        if opCode is 32:
            print("lb $%d %d($%d)" % (rt, iMM, rs))
        if opCode is 33:
            print("lh $%d %d($%d)" % (rt, iMM, rs))
        if opCode is 34:
            print("lw $%d %d($%d)" % (rt, iMM, rs))
        if opCode is 36:
            print("lbu $%d %d($%d)" % (rt, iMM, rs))
        if opCode is 37:
            print("lhu $%d %d($%d)" % (rt, iMM, rs))
        if opCode is 40:
            print("sb $%d %d($%d)" % (rt, iMM, rs))
        if opCode is 41:
            print("sh $%d %d($%d)" % (rt, iMM, rs))
        if opCode is 43:
            print("sw $%d %d($%d)" % (rt, iMM, rs))

    line_count += 1