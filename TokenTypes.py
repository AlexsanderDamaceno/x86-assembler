from enum import Enum


class TokenType(Enum):
 Mnemonic = 1
 Register = 2
 Colon    = 3
 NewLine  = 4
 Decimal  = 5
 LPAREN   = 6
 RPAREN   = 7
 EOF = 8
