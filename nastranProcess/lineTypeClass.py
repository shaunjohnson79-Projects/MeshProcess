from enum import Enum

# class syntax


class LineType(Enum):
    GRID = "GRID"
    COMMENT = "$"
    BEGINBULK = "BEGIN BULK"
    CEND = "CEND"
    SOL = "SOL"
    PSOLID = "PSOLID"
    CTRIA3 = "CTRIA3"
    CTETRA = "CTETRA"
    CPENTA = "CPENTA"
    EIGRL = "EIGRL"
    ENDDATA = "ENDDATA"
    EMPTY = "EMPTY"
    PSHELL = "PSHELL"
    CORD2R = "CORD2R"
    META = "METADATA"
    PLUS = "+"
    STAR = "*"


class MeshNOE(Enum):
    CTETRA = "4"
    CPENTA = "6"
    CTRIA3 = "3"
