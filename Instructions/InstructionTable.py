
# table for when instruction operands are both registers
instruction_table2OP = {
 "add" : 0x0 ,
 "and" : 0x20 ,
 "sub" : 0x28
}

instruction_table1OP = {
   "inc" : 0xFE
}


def SelectOpcode(mnemonic):
     if   mnemonic in instruction_table2OP:
          print(mnemonic)
          return instruction_table2OP[mnemonic]
     elif  mnemonic in instruction_table1OP:
          return instruction_table1OP[mnemonic]
