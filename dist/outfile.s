lui $1 4097
ori $1 $8 0
lui $1 4097
ori $1 $13 48
addiu $0 $10 1
sll $17 $4 0
sw $10 0($8)
sw $10 4($8)
addi $13 $9 65534
add $10 $11 $12
sw $10 8($8)
addi $8 $8 4
addi $9 $9 65535
bgtz $9 65529
lui $1 4097
ori $1 $4 0
add $5 $0 $13
jal 1048599
addiu $0 $2 10
syscall

add $8 $0 $4
add $9 $0 $5
lui $1 4097
ori $1 $4 54
addiu $0 $2 4
syscall

addiu $0 $2 1
syscall

lui $1 4097
ori $1 $4 52
addiu $0 $2 4
syscall

addi $8 $8 4
addi $9 $9 65535
bgtz $9 65526
jr $31
