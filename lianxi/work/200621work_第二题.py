
inflie = 'D:/file1.txt'
outfile = 'D:/file2.txt'
#读取文件1中的数据，创建一个文件夹2写入数据
with open(inflie) as ifile,open(outfile,'w') as ofile:
    #创建列表接收读取文件1中的每行数据
    beforeTax = ifile.read().splitlines()
    # print(beforeTax)
    for one in beforeTax:#遍历接收的数据列表
        namePart,salaryPart = one.split(';')#以';'截取列表列表数据
        name =  namePart.split(":")[1].strip()#获取截取数据中分号后的数据并去掉前后空格
        # print(name)
        salary = int(salaryPart.split(':')[1].strip())#获取截取数据中分号后的数据并去掉前后空格转化为int类型
        # print(salary)
        income =int(salary*0.9)#计算税后金额
        tax = int(salary*0.1)#计算扣税金额
        #通过字符串传值写入字符串
        outPutStr ='name:{:6} ; salary:{:6} ;  tax:{:6} ;  income:{:6}'.format(name,salary,tax,income)
        #把字符串内容写入到第二个文件中file2.txt
        ofile.write(outPutStr+'\n')