from  Instructions.InstructionTable  import *
from  operands import *
import struct
class IntelInstruction2op():
    def __init__(self , Mnemonic ,  Operand16mode  , SizeType , DirectionBit , Mod , Reg , Rm  , disp):
        self.Operand16Mode = Operand16mode
        self.modrm_encode  = 0
        self.opcode        = SelectOpcode(Mnemonic , Reg)
        self.SizeType      = SizeType
        self.DirectionBit  = DirectionBit
        self.Mod           = Mod
        self.Reg           = Reg
        self.Rm            = Rm
        self.disp          = disp

    def makePrefixBytes(self):
     if self.Operand16Mode != -1:
        return self.Operand16Mode
     else:
        return -1

    def makeOpcode(self):
       self.opcode = (self.opcode) | (self.DirectionBit << 1) | (self.SizeType << 0)

       return self.opcode

    def modRM(self):
        print(self.Rm)
        self.modrm_encode = (self.Mod << 6) | (self.Reg  << 3) | (self.Rm << 0)
        return self.modrm_encode
    def Makedisp(self):

        return struct.pack('<h' ,self.disp)

    def EncodeImmediate(self , number):
         if  self.SizeType == 0:
             return struct.pack('<b' , number)
         elif self.SizeType == 1 and self.Operand16Mode != -1:
             return struct.pack('<h' , number)
         else:
             return struct.pack('<i' , number)



    def EncodeInstruction(self):
        instruction  = []
        prefixbytes = self.makePrefixBytes()
        Immediate = None

        if isinstance(self.Reg , Number):
             Immediate =  self.EncodeImmediate(self.Reg.Get_Number())
             self.Reg = 0

        if prefixbytes != -1:
             instruction.append(prefixbytes)


        instruction.append(self.makeOpcode())
        instruction.append(self.modRM())
        if  self.disp != None:
             return bytearray(instruction) +  self.Makedisp()
        elif Immediate != None:
           print("afd")
           return bytearray(instruction) + Immediate

        return bytearray(instruction)

class IntelInstruction1op():
    def __init__(self , Mnemonic ,  Operand16mode , SizeType ,  Mod ,  operand ):
        self.Operand16Mode = Operand16mode
        self.modrm_encode  = 0
        self.opcode        = SelectOpcode(Mnemonic)
        self.SizeType      = SizeType
        self.Mod           = Mod
        self.reg           = 0
        self.operand       = operand
        self.DirectionBit  = 0

    def makePrefixBytes(self):
         if self.Operand16Mode != -1:
            return self.Operand16Mode
         else:
            return -1
    def makeOpcode(self):
           self.opcode = (self.opcode) | (self.DirectionBit) | self.SizeType << 0

           return self.opcode

    def modRM(self):

        self.modrm_encode = (self.Mod << 6) | (self.reg << 3) | (self.operand << 0)
        return self.modrm_encode

    def EncodeInstruction(self):
        instruction  = []
        prefixbytes  =  self.makePrefixBytes()

        if prefixbytes != -1:
           instruction.append(prefixbytes)

        instruction.append(self.makeOpcode())
        instruction.append(self.modRM())

        return instruction
