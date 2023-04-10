class Person():
    
    def __init__(self,name,age):
        self.name=name
        self.age=age

def main():
    personList={}
    aa=Person('aa',10)
    bb=Person('bb',20)
    
    personList[aa.name]=aa
    personList[bb.name]=bb
    
    print(personList)
    
    print(personList["aa"].age)
    


if __name__ == "__main__":
    main()