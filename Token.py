import sys

class Token():

   def __init__(self, TokenType ,  value):
       self.TokenType = TokenType
       self.value     = value

   def Get_Token_Type(self):
        return self.TokenType

   def Get_Token_value(self):
        return self.value

   def match(self ,  *Args):

       for TokenType in Args:
         if self.Get_Token_Type() == TokenType:
             return 1
       print("Error  parsing the statement expect {} but got {}".format(Args , self.TokenType))
       sys.exit(1)
