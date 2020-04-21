from enum import Enum

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