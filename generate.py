import operands
from operands import Register32
from operands import Register
from operands import Decimal
from elf  import *
import binascii
import struct
from enum import Enum


class x86_opcode_options(Enum):
    Operands32 = 1
    Operands8  = 0

    RegtoRm    = 0
    RmtoReg    = 1

class X86_Mod_options(Enum)





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

    def modrm(self , mod , source , destination):
        modrm_encode = (mod << 6) | (source << 0) | (destination << 0)
        return modrm_encode

    def encode_opcode(self ,  instr_number  ,  mnemonic , directionbit  , operandsize):
        opcode =  instr_number  | (directionbit << 1)  | operandtype
        return opcode


    def  GenerateStatementCode(self, statement):
           mnemonic = statement.Get_mnemonic()

           if mnemonic == 'add':

                    machinecode = []
                    modrm = 0

                    operands      = statement.Get_Operands()
                    source        = operands[0]
                    destination   = operands[1]



                    if isinstance(source , Register) and isinstance(destination , Register):

                           mod = 3 # mod code for Register



                           if isinstance(source , Register32) and isinstance(destination , Register32):
                             machinecode.append(self.encode_opcode(statement , mnemonic , x86_opcode_options.RegtoRm , x86_opcode_options.Operands32))
                             machinecode.append(self.modrm(mod , source.Get_RegisterNumber()  ,  destination.Get_RegisterNumber()))
                             return bytearray(machinecode)

                    if isinstance(source , Decimal) and isinstance(destination , Register32):
                           mod = 3
                           source_number        =  struct.pack("<i" , source.Get_decimal())
                           destination_register =  destination.Get_RegisterNumber()

                           reg = 0
                           modrm = (mod << 6) | (reg << 0) | destination_register

                           directionbit = 0
                           const = 1

                           opcode =   0x80 | (directionbit << 1) | (const << 0)

                           machinecode.append(self.encode_opcode(statement , 0x80 , x86_opcode_options.RmtoReg ,  x86_opcode_options.Operands32)
                           machinecode.append(modrm)



                           return bytearray(machinecode) + source_number  # encode immediate






    def  GenerateMachineCode(self):
        machinecode = bytearray(0)
        for statement in self.statements:
             machinecode += self.GenerateStatementCode(statement)





        #ph = ProgramHeader(SegmentType.PT_LOAD, 0x00100054 )

        Ph = ProgramHeader(SegmentHeader.PT_LOAD , ELF_HEADER_SIZE + 32 , 0x00100054 , 0 ,len(machinecode) , len(machinecode) , 0x7 , 0x1000);
        Hd = Header(TypeFile.ET_EXEC)

        elf  = ElfFile(Hd , Ph , machinecode)
        r = elf.generateBytes()

        self.writefile(r)
        self.closefile()
