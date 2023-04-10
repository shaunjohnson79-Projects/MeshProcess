from pytictoc import TicToc

from .rawDataClass import RawData





class Nastran:
    def __init__(self) -> None:
        # define variables
        self.fileName = str
        self.precision = 8
        self.isGood = False
        
        # read the data
        #self.readData()
    
    def __repr__(self):
        returnString = ''
        returnString += f"Nastran\n"
        returnString += f"Filename: {self.fileName}\n"
        returnString += f"precision: {self.precision}\n"
        returnString += f"isGood: {self.isGood}\n"
        return returnString
    
    def readfromFile(self,fileName) -> None:
        """Read the file data"""
        
        self.fileName=fileName
        
        # Start timer
        timer = TicToc()
        timer.tic()
        
        self.rawData = RawData().read(fileName)
        
        # Stop timer
        timer.toc("Read nastran file:")
        
        #

    #def __init__(self, fileName) -> None:
        #"""Read the nastran file"""
        

        

        #self.fileName = fileName
        #self.rawData = RawData().read(fileName)
        #self.grid = Grid().convert(self.rawData)
        #self.mesh = Mesh().convert(self.rawData)
        
        #timer.toc("Read nastran file:")
        
               
        #print(self.rawData.display())
        #print(self.rawData.numberOfLines)
        #print(self.rawData.CountEnumType(LineType.GRID))
        

        #file = open('tempData.dat', 'wb')
        #pickle.dump(self, file)
        #file.close()
        
    

