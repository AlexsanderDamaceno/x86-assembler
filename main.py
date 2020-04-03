from TokenTypes import TokenType
from Tokenizer import Tokenizer
from parser import Parser
from  operands import Register32
from generate import CodeGenerate


file = open("TESTE" , "r")

buffer  = file.read()

Parser     = Parser(buffer)


statements = Parser.parse()

Generator  = CodeGenerate("TESTE" , statements)


Generator.GenerateMachineCode()
