from TokenTypes import TokenType
from Token import Token

class Tokenizer():

    def __init__(self, filestream):
       self.filestream = filestream
       self.text_pos =  0


    def advance(self):
         self.text_pos += 1

    def lookahead(self):
     orig = self.text_pos
     Token = self.nextToken()
     self.text_pos = orig
     return Token



    def nextToken(self):
        if self.text_pos >= len(self.filestream) - 1:
             print("end of file")
             return  Token(TokenType.EOF , "EOF")

        while self.filestream[self.text_pos] == ' ':

            self.advance()

            if self.text_pos >= len(self.filestream) - 1:
                    return  Token(TokenType.EOF , "EOF")



        if self.filestream[self.text_pos].isalpha():

             name = ""

             while self.filestream[self.text_pos].isalpha():
                  name +=  self.filestream[self.text_pos]
                  self.advance()

             return Token(TokenType.Mnemonic , name)

        elif self.filestream[self.text_pos] == '%':

             self.advance()
             name = ""
             while self.filestream[self.text_pos].isalpha():
                  name +=  self.filestream[self.text_pos]
                  self.advance()
             return Token(TokenType.Register , name)

        elif  self.filestream[self.text_pos]  == ',':

            self.advance()
            return Token(TokenType.Colon , ',')

        elif self.filestream[self.text_pos] == '$':
            self.advance()
            number = ""
            while self.filestream[self.text_pos].isdigit():
               number += self.filestream[self.text_pos]
               self.advance()


            return Token(TokenType.Number ,  int(number))

        elif  self.filestream[self.text_pos] == '(':
                self.advance()
                return Token(TokenType.LPAREN , '(')

        elif  self.filestream[self.text_pos] == ')':
                    self.advance()
                    return Token(TokenType.RPAREN , ')')

        elif self.filestream[self.text_pos] == '-' or self.filestream[self.text_pos].isdigit():
                   val = ''
                   flag = 0
                   if self.filestream[self.text_pos] == '-':
                       flag = 1
                       self.advance()

                   while self.filestream[self.text_pos].isdigit():
                        val += self.filestream[self.text_pos]
                        self.advance()

                   if flag:
                        return Token(TokenType.Disp , -int(val))
                   else:
                       return Token(TokenType.Disp ,   int(val))



        elif  self.filestream[self.text_pos]  == '\n':

           self.advance()
           return Token(TokenType.NewLine , '\n')
