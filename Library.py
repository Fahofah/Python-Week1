from abc import ABC,abstractmethod

class Library():

    def __init__(self):
        self.itemList=[]
        self.memberList=[]
        self.itemsFromFile=[]

    def addToList(self,thing):
        if(isinstance(thing,Items)):
            self.itemList.append(thing)
        if(isinstance(thing,Member)):
            self.memberList.append(thing)
    def printItems(self):
        for i in range(len(self.itemList)):
            if(isinstance(self.itemList[i],Book)):
                print("ID: {0}, Title: {1}, In Library: {2}, Author: {3}".format(self.itemList[i].id,self.itemList[i].title,self.itemList[i].inLibrary,self.itemList[i].author))
            elif(isinstance(self.itemList[i],Media)):
                print("ID: {0}, Title: {1}, In Library: {2}, Size: {3}".format(self.itemList[i].id,self.itemList[i].title,self.itemList[i].inLibrary,self.itemList[i].size))
            elif(isinstance(self.itemList[i],GDoc)):
                print("ID: {0}, Title: {1}, In Library: {2}, Classified: {3}".format(self.itemList[i].id,self.itemList[i].title,self.itemList[i].inLibrary,self.itemList[i].classified))
    def printMembers(self):
        for i in range(len(self.memberList)):
            print("Reg: {0}, Name: {1}, Age: {2}, Borrowed: {3}".format(self.memberList[i].reg,self.memberList[i].name,self.memberList[i].age,self.memberList[i].borrowed))
    
    def updateItem(self):
        id=input('Enter id number of the item to be updated\n')
        id=int(id)
        print('What would you like to update about {0}?\n1.Title\n2.In Library'.format(self.itemList[id-1].title))
        for i in range(len(self.itemList)):
            if(self.itemList[i].id==id):
                if(isinstance(self.itemList[i],Book)):
                    choice=input('3.Author\n')
                    choice=int(choice)
                    if(choice==1):
                        new_title=input('Enter new title\n')
                        self.itemList[i].title=new_title
                    elif(choice==2):
                        new_availability=input('Is this item in the library? Enter True or False\n')
                        self.itemList[i]=new_availability    
                    elif(choice==3):
                        new_author=input('Enter new author\n')
                        self.itemList[i].author=new_author
                    else:
                        print('Choice invalid')
                
                elif(isinstance(self.itemList[i],Media)):
                    choice=input('3.Size\n')
                    choice=int(choice)
                    if(choice==1):
                        new_title=input('Enter new title\n')
                        self.itemList[i].title=new_title
                        pass
                    elif(choice==2):
                        new_availability=input('Is this item in the library? Enter True or False\n')
                        self.itemList[i]=new_availability
                        pass
                    elif(choice==3):
                        new_size=input('Enter new size\n')
                        self.itemList[i].size=new_size
                        pass        
                    else:
                        print('Choice invalid')    
                elif(isinstance(self.itemList[i],GDoc)):
                    choice=input('3.Classified\n')
                    choice=int(choice)
                    if(choice==1):
                        new_title=input('Enter new title\n')
                        self.itemList[i].title=new_title
                        pass
                    elif(choice==2):
                        new_availability=input('Is this item in the library? Enter True or False\n')
                        self.itemList[i]=new_availability
                        pass
                    elif(choice==3):
                        new_class=input('Is the item classified? Enter True or False\n')
                        self.itemList[i].classified=new_class
                        pass
                    else:
                        print('Choice invalid')            
            else:
                print('Item id did not match records')
                  
    def updateMember(self):
        reg=input('Enter registration number of the member to be updated\n')
        reg=int(reg)
        for i in range(len(self.memberList)):
            if(self.memberList[i].reg==reg):
                choice=input('What would you like to update about {0}?\n1.Name\n2.Age\n'.format(self.memberList[reg-1].name))
                choice=int(choice)
                if(choice==1):
                    new_name=input('Enter new name\n')
                    self.memberList[i].name=new_name
                    pass
                elif(choice==2):
                    new_age=input('Enter new age\n')
                    self.memberList[i].age=new_age
                    pass
                else:
                    print('Invalid selection')
            else:
                print('Registration number did not match records')
    def registerMember(self):
        name=input("Input new member's name\n")
        age=input('Enter their age\n')
        new_member= Member(self.memberList[-1].reg+1,name,age)
        self.addToList(new_member)

    def addItem(self):
        itemType=input('What is the new item?\n1.Book\n2.Media\n3.Government Document\n')
        itemType=int(itemType)
        title=input('Enter title\n')
        inLibrary=True
        nextID=self.itemList[-1].id+1
        if(itemType==1):
            author=input('Enter author\n')
            new_item=Book(nextID,title,inLibrary,author)
        elif (itemType==2):
            size=input('Enter size\n')
            new_item=Media(nextID,title,inLibrary,size)
        elif (itemType==3):
            classified=input('Is document classified? Enter True or False\n')
            new_item=GDoc(nextID,title,inLibrary,classified)
        self.addToList(new_item)    

    def removeItem(self):
        id=input('Enter id number of the item to be removed\n')
        id=int(id)
        for i in range(len(self.itemList)):
            if(self.itemList[i].id==id):
                removed_title=self.itemList[i].title
                self.itemList.remove(self.itemList[i])
                print('{0} removed from library'.format(removed_title))

    def removeMember(self):
        reg=input('Enter registration number of the member to be removed\n')
        reg=int(reg)
        for i in range(len(self.memberList)):
            if(self.memberList[i].reg==reg):
                removed_name=self.memberList[i].name
                self.memberList.remove(self.memberList[i])
                print('{0} removed from library'.format(removed_name))

    def checkOutItem(self):
        itemID=input('Enter id of the item to be checked out\n')
        itemID=int(itemID)
        for i in range(len(self.itemList)):
            if(self.itemList[i].id==itemID):
                self.itemList[i].inLibrary=False
                borrower=input('Enter registration of member borrowing {0}\n'.format(self.itemList[i].title))
                borrower=int(borrower)
                for n in range(len(self.memberList)):
                    if(self.memberList[n].reg==borrower):
                        self.memberList[n].borrowed.append(itemID)
    
    def checkInItem(self):
        itemID=input('Enter id of the item to be checked in\n')
        itemID=int(itemID)
        for i in range(len(self.itemList)):
            if(self.itemList[i].id==itemID):
                self.itemList[i].inLibrary=True
                for n in range(len(self.memberList)):
                    self.memberList[n].borrowed.remove(itemID)

    def writeItemsToFile(self):
        fw=open("Library_items.txt","w")
        ilist=self.itemList
        for i in range(len(ilist)):
            if(isinstance(ilist[i],Book)):
                fw.write("{0},{1},{2},{3}\n".format(ilist[i].id,ilist[i].title,ilist[i].inLibrary,ilist[i].author))
                print('item written')
            elif(isinstance(ilist[i],Media)):
                fw.write("{0},{1},{2},{3}\n".format(ilist[i].id,ilist[i].title,ilist[i].inLibrary,ilist[i].size))
                print('item written')
            elif(isinstance(ilist[i],GDoc)):
                fw.write("{0},{1},{2},{3}\n".format(ilist[i].id,ilist[i].title,ilist[i].inLibrary,ilist[i].classified))
                print('item written')
        fw.close()

    def readItemsFromFile(self):
        fr=open("Library_items.txt","r")
        content=fr.readlines()
        w,h=4,len(content)
        tmp = [None]*w
        self.itemsFromFile=[[0 for x in range(w)] for y in range(h)] 
        for x in range(h):
            tmp=content[x].split(',')
            print()
            for y in range(w):
                self.itemsFromFile[x][y]=tmp[y]
                print(self.itemsFromFile[x][y])


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
     def __init__(self,reg,name,age):
        self.reg=reg
        self.name=name
        self.age=age
        self.borrowed=[]

