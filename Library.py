from abc import ABC,abstractmethod

class Library():

    def __init__(self):
        self.itemList=[]
        self.memberList=[]
        self.borrowedList=[]

    def addToList(self,thing):
        if(isinstance(thing,Items)):
            print('book')
            self.itemList.append(thing)
        if(isinstance(thing,Member)):
            self.memberList.append(thing)
    def printItems(self):
        for i in range(len(self.itemList)):
            print("{0},{1},{2},{3}".format(self.itemList[i].id,self.itemList[i].title,self.itemList[i].inLibrary,self.itemList[i].author))

    def printMembers(self):
        for i in range(len(self.memberList)):
            print("{0},{1},{2},{3}".format(self.memberList[i].reg,self.memberList[i].name,self.memberList[i].age,self.memberList[i].borrowed))
    
class Items(ABC):
    def __init__(self,id,title,inLibrary):
        self.id=id
        self.title=title
        self.inLibrary=inLibrary

class Book(Items):
    def __init__(self,id,title,inLibrary,author):
        super().__init__(id,title,inLibrary)
        self.author=author
class Media(Items):
     def __init__(self,id,title,inLibrary,size):
        super().__init__(id,title,inLibrary)
        self.size=size
class GDoc(Items):
     def __init__(self,id,title,inLibrary,classified):
        super().__init__(id,title,inLibrary)
        self.classified=classified

class Member():
     def __init__(self,reg,name,age,borrowed):
        self.reg=reg
        self.name=name
        self.age=age
        self.borrowed=borrowed

book1=Book(1,'alahambra',True,'Mike Jackson')
member1=Member(1,'Nicole',22,False)
library=Library()

library.addToList(book1)
library.addToList(member1)

library.printItems()
library.printMembers()
