
Instructions_CodeTable = {"add" : 0}

class Intruction():
    def __init__(self , mnemonic , operands):
        self.mnemonic   = mnemonic
        self.operands = operands
    def Get_mnemonic(self):
        return self.mnemonic
    def Get_Operands(self):
        return self.operands

    def Get_IntelCode(self , mnemonic):
        return Instructions_CodeTable[mnemonic]
