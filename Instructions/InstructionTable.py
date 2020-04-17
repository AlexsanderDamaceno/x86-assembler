from operands import *
# table for when instruction operands are both registers
instruction_table2OP = {
 "add" : 0x0 ,
 "and" : 0x20 ,
 "sub" : 0x28
}

instruction_table2OPImme = {
 "add" : 0x80 ,
 "and" : 0x20 ,
 "sub" : 0x28
}



instruction_table1OP = {
   "inc" : 0xFE
}


def SelectOpcode(mnemonic , Immediate):
     hasImmediate = 0
     if isinstance(Immediate , Number):
         hasImmediate = 1

     if   mnemonic in instruction_table2OP and  not hasImmediate:
          print(mnemonic)
          return instruction_table2OP[mnemonic]
     elif  mnemonic in instruction_table1OP and not hasImmediate:
          return instruction_table1OP[mnemonic]
     else:

          return instruction_table2OPImme[mnemonic]
