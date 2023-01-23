from enum import Enum
import numpy as np
from pytictoc import TicToc
import struct

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
    
    def __init__(self,fileName) -> None:
        timer = TicToc() #create instance of class
        
        timer.tic()
        self.ReadRawData(fileName)
        timer.toc("Read Raw Data")
        
        print(self.numberOfLines)

        print(self._CountEnumType(LineType.GRID))
        
        self.readGrid()

    def calculateArraySizeForString(self,tempLines,width) -> list:
        """Calculate the array size for a given delimation width"""
        width=8
        NOC=int(np.dtype(tempLines.dtype).itemsize/4)
        if (NOC % width) == 0:
            pass
        else:
            print(f"problems")
        arraySize=[np.size(tempLines),int(NOC/width)]
        return arraySize    
    
    def divideStringArrayFixedWidth(self,tempLines,width) -> np.ndarray:
        
        #Calculate the array size for a given delimation width
        arraySize=self.calculateArraySizeForString(tempLines,width)
        
        tempLines=np.array([string[i:i+width] for string in tempLines for i in range(0, len(string), width)], dtype='U8')
        tempLines=np.reshape(tempLines,arraySize)
        
        return tempLines
    
    def convertToFloat(self,tempGrid) -> np.ndarray:
        
        tempGrid = np.core.defchararray.replace(tempGrid, '-', 'e-')
        tempGrid = np.core.defchararray.replace(tempGrid, '+', 'e+')
        remove_e = lambda x: x if x[0]!='e' else x[1:]
        remove_e = np.vectorize(remove_e)
        tempGrid = remove_e(tempGrid)
        
        tempGrid=tempGrid.astype(float)
        
        return tempGrid
        
        
    def readGrid(self):
        # Get the grid lines
        tempLines = self.rawData[self.getLineTypes == LineType.GRID]
        
        # Divide the lines by fixed width
        width=8
        tempLines=self.divideStringArrayFixedWidth(tempLines,width)
        
        # Grid coordinates        
        tempGrid=tempLines[:,[3,4,5]]
        tempGrid=self.convertToFloat(tempGrid)
        
        # Element Numbers
        tempElementNumber=tempLines[:,[1]]
        tempElementNumber=tempElementNumber.astype(int)



        print(tempGrid)
        print(type(tempLines))
        
        
        #np.save("tempData.npy", tempLines)        
        #grid_number=np.empty(self.numberOfLines,dtype=int)
        #grid_coordinate=np.empty([self.numberOfLines,3],dtype=float)
        #for i, line in np.ndenumerate(tempLines):
        #    data = struct.unpack(format_string, line)
        
        
    def _CountEnumType(self,enumType):
        return np.count_nonzero(self.getLineTypes == enumType)

        

    # def ProcessRawData(self) -> None:
    #     """Proces the Raw Data"""
    #     for line in self.rawData:
    #         currentLineType = self.getLineType(line)
    #         print(currentLineType)

    @property
    def getLineTypes(self) -> list:
        """Make a list of the LineTypes"""

        # Check if variable has already been calculated
        if hasattr(self,'_lineTypeList'):
            return self._lineTypeList
        
        # define the list
        self._lineTypeList = np.empty(self.numberOfLines,dtype=LineType)
        
        # fill the list
        for i, line in np.ndenumerate(self.rawData):
            self._lineTypeList[i]=self.getLineType(line)    
        
                
        return self._lineTypeList
                      
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
        
    @property
    def numberOfLines(self) -> int:
        """Get the number of lines in the file"""
        return len(self.rawData)
        
    def ReadRawData(self,fileName) -> None:
        """Read in the raw data"""
        with open(fileName) as fileHandle:
            Lines = fileHandle.readlines()
        self.rawData=np.array(Lines)
        
        # Remove new line charcter from strings
        self.rawData=np.core.defchararray.replace(self.rawData,"\n",'', count=None)
        
          
        

def main():
    print("Hello World!")
    fileName="nastran_input.nas"
    mesh=MeshReader(fileName)


if __name__ == "__main__":
    main()
