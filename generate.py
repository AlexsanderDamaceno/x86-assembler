import operands
from operands import Register32
from operands import Register

class CodeGenerate():

    def __init__(self , filename , statements):
         self.statements = statements
         self.filename   = open(filename + ".ge" , "wb")

    def writefile(self , instructionmachinecode):
        self.filename.write(instructionmachinecode)

    def closefile(self):
        self.filename.close()

    def  GenerateStatementCode(self, statement):
           mnemonic = statement.Get_mnemonic()

           if mnemonic == 'add':
                    machinecode = []
                    modrm = 0

                    operands  = statement.Get_Operands()
                    source        = operands[0]
                    destination   = operands[1]

                    if isinstance(source , Register) and isinstance(destination , Register):

                           mod = 3 # mod code for Register
                           source_number      = source.Get_RegisterNumber()

                           destination_number = destination.Get_RegisterNumber()

                           modrm = (mod << 6) | (source_number << 0) | (destination_number << 0)
                           print(modrm)

                           if isinstance(source , Register32) and isinstance(destination , Register32):
                               operandtype = 1

                           directionbit = 0
                           opcode =  statement.Get_IntelCode(mnemonic) | (directionbit << 1)  | operandtype << 0

                           machinecode.append(opcode)
                           machinecode.append(modrm)


                    return bytearray(machinecode)

    def  GenerateMachineCode(self):
        for statement in self.statements:
             machinecode = self.GenerateStatementCode(statement)
             print(machinecode)
             self.writefile(machinecode)
        self.closefile()
