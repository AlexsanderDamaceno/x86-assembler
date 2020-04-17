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


             # source have adress displacement
               if Token.Get_Token_Type() == TokenType.Disp:

                    disp  = Token.Get_Token_value()
                    Token = self.Tokenizer.nextToken()
                    Token.match(TokenType.LPAREN)
                    Token = self.Tokenizer.nextToken()

                    operand = self.operand.MakeOperand(Token.Get_Token_Type() , Token.Get_Token_value())
                    operands.append(Address(operand , disp))
                    Token = self.Tokenizer.nextToken()
                    Token.match(TokenType.RPAREN)




               elif Token.Get_Token_Type() == TokenType.LPAREN:

                     Token = self.Tokenizer.nextToken()
                     operand = self.operand.MakeOperand(Token.Get_Token_Type() , Token.Get_Token_value())
                     operands.append(Address(operand , None))
                     Token = self.Tokenizer.nextToken()
                     Token.match(TokenType.RPAREN)

               elif  Token.Get_Token_Type() == TokenType.Register or Token.Get_Token_Type() == TokenType.Number:
                     Token.match(TokenType.Register , TokenType.Number)
                     operands.append(self.operand.MakeOperand(Token.Get_Token_Type() , Token.Get_Token_value()))


                     if self.Tokenizer.lookahead().Get_Token_Type() == TokenType.NewLine:
                         statements.append(Intruction(opcode , operands))
                         self.Tokenizer.nextToken()
                         continue
                     if self.Tokenizer.lookahead().Get_Token_Type() == TokenType.EOF:
                          statements.append(Intruction(opcode , operands))
                          self.Tokenizer.nextToken()
                          break




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
