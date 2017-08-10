string1= 'catterpilar'
string2='rooster'
subsequence=[]
common= ""

for i in range(len(string2)):
    if(string2[i] in string1):
        subsequence.append(string2[i])
additions=string1
for i in range(len(subsequence)):
    additions=additions.replace(subsequence[i],"",1)

for i in range(len(subsequence)):
    common+=(subsequence[i])

remove=string2
commonSet=str(set(common))

for i in range(len(commonSet)):
    remove=remove.replace(commonSet[i],"",1)

print('\nTo get {0} from {1}, we need to remove characters: '.format(string1,string2), end='')
print(remove, end='')
print('\nand add characters: {0}'.format(additions))