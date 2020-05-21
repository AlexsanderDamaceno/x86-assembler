from  Instructions.InstructionTable  import *
from  TokenTypes import *
from  operands import *
from instructions_op import *
import binascii
import struct


Operandssize = {'b' : x86_Operand_size.Operands8.value , 'w' : x86_Operand_size.Operands16.value , 'l' : x86_Operand_size.Operands32.value}

Dispvalue    = {'b' : x86_Mod_options.OneByteDisplacement.value , 'w' : x86_Mod_options.FourByteDisplacement.value , 'l' : x86_Mod_options.FourByteDisplacement.value}

Scale        = {1 : SibByteoptions.OneScale.value, 2  : SibByteoptions.TwoScale.value , 4 : SibByteoptions.FourScale.value  , 8 : SibByteoptions.EightScale.value }

Immediatereg = {'add'  : 0 ,
                'sub'  : 5 ,
                'mov'  : 0 ,
                'xor'  : 6 ,
                'test' : 0 ,
                'shr'  : 5}

NoDirectionBit = {'cmpxchg' : 0}

SpecialOpcode = {'cmpxchg' : 0x0f}

MemoryDirec =  {    'sub'     : 1 ,
                    'test'    : 0 ,
                    'xchg'    : 1 ,
                    'xor'     : 1 ,
                    'add'     : 1 ,
                    'and'     : 1 ,
                    'cmp'     : 1 ,
                    'cmpxchg' : 1 ,
                    'shr'     : 0
                  }

def prefix(suffix):
    if suffix == 'w':
      return 1
    return 0


def  chooseDirectionBit(mnemonic , source_type , destination_type):
       if NoDirectionBit.get(mnemonic):
         return NoDirectionBit[mnemonic]

       if isinstance(source_type  , Register) and isinstance(destination_type , Register):
           return x86_DirectionBit.RegtoRm.value
       if isinstance(source_type  , Number) and isinstance(destination_type , Register):
           return 0

def determineopsize(suffix):
    return Operandssize.get(suffix)


def make2opcode(mnemonic , suffix , source_type  ,  destination_type):
      opcode = 0x0



      if isinstance(source_type  , Register) and isinstance(destination_type , Register):
          opcode = instruction_table2OP[mnemonic] | chooseDirectionBit(mnemonic , source_type  , destination_type) << 1 | determineopsize(suffix)
      elif isinstance(source_type  , Number) and isinstance(destination_type , Register):
          DirectionBit = 0
          opcode = instruction_table2OPImme[mnemonic] | DirectionBit << 1 | determineopsize(suffix)
      elif isinstance(source_type  , Address) and isinstance(destination_type , Register):
          DirectionBit = MemoryDirec.get(mnemonic[:len(mnemonic)])
          opcode = instruction_table2OP[mnemonic] | DirectionBit << 1 | determineopsize(suffix)


      by = bytearray()
      by.append(opcode)
      debug(by)
      return by

def makeImmediateorDisp(source , suffix):
      if suffix == 'b':
          return  struct.pack('<b' , source.Get_Number())
      if suffix == 'w':
          return  struct.pack('<h' , source.Get_Number())
      if suffix == 'l':
          return  struct.pack('<i' , source.Get_Number())

def MakeDisp(source , suffix):
      if suffix == 'b':
          return  struct.pack('<b' , source.Get_Disp())
      if suffix == 'l' or suffix == 'w':
          return  struct.pack('<i' , source.Get_Disp())


def makemod_rm2(mnemonic , source , destination , suffix):
      if isinstance(source  , Register) and isinstance(destination, Register):
        modrm = bytearray()
        modrm.append(x86_Mod_options.RegisterAddress.value << 6 |  source.Get_RegisterNumber()  << 3 | destination.Get_RegisterNumber())

        return  modrm

      if isinstance(source  , Number) and isinstance(destination, Register):
         reg    = Immediatereg[mnemonic]
         modrm = bytearray()
         modrm.append(x86_Mod_options.RegisterAddress.value << 6 |  reg  << 3 | destination.Get_RegisterNumber())
         return modrm + makeImmediateorDisp(source , suffix)

      if isinstance(source , Address) and  isinstance(destination , Register):


         if source.Get_base() != None and source.Get_indexreg() != None and source.Get_scale() != None:

            modrm_sib = bytearray()
            sib = SibByteoptions.Sibbyte.value

            modrm_sib.append(x86_Mod_options.RegisterIndirect.value << 6 |  destination.Get_RegisterNumber()  << 3 | sib)
            scaleop = Scale.get(source.Get_scale())
            modrm_sib.append(scaleop << 6 |  source.Get_indexreg()  << 3 | source.Get_base())
            return modrm_sib


         elif source.Get_Disp() == None:

            modrm = bytearray()
            modrm.append(x86_Mod_options.RegisterIndirect.value << 6 |  destination.Get_RegisterNumber()  << 3 | source.Get_base())
            return modrm
         elif source.Get_Disp() != None:
            modrm = bytearray()
            modfield = Dispvalue.get(suffix)


            modrm.append(modfield << 6 |  destination.Get_RegisterNumber()  << 3 | source.Get_base())

            return modrm + MakeDisp(source , suffix)






def debug(instruction):
     print(binascii.hexlify(instruction))




def encode2op(mnemonic , source , destination):

      ins_suffix = ['l' , 'b' , 'w']

      instruction  = bytearray()

      # if not given the suffix assume 32 bit instruction
      if  not mnemonic[len(mnemonic)-1:] in  ins_suffix:
           mnemonic += 'l'


      if prefix(mnemonic[len(mnemonic)-1:]):
         instruction.append(x86_PrefixByte.Operand_16bits.value)

      if SpecialOpcode.get(mnemonic[:len(mnemonic)-1]):
          instruction.append(SpecialOpcode[mnemonic[:len(mnemonic)-1]])


      instruction.extend(make2opcode(mnemonic[:len(mnemonic)-1] ,  mnemonic[len(mnemonic)-1:] , source , destination))
      instruction.extend(makemod_rm2(mnemonic[:len(mnemonic)-1], source , destination ,  mnemonic[len(mnemonic)-1]))
      debug(instruction)
      return instruction
