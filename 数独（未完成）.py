def square(line_index,column_index,num):
    if line_index < 3:
        if column_index < 3:
            for each_line in lines[:3]:
                for each in each_line[:3]:
                    for i in each:
                        if num == i:
                            return False
                        else:
                            pass
            return True
                        
        elif 3 <= column_index < 6:
            for each_line in lines[:3]:
                for each in each_line[3:6]:
                    for i in each:
                        if num == i:
                            return False
                        else:
                            pass
            return True
        elif 6 <= column_index <9:
            for each_line in lines[:3]:
                for each in each_line[6:9]:
                    for i in each:
                        if num == i:
                            return False
                        else:
                            pass
            return True
    elif 3 <= line_index < 6:
        if column_index < 3:
            for each_line in lines[3:6]:
                for each in each_line[:3]:
                    for i in each:
                        if num == i:
                            return False
                        else:
                            pass
            return True
        elif 3 <= column_index < 6:
            for each_line in lines[3:6]:
                for each in each_line[3:6]:
                    for i in each:
                        if num == i:
                            return False
                        else:
                            pass
            return True
        elif 6 <= column_index <9:
            for each_line in lines[3:6]:
                for each in each_line[6:9]:
                    for i in each:
                        if num == i:
                            return False
                        else:
                            pass
            return True
    elif 6 <= line_index <9:
        if column_index < 3:
            for each_line in lines[6:9]:
                for each in each_line[:3]:
                    for i in each:
                        if num == i:
                            return False
                        else:
                            pass
            return True
        elif 3 <= column_index < 6:
            for each_line in lines[6:9]:
                for each in each_line[3:6]:
                    for i in each:
                        if num == i:
                            return False
                        else:
                            pass
            return True
        elif 6 <= column_index <9:
            for each_line in lines[6:9]:
                for each in each_line[6:9]:
                    for i in each:
                        if num == i:
                            return False
                        else:
                            pass
            return True



def each_column(index,num):
    for each in lines:
        if num == each[index]:
            return False
        else:
            pass
    return True




def main(liness):
	global lines
	lines = liness
	for line_index,line in enumerate(lines):
		for index,each in enumerate(line):
			if each == '0':
				l = []
				for i in range(1,10):
					if str(i) not in line and each_column(index,str(i)) and square(line_index,index,str(i)):
						l.append(str(i))
					else:
						pass
				if len(l) == 1:
					#print(l[0])
					line = line.replace('0',l[0],1)
					lines[line_index] = line
					#print(lines[line_index])
	if lines != liness:
		main( lines)
	else:
		return print(lines)                  
shudu1 = ['902547360',"465003027","730926805","006815479","809364502","514070083","157098206","240601090","098730154"]

shudu2 = ["000056810","070000000","800010300","040009003","000080000","190000048","015008002","069270405","200540600"]

main(shudu2)
