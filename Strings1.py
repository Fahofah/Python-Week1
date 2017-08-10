string1 = 'ABCDGH'
string2 = 'AEDFHR'
subsequence=[]
pos2prev=-1

for i in range(len(string2)):
    if(string2[i] in string1):
        pos2=string1.index(string2[i])
        if( pos2>=pos2prev and string2[i] not in subsequence):
            subsequence.append(string2[i])
            pos2prev=pos2

print(subsequence)
