import InstructionTable

class IntelInstruction2op():
    def __init__(self , Mnemonic ,  Operand16mode  , SizeType , DirectionBit , Mod , Reg , Rm):
        self.Operand16Mode = Operand16mode
        self.modrm_encode  = 0
        self.opcode        = InstructionTable.SelectOpcode(Mnemonic)
        self.SizeType      = SizeType
        self.DirectionBit  = DirectionBit
        self.Mod           = Mod
        self.Reg           = Reg
        self.Rm            = Rm

    def makePrefixBytes(self):
     if self.Operand16Mode != -1:
        return self.Operand16Mode
     else:
        return -1

    def makeOpcode(self):
       self.opcode = (self.opcode) | (self.DirectionBit) | self.SizeType << 0

       return self.opcode

    def modRM(self):
        self.modrm_encode = (self.Mod << 6) | (self.Reg  << 0) | (self.Rm << 0)
        return self.modrm_encode

    def EncodeInstruction(self):
        instruction  = []
        prefixbytes = self.makePrefixBytes()

        if prefixbytes != -1:
             instruction.append(prefixbytes)
        instruction.append(self.makeOpcode())
        instruction.append(self.modRM())

        return instruction

class IntelInstruction1op():
    def __init__(self , Mnemonic ,  Operand16mode , SizeType ,  Mod ,  operand ):
        self.Operand16Mode = Operand16mode
        self.modrm_encode  = 0
        self.opcode        = InstructionTable.SelectOpcode(Mnemonic)
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
