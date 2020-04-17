from enum import Enum


class TokenType(Enum):
 Mnemonic = 1
 Register = 2
 Colon    = 3
 NewLine  = 4
 Number   = 5
 LPAREN   = 6
 RPAREN   = 7
 Disp     = 8
 EOF = 9
