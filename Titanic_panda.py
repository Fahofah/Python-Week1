import pandas as pd
import random

data = pd.read_csv("titanic.csv")
pd.set_option("display.max_columns",12)
# print(data.head())
# empty_cells=pd.isnull()
col_names=list(data.columns.values)
# for i in range(len(col_names)):
#     empty_cells=pd.isnull(data[col_names[i]]).sum()
#     print('Column {0} has {1} empty/nan values'.format(col_names[i],empty_cells))



#Replace empty ages with average of ages
data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna(method='pad', limit=1, inplace=True)

#Replace e,pty values with most popular cabin (has multple, so brings up randomly)
most_cabins=data['Cabin'].value_counts().idxmax()
most_cabins=most_cabins.split(" ")
data['Cabin'].fillna(most_cabins[0], inplace =True)

# data['Cabin'].apply(lambda x: pd.random.choice([x for x in range(min(data['Cabin']),max(data['Cabin'])]), if (pd.isnan(x)) else x))

# print()
# for i in range(len(col_names)):
#     empty_cells=pd.isnull(data[col_names[i]]).sum()
#     print('Column {0} has {1} empty/nan values'.format(col_names[i],empty_cells))

# # print(data.groupby('Cabin')['PassengerId'].count())
titles=[]
names=[]
middle_names=[]
surnames=[]
other_names=[]
pro_names=[]
else_names=[]
counts=[]
split1=data['Name'].str.split(',')
for i in range(len(split1)):
    surnames.append(split1[i][0])
    namepart=split1[i][1].split(" (")
    if(len(namepart)>=2):
        other_names.append(namepart[1].replace(")",""))
    else:
        other_names.append('N/A')  
    act_name=namepart[0].split(" ")
    titles.append(act_name[1])
    if(len(act_name)<=2):
        names.append('N/A')
    else:
        names.append(act_name[2])
    if(len(act_name)>3):  
        middle_names.append(act_name[3])
    else:
        middle_names.append('N/A')
    if(len(act_name)>4):
        pro_names.append(act_name[4])
    else:
        pro_names.append('N/A')
    
    if(len(act_name)>5):
        else_names.append(act_name[5])
    else:
        else_names.append('N/A')


print('titles',len(titles))
print('names',len(names))
print('middle_names',len(middle_names))
print('surnames',len(surnames))
print('other_names',len(other_names))
print('else_names',len(else_names))
data['Title']=titles
data['First Name']=names
data['Middle Name']=middle_names
data['Surname']=surnames
data['Partner Names']=other_names
data['Other Names']=else_names
del data['Name']


data_notQ=data.loc[data.Embarked!='Q']
survivalRate_1stClassMen=len(data_notQ.loc[(data_notQ.Survived==1) & (data_notQ.Pclass==1) & (data_notQ.Sex=='male') & (data_notQ.Age>=21)])/len(data_notQ.loc[ (data_notQ.Sex=='male')  & (data_notQ.Pclass==1) & (data_notQ.Age>=21)])*100
print('survivalRate_1stClassMen: {0}%'.format(survivalRate_1stClassMen))
survivalRate_3rdClassChildren=len(data_notQ.loc[(data_notQ.Survived==1) &  (data_notQ.Pclass==3) & (data_notQ.Age<21)])/len(data_notQ.loc[(data_notQ.Age<21)  & (data_notQ.Pclass==3)])*100
print('survivalRate_3rdClassChildren: {0}%'.format(survivalRate_3rdClassChildren))
if(survivalRate_1stClassMen<survivalRate_3rdClassChildren):
    print('3rd class children had higher survival rate')
elif(survivalRate_1stClassMen==survivalRate_3rdClassChildren):
    print('3rd class children and 1st class males had same survival rate')
else:
    print('1st class men had higher survival rate than 3rd class children')   