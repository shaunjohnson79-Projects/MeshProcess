#import pickle
import numpy as np
from typing import Self

from .lineTypeClass import LineType
from .lineTypeClass import MeshCount
from .generalMethods import convertToFloat,convertToInt
from .generalMethods import divideStringArrayFixedWidth, getEnum

class Mesh():
    def __init__(self) -> None:
        print("Mesh init")
        
    def convert(self,rawData) -> Self:

        #lineType=rawData.getLineTypes
  
        self.pointer={}
        self.tempElementNumber={}
        self.mesh={}
  
        for MT in MeshCount:
            LThandle=getEnum(MT.name,LineType)
            MThandle=getEnum(MT.name,MeshCount)
            
            print(LThandle.value)
            print(MThandle.value)

            tempLines=rawData.data[rawData.getLineTypes == LThandle]

            # Divide the lines by fixed width
            width=8
            tempLines=divideStringArrayFixedWidth(tempLines,width)
            
            # Pointer
            tempPointer=tempLines[:,[1]]
            tempPointer=convertToInt(tempPointer)
            
            # elementNumber??
            tempElementNumber=tempLines[:,[2]]
            tempElementNumber=convertToInt(tempElementNumber)  
            
            # Mesh
            tempMesh=tempLines[:,3:]
            tempMesh=convertToInt(tempMesh)
            tempMesh=tempMesh[:,:int(MThandle.value)]

            tempDictName=str(LThandle.value)
            print(tempDictName)
            
            # Add to dictionary
            self.pointer[tempDictName]=tempPointer
            self.tempElementNumber[tempDictName]=tempElementNumber
            self.mesh[tempDictName]=tempMesh
        
