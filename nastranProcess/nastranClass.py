import pickle

from .rawDataClass import RawData
from .gridClass import Grid
from .lineTypeClass import LineType



class ReadFile():
    
    def __init__(self, fileName) -> None:
        print("read nastran from file")
        self.fileName = fileName
        
        self.rawData = RawData().read(fileName)
        
        file = open('tempData.dat', 'wb')
        pickle.dump(self, file)
        file.close()
        
        self.grid = Grid().convert(self.rawData)
       
        print(self.rawData.display())
        print(self.rawData.numberOfLines)
        print(self.rawData.CountEnumType(LineType.GRID))
        


    

    

