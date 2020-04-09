class Sub():
    def __init__(self , Operand16mode  , SizeType , DirectionBit , Mod , Reg , Rm):
        self.Operand16Mode = Operand16mode
        self.modrm_encode  = 0
        self.opcode        = 0x28
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
       print(hex(self.opcode))
       return self.opcode

    def modRM(self):
        self.modrm_encode = (self.Mod << 6) | (self.Reg  << 0) | (self.Rm << 0)
        return self.modrm_encode

    def EncodeInstruction(self):
        instruction  = []
        r = self.makePrefixBytes()
        if r != -1:
             instruction.append(r)
        instruction.append(self.makeOpcode())
        instruction.append(self.modRM())
        return instruction

class Sub32_ImReg():
    def __init__(self , SizeType , DirectionBit , Mod , Reg , Rm):

        self.prefix        = 0
        self.modrm_encode  = 0
        self.opcode        = 0x29
        self.SizeType      = SizeType
        self.DirectionBit  = DirectionBit
        self.Mod           = Mod
        self.Reg           = Reg
        self.Rm            = Rm

    def modRM(self):
        self.modrm_encode = (self.Mod << 6) | (self.Reg  << 0) | (self.Rm << 0)
        return self.modrm_encode

    def EncodeInstruction(self):
        instruction  = []
        instruction.append(self.makePrefixBytes())
        instruction.append(self.opcode)
        instruction.append(self.modRM())
        return instruction
