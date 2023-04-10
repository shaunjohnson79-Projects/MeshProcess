import nastranProcess.nastranClass as nastran  
  
      
def main():
    print("main: start")
    fileName="nastran_input.nas"
    
    nastranData=nastran.ReadFile(fileName)

    print("main: end")

if __name__ == "__main__":
    main()