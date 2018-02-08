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
infile = input("Input a machine file: ")
mach_infile = open(infile, 'r')

# open output file
outfile = open("outfile.s", "w")


line_count = 0  # count each line

for line in mach_infile:  # for each line . . .
    #outfile.write("Line #: %d" % int(line_count + 1))

    opCode = findOp(line)

    if opCode is 0 or opCode is 17:

        rs = findRS(line)
        rt = findRT(line)
        rd = findRD(line)
        sft = findShamt(line)
        fct = findFunct(line)

        #outfile.write("Type R - opCode: %d, rs: %d, rt: %d, rd: %d, shift: %d, funct: %d" % (opCode, rs, rt, rd, sft, fct))
        if fct is 0:
            outfile.write("sll $%d $%d %d\n" % (rs, rt, sft))
        if fct is 2:
            outfile.write("srl $%d $%d %d\n" % (rs, rt, sft))
        if fct is 3:
            outfile.write("sra $%d $%d %d\n" % (rd, rt, sft))
        if fct is 4:
            outfile.write("sllv $%d $%d %d\n" % (rd, rt, rs))
        if fct is 6:
            outfile.write("srlv $%d $%d %d\n" % (rd, rt, rs))
        if fct is 7:
            outfile.write("srav $%d $%d %d\n" % (rd, rt, rs))
        if fct is 8:
            outfile.write("jr $%d\n" % rs)
        if fct is 9 and rd is not 31:
            outfile.write("jalr $%d $%d\n" % (rd, rs))
        if fct is 9 and rd is 31:
            outfile.write("jalr $%d\n" % rs)
        if fct is 12:
            outfile.write("syscall\n\n")
        if fct is 16:
            outfile.write("mfhi $%d\n" % rd)
        if fct is 17:
            outfile.write("mthi $%d\n" % rs)
        if fct is 18:
            outfile.write("mflo $%d\n" % rd)
        if fct is 19:
            outfile.write("mtlo $%d\n" % rs)
        if fct is 24:
            outfile.write("mult $%d $%d\n" % (rs, rt))
        if fct is 25:
            outfile.write("multu $%d $%d\n" % (rs, rt))
        if fct is 26:
            outfile.write("div $%d $%d\n" % (rs, rt))
        if fct is 27:
            outfile.write("divu $%d $%d\n" % (rs, rt))
        if fct is 32:
            outfile.write("add $%d $%d $%d\n" % (rd, rs, rt))
        if fct is 33:
            outfile.write("addu $%d $%d $%d\n" % (rd, rs, rt))
        if fct is 34:
            outfile.write("sub $%d $%d $%d\n" % (rd, rs, rt))
        if fct is 35:
            outfile.write("subu $%d $%d $%d\n" % (rd, rs, rt))
        if fct is 36:
            outfile.write("and $%d $%d $%d\n" % (rd, rs, rt))
        if fct is 37:
            outfile.write("or $%d $%d $%d\n" % (rd, rs, rt))
        if fct is 38:
            outfile.write("xor $%d $%d $%d\n" % (rd, rs, rt))
        if fct is 39:
            outfile.write("nor $%d $%d $%d\n" % (rd, rs, rt))
        if fct is 42:
            outfile.write("slt $%d $%d $%d\n" % (rd, rs, rt))
        if fct is 43:
            outfile.write("sltu $%d $%d $%d\n" % (rd, rs, rt))


    elif opCode is 2 or opCode is 3:

        psuedoAddr = findJAddr(line)

        if opCode is 2:
            outfile.write("j %d\n" % psuedoAddr)
        else:
            outfile.write("jal %d\n" % psuedoAddr)

    else:

        rs = findRS(line)
        rt = findRT(line)
        iMM = findImm(line)

        #outfile.write("Type I - opCode: %d, rs: %d, rt: %d, imm: %d" % (opCode, rs, rt, iMM))

        if opCode is 4:
            outfile.write("beq $%d $%d %d\n" % (rs, rt, iMM))
        if opCode is 5:
            outfile.write("bne $%d $%d %d\n" % (rs, rt, iMM))
        if opCode is 6:
            outfile.write("blez $%d %d\n" % (rs, iMM))
        if opCode is 7:
            outfile.write("bgtz $%d %d\n" % (rs, iMM))
        if opCode is 8:
            outfile.write("addi $%d $%d %d\n" % (rs, rt, iMM))
        if opCode is 9:
            outfile.write("addiu $%d $%d %d\n" % (rs, rt, iMM))
        if opCode is 10:
            outfile.write("stli $%d $%d %d\n" % (rs, rt, iMM))
        if opCode is 11:
            outfile.write("stliu $%d $%d %d\n" % (rs, rt, iMM))
        if opCode is 12:
            outfile.write("andi $%d $%d %d\n" % (rs, rt, iMM))
        if opCode is 13:
            outfile.write("ori $%d $%d %d\n" % (rs, rt, iMM))
        if opCode is 14:
            outfile.write("xor $%d $%d %d\n" % (rt, rs, iMM))
        if opCode is 15:
            outfile.write("lui $%d %d\n" % (rt, iMM))
        if opCode is 32:
            outfile.write("lb $%d %d($%d)\n" % (rt, iMM, rs))
        if opCode is 33:
            outfile.write("lh $%d %d($%d)\n" % (rt, iMM, rs))
        if opCode is 34:
            outfile.write("lw $%d %d($%d)\n" % (rt, iMM, rs))
        if opCode is 36:
            outfile.write("lbu $%d %d($%d)\n" % (rt, iMM, rs))
        if opCode is 37:
            outfile.write("lhu $%d %d($%d)\n" % (rt, iMM, rs))
        if opCode is 40:
            outfile.write("sb $%d %d($%d)\n" % (rt, iMM, rs))
        if opCode is 41:
            outfile.write("sh $%d %d($%d)\n" % (rt, iMM, rs))
        if opCode is 43:
            outfile.write("sw $%d %d($%d)\n" % (rt, iMM, rs))

    line_count += 1