from Tokenizer   import Tokenizer
from TokenTypes  import TokenType
from operands    import *
from Instruction import Intruction

class Parser():

   def __init__(self , Filebuffer):
       self.File  = Filebuffer
       self.Tokenizer = Tokenizer(Filebuffer)
       self.operand  = Operands()
   def parse(self):

       statements = []

       while 1:

           Token     = self.Tokenizer.nextToken()


           if  Token.Get_Token_Type() ==   TokenType.EOF:
               break






           if  Token.Get_Token_Type() ==  TokenType.Mnemonic:
             # statement -> mnemonic (%register | $decimal) , %register
               operands = []

               opcode = Token.Get_Token_value()

               Token  = self.Tokenizer.nextToken()

             # source can be Register or Decimal
               if Token.Get_Token_Type() == TokenType.LPAREN:
                     Token = self.Tokenizer.nextToken()
                     operand = self.operand.MakeOperand(Token.Get_Token_Type() , Token.Get_Token_value())
                     operands.append(Address(operand))
                     Token = self.Tokenizer.nextToken()
                     Token.match(TokenType.RPAREN)

               else:
                     Token.match(TokenType.Register , TokenType.Decimal)
                     operands.append(self.operand.MakeOperand(Token.Get_Token_Type() , Token.Get_Token_value()))

               Token = self.Tokenizer.nextToken()
               Token.match(TokenType.Colon)

               Token = self.Tokenizer.nextToken()
               Token.match(TokenType.Register)
               operands.append(self.operand.MakeOperand(Token.Get_Token_Type() , Token.Get_Token_value()))


               Token = self.Tokenizer.nextToken()

               statements.append(Intruction(opcode , operands))

               if  Token.Get_Token_Type() == TokenType.EOF:
                    break

               Token.match(TokenType.NewLine)


       return statements
