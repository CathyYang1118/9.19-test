FileOpen = open('qbdata.txt','r')
FileWrite = open('Q1.txt','w')

character = input('input a character:') #string

for i in FileOpen.readlines(): #string
    for j in i: #string
        if j == ' ':
            j = character
        FileWrite.write(j)

FileOpen.close()
FileWrite.close()
