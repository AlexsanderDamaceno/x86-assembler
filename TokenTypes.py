from enum import Enum


class TokenType(Enum):
 Mnemonic = 1
 Register = 2
 Comma    = 3
 NewLine  = 4
 Number   = 5
 LPAREN   = 6
 RPAREN   = 7
 Disp     = 8
 Colon    = 9
 EOF = 11
