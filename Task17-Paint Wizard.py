#Task17 - Paint Wizard
import math

class Paint():

    def __init__(self,name,capacity,price,coverage):
        self.name=name
        self.capacity=capacity
        self.price=price
        self.coverage=coverage
        self.tin_per_area=1/(coverage*capacity)
        self.waste=-1
        self.cost=-1

    def cal_waste(self,paint_area):
        tin_count=self.tin_per_area*paint_area
        tin_waste=math.ceil(tin_count)-tin_count
        metre_waste=tin_waste*self.capacity*self.coverage
        self.waste= metre_waste
    
    def cal_cost(self,paint_area):
        self.cost= self.tin_per_area*paint_area*self.price

p1= Paint('CheapoMax',20,19.99,10)
p2= Paint('AverageJoes',15,17.99,11)
p3= Paint('DuluxourousPaints',10,25,20)

paint_list= [p1,p2,p3]
minWaste_list = [None] * len(paint_list)
minCost_list =   [None] * len(paint_list)

paint_area=599
tmp=1000
tmp2=1000
x=0
y=0
for i in paint_list:
    Paint.cal_waste(i,paint_area)
    if(i.waste<=tmp):
        tmp=i.waste
        minWaste_list[x]=i 
        x=x+1
    Paint.cal_cost(i,paint_area)
    if(i.cost<=tmp2):
        tmp2=i.cost
        minCost_list[y]=i 
        y=y+1
print('Paint(s) with minimum waste on this project:')
for i in minWaste_list:
    if(isinstance(i,Paint)):
        print('- ',i.name,' with ', i.waste, 'metre square waste ')
print()
print('Paint(s) with minimum cost on this project:')
for i in minCost_list:
    if(isinstance(i,Paint)):
        print('- ',i.name,' with £', i.cost, ' cost ')


