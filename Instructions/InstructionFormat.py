from  Instructions.InstructionTable  import *
from  TokenTypes import *
from  operands import *
from instructions_op import *
import binascii 
import struct


Operandssize = {'b' : x86_Operand_size.Operands8.value , 'w' : x86_Operand_size.Operands16.value , 'l' : x86_Operand_size.Operands32.value}

def prefix(suffix):
    if suffix == 'w':
      return 1 
    return 0 


def  chooseDirectionBit(source_type , destination_type):
       if isinstance(source_type  , Register) and isinstance(destination_type , Register): 
           return x86_DirectionBit.RegtoRm.value
       if isinstance(source_type  , Number) and isinstance(destination_type , Register): 
           return 0

def determineopsize(suffix):
    return Operandssize.get(suffix)
       

def make2opcode(mnemonic , suffix , source_type  ,  destination_type):
      opcode = 0
    
      if isinstance(source_type  , Register) and isinstance(destination_type , Register): 
          opcode = instruction_table2OP[mnemonic] | chooseDirectionBit(source_type  , destination_type) << 1 | determineopsize(suffix)
      elif isinstance(source_type  , Number) and isinstance(destination_type , Register): 
          DirectionBit = 0
          opcode = instruction_table2OPImme[mnemonic] | DirectionBit << 1 | determineopsize(suffix)  
      
      by = bytearray()
      by.append(opcode)
      return by

def makeImmediate(source , suffix): 
      if suffix == 'b': 
          return  struct.pack('<b' , source.Get_Number())
      if suffix == 'w': 
          return  struct.pack('<h' , source.Get_Number())
      if suffix == 'l': 
          return  struct.pack('<i' , source.Get_Number())

def makemod_rm2(source , destination , suffix):
      if isinstance(source  , Register) and isinstance(destination, Register): 
        modrm = x86_Mod_options.RegisterAddress.value << 6 |  source.Get_RegisterNumber() << 3 | destination.Get_RegisterNumber()
        return  modrm
      if isinstance(source  , Number) and isinstance(destination, Register): 

         reg    = 0
        
         modrm = bytearray()
      
         modrm.append(x86_Mod_options.RegisterAddress.value << 6 |  reg  << 3 | destination.Get_RegisterNumber())

         return modrm + makeImmediate(source , suffix)



def debug(instruction):
     print binascii.hexlify(instruction)

def encode2op(mnemonic , source , destination): 
      instruction  = bytearray()
     
      if prefix(mnemonic[len(mnemonic)-1:]):
         instruction.append(x86_PrefixByte.Operand_16bits.value)

      instruction.extend(make2opcode(mnemonic[:len(mnemonic)-1] ,  mnemonic[len(mnemonic)-1:] , source , destination))
      instruction.extend(makemod_rm2(source , destination ,  mnemonic[len(mnemonic)-1]))
      return instruction

    





    
