from pytictoc import TicToc
from dataclasses import dataclass

from .rawDataClass import RawData
from .gridClass import Grid
from .meshClass import Mesh
from .lineTypeClass import LineType



@dataclass
class ReadFile():

    def __init__(self, fileName) -> None:
        """Read the nastran file"""
        
        # Start timer
        timer = TicToc()
        timer.tic()
        

        self.fileName = fileName
        
        self.rawData = RawData().read(fileName)
        self.grid = Grid().convert(self.rawData)
        self.mesh = Mesh().convert(self.rawData)
        
        timer.toc("Read nastran file:")
        
               
        #print(self.rawData.display())
        #print(self.rawData.numberOfLines)
        #print(self.rawData.CountEnumType(LineType.GRID))
        

        #file = open('tempData.dat', 'wb')
        #pickle.dump(self, file)
        #file.close()
        
    

