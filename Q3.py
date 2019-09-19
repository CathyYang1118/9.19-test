FileOpen = open('Q2.txt','r')

InputNumber = input('input a number:') #string
printnot = 0
for i in FileOpen.readlines(): #string
    count = 0
    num = ''
    for j in i: #string
        count+=1
        #print(count,j)
        if count <= 4:
            num += j
    if str(num) == str(InputNumber):
        print(i)
        printnot = 1
if printnot == 0:
    print('No such student')
        
    
