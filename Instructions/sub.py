


class Sub32():



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
        instruction.append(self.opcode)
        instruction.append(self.modRM())
        return instruction
