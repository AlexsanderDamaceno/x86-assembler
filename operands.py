from TokenTypes import TokenType

registers_map32  = { "eax" : 0 , "ecx" : 1 , "edx": 2 ,  "ebx" : 3 , "esp" : 4 , "ebp"  : 5 ,  "esi" : 6 ,  "edi" : 7 }
registers_map16  = { "ax"  : 0 ,  "cx" : 1 , "dx" : 2 ,  "bx"  : 3 ,  "sp" : 4 ,  "bp"  : 5 ,  "si"  : 6 ,   "di" : 7 }
registers_map8   = { "al"  : 0 ,  "cl" : 1 , "dl" : 2 ,  "bl"  : 3 ,  "al" : 4 ,  "ch"  : 5 ,  "dh"  : 6 ,   "bh" : 7 }



class Register():
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
            return Register(value , registers_map32[value])
          elif value in registers_map16:
             return Register(value , registers_map16[value])
          elif value in registers_map8:
             return Register(value , registers_map8[value])

         elif  Type == TokenType.Decimal:
              return Decimal(value)
