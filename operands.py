from TokenTypes import TokenType

registers_map32  = {"eax" : 0 , "ecx" : 1}

class Register():
    def __init(self):
        pass

class Register32(Register):
      def __init__(self , name , intel_number):
        self.name = name
        self.intel_number = intel_number

      def Get_RegisterNumber(self):
          return  self.intel_number

class Decimal():
    def __init__(self ,  value):
        self.value  = value
    def Get_decimal(self):
        return self.value



class Operands():

    def __init__(self):
        pass

    def MakeOperand(self , Type , value):
         if Type == TokenType.Register:

          if value in registers_map32:
            return Register32(value , registers_map32[value])

         elif  Type == TokenType.Decimal:
              return Decimal(value)
