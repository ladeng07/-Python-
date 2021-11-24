def create_file (name='files',Extension='py',Route='F:\\python\\py\\'):
    file = open (Route+name+'.'+Extension,'w')
    print ('finishied!')
create_file (input('请输入文件名：'),input('请输入拓展名:'))