class UI():
    def __init__(self):
        self.exit=False
        self.selection=-1

    def selectFunction(self):
        print('\nSelect a function to perform from the menu below: (To exit enter [e])')
        print('\n1.Check Out Item\n2.Check In Item\n3.Add Item\n4.Remove Item\n5.Update Item\
        \n6.Register Member\n7.Delete Member\n8.Update Member\n9.Display all item records\
        \n0.Display all member records\n99.Export library items list into file\
        \n98.Import items list from file to seperate repository')
        function=input()
        if(function=='e'):
            self.exit=True
            print('Logging off..')
        else:   
            self.selection=int(function)

ui=UI()
library=Library()

book1=Book(1,'alahambra',True,'Mike Jackson')
member1=Member(1,'Nicole',22)

library.addToList(book1)
library.addToList(member1)

while True:
    
    ui.selectFunction()
    
    if(ui.selection==1):
        library.checkOutItem()
        pass
    elif (ui.selection==2):
        library.checkInItem()
        pass
    elif (ui.selection==3):
        library.addItem()
        pass
    elif (ui.selection==4):
        library.removeItem()
        pass
    elif (ui.selection==5):
        library.updateItem()
        pass
    elif (ui.selection==6):
        library.registerMember()
        pass    
    elif (ui.selection==7):
        library.removeMember()
        pass
    elif (ui.selection==8):
        library.updateMember()
        pass
    elif (ui.selection==9):
        library.printItems()
        pass
    elif (ui.selection==0):
        library.printMembers()
        pass
    elif (ui.selection==99):
        library.writeItemsToFile()
        pass
    elif (ui.selection==98):
        library.readItemsFromFile()
        pass
    else:
        pass
    if(ui.exit==True):
        break           

