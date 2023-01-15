from enum import Enum

# class syntax
class LineType(Enum):
    GRID = "GRID"
    COMMENT = "$"
    BEGINBULK = "BEGIN BULK"
    CEND = "CEND"
    SOL = "SOL"
    PSOLID = "PSOLID"
    CTETRA = "CTETRA"
    CPENTA = "CPENTA"
    EIGRL = "EIGRL"
    ENDDATA = "ENDDATA"
    EMPTY = "EMPTY"
    
class MeshGrid():
    pass

class MeshReader():
    #self._lineTypeList= list()
    
    def __init__(self,fileName):
        self.ReadRawData(fileName)
        print(self.numberOfLines)
        self.GetLineTypes()
        #self.processRawData()
    
    
    def ReadRawData(self,fileName) -> None:
        """Read in the raw data"""
        with open(fileName) as fileHandle:
            Lines = fileHandle.readlines()
        self.rawData=Lines
        
    # def ProcessRawData(self) -> None:
    #     """Proces the Raw Data"""
    #     for line in self.rawData:
    #         currentLineType = self.getLineType(line)
    #         print(currentLineType)

    def GetLineTypes(self) -> None:
        """Make a list of the LineTypes"""
        
        # define the list
        self._lineTypeList = [None] * self.numberOfLines
        
        # fill the list
        for i, line in enumerate(self.rawData):
            self._lineTypeList[i]=self.getLineType(line)    
             
    @property
    def numberOfLines(self):
        """Get the number of lines in the file"""
        return len(self.rawData)
                
    def getLineType(self,line) -> LineType:
        """get the line Type"""
        if line.startswith(LineType.GRID.value):
            return LineType.GRID
        elif line.startswith(LineType.BEGINBULK.value):
            return LineType.BEGINBULK
        elif line.startswith(LineType.COMMENT.value):
            return LineType.COMMENT
        elif line.startswith(LineType.SOL.value):
            return LineType.SOL
        elif line.startswith(LineType.CEND.value):
            return LineType.CEND
        elif line.startswith(LineType.PSOLID.value):
            return LineType.PSOLID
        elif line.startswith(LineType.CTETRA.value):
            return LineType.CTETRA
        elif line.startswith(LineType.CPENTA.value):
            return LineType.CPENTA
        elif line.startswith(LineType.EIGRL.value):
            return LineType.EIGRL  
        elif line.startswith(LineType.ENDDATA.value):
            return LineType.ENDDATA      
        else:
            print("Unknown line")
            print(line)
            return  
        
          
        

def main():
    print("Hello World!")
    fileName="nastran_input.nas"
    mesh=MeshReader(fileName)


if __name__ == "__main__":
    main()
