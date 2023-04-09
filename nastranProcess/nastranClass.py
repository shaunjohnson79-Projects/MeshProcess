import pickle

from .rawDataClass import RawData
from .gridClass import Grid
from .meshClass import Mesh
from .lineTypeClass import LineType



class ReadFile():
    
    def __init__(self, fileName) -> None:
        print("read nastran from file")
        self.fileName = fileName
        
        self.rawData = RawData().read(fileName)
        self.grid = Grid().convert(self.rawData)
        self.mesh = Mesh().convert(self.rawData)
        
       
        #print(self.rawData.display())
        #print(self.rawData.numberOfLines)
        #print(self.rawData.CountEnumType(LineType.GRID))
        

        #file = open('tempData.dat', 'wb')
        #pickle.dump(self, file)
        #file.close()
    

    

