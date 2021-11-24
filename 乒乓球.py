inputs = input()
inputss = []
details = ""
while inputs.find('E') == -1:
    inputss.append(inputs)
    inputs = input()
inputss.append(inputs)
details = "".join(inputss)
def show(n,details):
    w = 0
    l = 0
    for i in details:
        if i == 'W':
            w = w+1
        if i == 'L':
            l = l +1
        if ((w >= n) or (l >= n)) and abs(w-l) >= 2:
            print(str(w)+":"+str(l))
            w = 0
            l = 0
        if i == 'E':
            print(str(w)+":"+str(l))
            break
#11分制
show(11,details)
print("")
#21分制
show(21,details)
    
