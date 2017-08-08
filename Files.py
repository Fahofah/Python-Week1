class Person():

    def __init__(self,name,occupation,age):
        self.name=name
        self.occupation=occupation
        self.age=age

p1= Person('Nelu','Brick Layer',32)
p2= Person('Sarah', 'Receptionist', 27)
p3= Person('Miha','Surveyor',36)
p4= Person('Malinda','Customer Relations',24)
p5= Person('Babu','Lead Builder',45)

people_list=[p1,p2,p3,p4,p5]

fw=open("People_list.txt","w")
for i in people_list:
    fw.write("{0},{1},{2}\n".format(i.name,i.occupation,i.age))
fw.close()

fr=open("People_list.txt","r")
content=fr.readlines()
w,h=3,len(content)
tmp = [None]*w
peopleFromFile_list=[[0 for x in range(w)] for y in range(h)] 
for x in range(h):
    tmp=content[x].split(',')
    for y in range(w):
        peopleFromFile_list[x][y]=tmp[y]
        print(peopleFromFile_list[x][y])
