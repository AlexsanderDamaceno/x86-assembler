from enum import Enum
import struct

# http://www.skyfree.org/linux/references/ELF_Format.pdf format specification

ELF_HEADER_SIZE = 52


class ELFCLASSTYPE(Enum):
    ELFCLASSNONE = 0
    ELFCLASS32   = 1
    ELFCLASS64   = 2

class ELFDATA(Enum):
    ELFDATANONE = 0
    ELFDATA2LSB = 1
    ELFDATA2MSB = 2

class E_VERSION(Enum):
    EV_CURRENT = 1

class Arch(Enum):
    EM_386 = 3

class TypeFile(Enum):
    ET_NONE = 0
    ET_REL  = 1
    ET_EXEC = 2
    ET_DYN  = 3
    ET_CORE = 4
    ET_LOPROC = 0xff00
    ET_HIPROC = 0xffff

class SegmentHeader(Enum):
    PT_LOAD = 1

class Header():
   def __init__(self , type):
    self.e_ident     = [0x7f , 'E' , 'L' , 'F' , ELFCLASSTYPE.ELFCLASS32.value , ELFDATA.ELFDATA2LSB.value , E_VERSION.EV_CURRENT.value , 0 , 0 , 0, 0 , 0,0 , 0 , 0 , 0] # magic number
    self.e_type      = type.value
    self.e_version   = E_VERSION.EV_CURRENT.value
    self.e_machine   = Arch.EM_386.value
    self.e_entry     = 0x00100054
    self.e_phoff     = ELF_HEADER_SIZE
    self.e_shoff     = 0
    self.e_flags     = 0
    self.e_ehsize    = ELF_HEADER_SIZE
    self.e_phentsize = 32
    self.e_phnum     = 1
    self.e_shentsize = 40
    self.e_shnum     = 0
    self.e_shstrndx  = 0

   def generateBytes(self):
     v = self.e_ident

     value_ident  = struct.pack("bcccbbbbbbbbbbbb" , *v)

     value1 = struct.pack("<hhiiiii" , self.e_type , self.e_machine , self.e_version ,self.e_entry , self.e_phoff , 0 , self.e_flags)

     value2 = struct.pack("<hhhhhh" , self.e_ehsize , self.e_phentsize , self.e_phnum ,
     40 , self.e_shnum , self.e_shstrndx)

     return value_ident + value1 + value2



class SegmentType():
    def __int__(self):
        self.value = 0

class ProgramHeader():

    def __init__(self, type , offset , vaddr , paddr , filesz , memsz , flags , align):
        self.type       =  SegmentType()
        self.type.value =  type.value
        self.offset     =  offset
        self.vaddr      =  vaddr
        self.paddr      =  paddr
        self.filesz     =  filesz
        self.memsz      =  memsz
        self.flags      =  flags
        self.align      =  align

    def generateBytes(self):
        bytes = struct.pack('<' + 'i'* 8 , self.type.value , self.offset , self.vaddr , self.paddr , self.filesz , self.memsz , self.flags , self.align)
        return bytes



class ElfFile():
    def __init__(self, Header , ProgramHeader ,  data):
          self.Header = Header
          self.ProgramHeader = ProgramHeader
          self.data = data
    def generateBytes(self):
        print(len(self.ProgramHeader.generateBytes()))
        return  self.Header.generateBytes() + self.ProgramHeader.generateBytes() + self.data
