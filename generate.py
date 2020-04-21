from operands import *
from Instructions.InstrutionFormat import *
from elf  import *
from enum import Enum
import binascii
import struct
import operands
import binascii



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

    def verify_source(self, source):
        if isinstance(source , Register) or isinstance(source , Address) or isinstance(source , Number):
               return 1
        return 0

    def verify_destination(self, destination):
        if isinstance(destination , Register) or isinstance(destination , Address):
               return 1
        return 0



    def  GenerateStatementCode(self, statement):

                    mnemonic = statement.Get_mnemonic()
                    operands      = statement.Get_Operands()

                    source        = operands[0]
                    if len(operands) >= 2:
                      destination   = operands[1]

                    if len(operands) == 2:


                     if  self.verify_source(source) and self.verify_destination(destination):
                              return bytes(encode2op(mnemonic , source , destination))




    def  GenerateMachineCode(self):
        machinecode = bytearray()
        for statement in self.statements:
             machinecode += self.GenerateStatementCode(statement)






        #ph = ProgramHeader(SegmentType.PT_LOAD, 0x00100054 )

        Ph = ProgramHeader(SegmentHeader.PT_LOAD , ELF_HEADER_SIZE + 32 , 0x00100054 , 0 ,len(machinecode) , len(machinecode) , 0x7 , 0x1000)
        Hd = Header(TypeFile.ET_EXEC)

        elf  = ElfFile(Hd , Ph , machinecode)
        r = elf.generateBytes()

        self.writefile(r)
        self.closefile()
