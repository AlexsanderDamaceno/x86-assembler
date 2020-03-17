from Tokenizer   import Tokenizer
from TokenTypes  import TokenType
from operands    import Operands
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

           if  Token.Get_Token_Type() ==  TokenType.Name:
               operands = []
               print('d')
               opcode = Token.Get_Token_value()

               Token  = self.Tokenizer.nextToken()
               Token.match(TokenType.Register)
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
