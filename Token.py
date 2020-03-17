import sys
class Token():

   def __init__(self, TokenType ,  value):
       self.TokenType = TokenType
       self.value     = value

   def Get_Token_Type(self):
        return self.TokenType

   def Get_Token_value(self):
        return self.value

   def match(self ,  TokenType):

       if self.TokenType != TokenType:
             print("Error  parsing the statement exptect {} but got {}".format(TokenType , self.TokenType))
             sys.exit(1)
