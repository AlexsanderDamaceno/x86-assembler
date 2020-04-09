from operands import Register
from operands import Register
from operands import Decimal
from Instructions.sub import *
from elf  import *
from enum import Enum
import binascii
import struct
import operands
import binascii


class x86_opcode_options(Enum):
    Operands32 = 1
    Operands8  = 0


class x86_Mod_options(Enum):
  RegisterIndirect     = 0
  OneByteDisplacement  = 1
  FourByteDisplacement = 2
  RegisterAddress      = 3

class x86_Operand_size(Enum):
   Operands16 = 1
   Operands32 = 1
   Operands8  = 0

class x86_DirectionBit(Enum):
    RegtoRm    = 0
    RmtoReg    = 1

class x86_PrefixByte(Enum):
    Operand_16bits = 0x66

class CodeGenerate():

    def __init__(self , filename , statements):
         self.statements = statements
         self.filename   = open(filename + ".ge" , "wb")

    def writefile(self , instructionmachinecode):
        self.filename.write(instructionmachinecode)

    def closefile(self):
        self.filename.close()

    def printb(self, value):
        print("{0:b}".format(value))



    def  GenerateStatementCode(self, statement):
           mnemonic = statement.Get_mnemonic()


           if mnemonic[:len(mnemonic)-1] == 'sub':
                    operands      = statement.Get_Operands()
                    source        = operands[0]
                    destination   = operands[1]
                    print(source.Get_RegisterNumber())
                    if isinstance(source , Register) and isinstance(destination , Register):

                             prefix = -1

                             if mnemonic[-1] == 'w':
                                 prefix = 0x66


                             s            = source.Get_RegisterNumber()
                             d            = destination.Get_RegisterNumber()

                             if mnemonic[-1]   == 'l':
                               Operandsize  = x86_Operand_size.Operands32.value
                             elif mnemonic[-1] == 'w':
                               Operandsize  = x86_Operand_size.Operands16.value
                             elif mnemonic[-1] == 'b':
                               Operandsize  = x86_Operand_size.Operands8.value



                             directionbit = x86_DirectionBit.RegtoRm.value
                             mod          = x86_Mod_options.RegisterAddress.value
                             return bytearray(Sub(prefix , Operandsize , directionbit , mod ,  s , d).EncodeInstruction())

                    if isinstance(source , Decimal) and isinstance(destination , Register32):




                           return bytearray(machinecode) + source_number  # encode immediate






    def  GenerateMachineCode(self):
        machinecode = bytearray(0)
        for statement in self.statements:
             machinecode += self.GenerateStatementCode(statement)






        #ph = ProgramHeader(SegmentType.PT_LOAD, 0x00100054 )

        Ph = ProgramHeader(SegmentHeader.PT_LOAD , ELF_HEADER_SIZE + 32 , 0x00100054 , 0 ,len(machinecode) , len(machinecode) , 0x7 , 0x1000)
        Hd = Header(TypeFile.ET_EXEC)

        elf  = ElfFile(Hd , Ph , machinecode)
        r = elf.generateBytes()

        self.writefile(r)
        self.closefile()
