FileOpen = open('Q1.txt','r')
FileWrite = open('Q2.txt','w')

name = input('input a name:')#string
InputName = ''#string
for n in name:
    count = 0 #intiger
    if n != ' ':
        InputName+=n

num = 0 #int

for i in FileOpen.readlines(): #string
    count = 0 #integer
    FirstName = '' #string
    LastName = '' #string
    for j in i: 
        if j == '@': #during the first question, I changed the space into the @
            count+=1
        if count <1:
            FirstName += j
        if count == 1:
            LastName += j
    LastName = LastName[1:] #string
    num += 1
    TestName = FirstName+LastName #string
    if TestName != InputName:
        num2='0'*(4-len(str(num)))+str(num) #string
        FileWrite.write(num2)
        FileWrite.write(i)

FileOpen.close()
FileWrite.close()
